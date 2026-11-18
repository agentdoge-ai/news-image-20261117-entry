#!/usr/bin/env python3
"""Copy entry.png to /output/entry.png, byte-for-byte.

The entry image lives next to this script. This program copies it
unchanged to /output/entry.png (creating /output if needed) and prints
the destination path plus the SHA-256 of the bytes it wrote, so the
copy can be checked against the source.

Deterministic: every run writes the exact same bytes, because it is a
plain byte-for-byte copy with no re-encoding or modification.

Usage:
    python3 main.py

Exit code is 0 on success, non-zero with a clear error on failure.
"""

import hashlib
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
DEST_DIR = Path("/output")
DEST = DEST_DIR / "entry.png"

CHUNK_SIZE = 1024 * 1024  # 1 MiB


def sha256_of(path):
    """Return the hex SHA-256 digest of the file at *path*."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(CHUNK_SIZE)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not SOURCE.is_file():
        print(f"error: entry.png not found next to the script: {SOURCE}",
              file=sys.stderr)
        return 1

    DEST_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)

    digest = sha256_of(DEST)

    # Verify the copy: the output must be byte-identical to the source.
    source_digest = sha256_of(SOURCE)
    if digest != source_digest:
        print("error: output hash does not match source hash "
              f"(source {source_digest}, output {digest})",
              file=sys.stderr)
        return 1

    size = DEST.stat().st_size
    print(f"wrote {DEST}")
    print(f"sha256: {digest}")
    print(f"verified: output matches source ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
