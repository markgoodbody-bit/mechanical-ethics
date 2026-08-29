#!/usr/bin/env python3
"""Verify the frozen Mechanical Ethics v0.7.0 working candidate surface."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CANDIDATE = Path("work/v0_7_0/MECHANICAL_ETHICS_HUMAN_READER_v0_7_0_NEXT_WORKING_CANDIDATE_v0_2.md")

EXPECTED = {
    CANDIDATE: (87177, "56b09d5a1f7f0db5102ad47a636c60273cd2ddc325d216b4414e5359f21604a7"),
    Path("work/v0_7_0/figures/figure-1-file-and-life.svg"): (3268, "7e925765434bc701d5eacb88972a8f9715bc4a66d548e5b569d9c9a99692c2bb"),
    Path("work/v0_7_0/figures/figure-1-file-and-life.png"): (81671, "bc19a7b7121faba611ef900470398ad5981ae1d1ff44faa79b3912b2a449ec00"),
    Path("work/v0_7_0/figures/figure-2-correction-window.svg"): (2887, "4d1570e07bfb8dcf7a3b9c7fc6cf380f1522e3b49b29fbf78df218be99069a5f"),
    Path("work/v0_7_0/figures/figure-2-correction-window.png"): (58039, "d1df6bea949b7db9bb64fd76fda35921d49473503b920b85ccae83864c445bc3"),
    Path("work/v0_7_0/figures/figure-3-two-flats-one-wall.svg"): (3756, "0d98a7ea605bf9a440f0d315b5ca62fb2c4144d4cedea78bad81cbad5119db11"),
    Path("work/v0_7_0/figures/figure-3-two-flats-one-wall.png"): (69949, "e6e0a457e3e1225edb1b29e0be9e698b988814270578d75ebd381f6bbab928d1"),
    Path("work/v0_7_0/figures/figure-4-machine-speed-human-correction.svg"): (3979, "c17f04eb3d3c22e6b1d62eae7e505ba0bd42e7f6a6c6a76d45d263bdd2e5662a"),
    Path("work/v0_7_0/figures/figure-4-machine-speed-human-correction.png"): (65773, "4d0f41aa5eb560b6afe1b9e2102c99a8476d2c9211a380d6c401192016797ebf"),
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    errors: list[str] = []

    for relative, (expected_bytes, expected_hash) in EXPECTED.items():
        path = REPO / relative
        if not path.is_file():
            errors.append(f"missing controlled file: {relative.as_posix()}")
            continue
        data = path.read_bytes()
        if len(data) != expected_bytes:
            errors.append(
                f"byte mismatch for {relative.as_posix()}: expected {expected_bytes}, observed {len(data)}"
            )
        observed_hash = sha256(data)
        if observed_hash != expected_hash:
            errors.append(
                f"SHA-256 mismatch for {relative.as_posix()}: expected {expected_hash}, observed {observed_hash}"
            )

    candidate_path = REPO / CANDIDATE
    if candidate_path.is_file():
        text = candidate_path.read_text(encoding="utf-8")
        if len(text.splitlines()) != 922:
            errors.append(f"candidate line count is {len(text.splitlines())}, expected 922")
        if len(text.split()) != 14080:
            errors.append(f"candidate whitespace word count is {len(text.split())}, expected 14080")

        image_links = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)
        expected_links = {
            "figures/figure-1-file-and-life.png",
            "figures/figure-2-correction-window.png",
            "figures/figure-3-two-flats-one-wall.png",
            "figures/figure-4-machine-speed-human-correction.png",
        }
        if set(image_links) != expected_links or len(image_links) != 4:
            errors.append(f"candidate image links do not match the four controlled PNGs: {image_links}")
        for link in image_links:
            if not (candidate_path.parent / link).is_file():
                errors.append(f"broken candidate image link: {link}")

        required_ceiling = (
            "The timing condition is not a universal priority rule. "
            "Using it as if it ranked competing lives, paths, or claims would be a misuse."
        )
        if required_ceiling not in text:
            errors.append("candidate priority-misuse ceiling is absent or changed")

    if errors:
        print("ME v0.7.0 candidate verification: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("ME v0.7.0 candidate verification: PASS")
    print("- candidate identity: exact")
    print("- figure identities: exact")
    print("- four candidate image links: present")
    print("- priority-misuse ceiling: present")
    print("This verifies controlled bytes and declared surface only; it does not validate the argument.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
