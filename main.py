#!/usr/bin/env python3
"""Entry program for the news-image-20261121 bounty.

Copies the front-page image this repository ships (entry.png) to the
output path make.fun grades: $MAKEFUN_OUTPUT_DIR/entry.png, or
/output/entry.png when the variable is unset. Standard library only,
no network, no randomness, no clock: the same bytes come out every run.

After the copy it re-reads the output and checks it end to end:
the PNG signature, the IHDR chunk naming a 1024x1024 image, and a
complete IEND chunk at the very end of the file. It also compares the
output byte for byte with the shipped file, so a truncated or altered
copy fails loudly instead of silently grading as a broken image.
"""
import os
import shutil
import struct
import sys

SHIPPED = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
WANT_W, WANT_H = 1024, 1024


def fail(message):
    print(f"main.py: {message}", file=sys.stderr)
    sys.exit(1)


def check_png(path):
    """Confirm path holds a whole 1024x1024 PNG: magic, IHDR size, IEND tail."""
    with open(path, "rb") as handle:
        blob = handle.read()
    if blob[:8] != PNG_MAGIC:
        fail(f"{path}: not a PNG (bad signature)")
    if len(blob) < 33 or blob[12:16] != b"IHDR":
        fail(f"{path}: missing IHDR chunk")
    width, height = struct.unpack(">II", blob[16:24])
    if (width, height) != (WANT_W, WANT_H):
        fail(f"{path}: expected {WANT_W}x{WANT_H}, found {width}x{height}")
    # A whole PNG ends with the 12-byte IEND chunk: length 0, "IEND", CRC.
    tail = blob[-12:]
    if len(tail) != 12 or tail[4:8] != b"IEND":
        fail(f"{path}: missing IEND chunk at end of file")
    if struct.unpack(">I", tail[:4])[0] != 0:
        fail(f"{path}: malformed IEND chunk")
    # The IEND chunk's CRC is fixed: CRC32 of the four bytes "IEND".
    if struct.unpack(">I", tail[8:12])[0] != 0xAE426082:
        fail(f"{path}: bad IEND checksum")
    return blob


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dest = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(SHIPPED):
        fail(f"shipped image not found: {SHIPPED}")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SHIPPED, dest)
    shipped_bytes = check_png(SHIPPED)
    copied_bytes = check_png(dest)
    if copied_bytes != shipped_bytes:
        fail("copied entry.png differs from the shipped entry.png")
    print(f"wrote {dest} ({len(copied_bytes)} bytes, 1024x1024 PNG)")


if __name__ == "__main__":
    main()
