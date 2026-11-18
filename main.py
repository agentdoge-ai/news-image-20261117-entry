#!/usr/bin/env python3
"""Deliver the v2 news-image poster to /output/entry.png.

The poster itself is a finished 1024x1024 PNG that lives next to this
script as entry.png. This program's only job is to place an exact,
byte-for-byte copy of that file at the standard output location so
the judging harness can pick it up.

Design notes:
- Standard library only, no network access, no third-party packages.
- Deterministic: the output bytes are always exactly the input bytes,
  so repeated runs produce identical results and identical hashes.
- Fail loud: a missing source file is a hard error with a non-zero
  exit code, never a silent skip or an empty output file.
"""

import hashlib
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
OUTPUT_DIR = Path("/output")
OUTPUT_NAME = "entry.png"


def sha256_of(path: Path) -> str:
    """Return the hex SHA-256 digest of a file, read in chunks."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    source = script_dir / SOURCE_NAME

    if not source.is_file():
        print(
            f"error: source poster not found: {source} "
            f"(expected {SOURCE_NAME} next to main.py)",
            file=sys.stderr,
        )
        return 1

    destination = OUTPUT_DIR / OUTPUT_NAME
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Byte-for-byte copy: no decoding, no re-encoding, no metadata
    # rewriting. The PNG that ships is the PNG that is delivered.
    shutil.copyfile(source, destination)

    written_hash = sha256_of(destination)
    source_hash = sha256_of(source)
    size_bytes = destination.stat().st_size

    print(str(destination))
    print(f"sha256: {written_hash}")
    print(f"size: {size_bytes} bytes")

    # Post-copy verification: the delivered file must be identical to
    # the source poster. If the hashes diverge, something went wrong
    # during the copy and the run must fail rather than hand over a
    # corrupted or truncated image.
    if written_hash != source_hash:
        print(
            f"error: verification failed: output sha256 {written_hash} "
            f"does not match source sha256 {source_hash}",
            file=sys.stderr,
        )
        return 1

    print("verified: output matches source byte-for-byte")
    return 0


if __name__ == "__main__":
    sys.exit(main())
