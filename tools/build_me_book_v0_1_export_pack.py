#!/usr/bin/env python3
"""
Build a compact Mechanical Ethics book export pack.

Purpose:
- Keep user-facing ZIPs under 10 files.
- Preserve the repo's editable multi-file book structure.
- Generate one consolidated full reader from the source book files.
- Keep the export pack aligned with the value-spine propagation pass.

Run from the repository root:

    python tools/build_me_book_v0_1_export_pack.py

Optional:

    python tools/build_me_book_v0_1_export_pack.py --date 2026_06_27 --out-dir dist

The generated ZIP contains 7 files by design.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import textwrap
import zipfile
from datetime import date
from pathlib import Path

BOOK_DIR = Path("01_BOOK_DRAFT/ME_BOOK_v0_1")
PACK_FILE_LIMIT = 10

FULL_READER_SOURCES = [
    "00_TITLE_AND_CONTROL.md",
    "PART_0_HOW_TO_READ_THIS_BOOK.md",
    "PART_1_THE_ENTITY_THAT_WAKES.md",
    "PART_2_THE_WORLD_THAT_PUSHES_BACK.md",
    "PART_3_LAYERS_OF_ACTION.md",
    "PART_4_HARM_TIME_AND_FUTURE_SPACE.md",
    "PART_5_DESCRIPTION_IS_NOT_PERMISSION.md",
    "PART_6_THE_FIRST_GATES.md",
    "PART_7_PROTECTION_STANDING_AND_SCOPE.md",
    "PART_8_CORRECTION_REPAIR_AND_RESIDUE.md",
    "PART_9_DIRTY_CONFLICTS.md",
    "PART_10_RESPONSIBILITY_AFTER_VISIBILITY.md",
    "PART_11_POWER_LEGITIMACY_AND_COERCION.md",
    "PART_12_CIVILIZATION_UNDER_UNCERTAINTY.md",
    "PART_13_ARTIFICIAL_SYSTEMS_AND_FUTURE_MINDS.md",
    "PART_14_CASE_RECORDS_AND_USE_PROTOCOLS.md",
    "PART_15_LIMITS_FAILURES_AND_OPEN_QUESTIONS.md",
]

COPY_FILES = {
    "04_STRUCTURAL_REVIEW.md": "STRUCTURAL_REVIEW_v0_1_2026_06_27.md",
    "05_REVIEW_PROMPT.md": "CLAUDE_REVIEW_PROMPT_v0_1.md",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip() + "\n"


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require_sources(repo_root: Path) -> None:
    missing = []
    for rel in FULL_READER_SOURCES:
        if not (repo_root / BOOK_DIR / rel).exists():
            missing.append(str(BOOK_DIR / rel))
    for rel in COPY_FILES.values():
        if not (repo_root / BOOK_DIR / rel).exists():
            missing.append(str(BOOK_DIR / rel))
    if missing:
        raise FileNotFoundError("Missing source files:\n" + "\n".join(missing))


def build_full_reader(repo_root: Path) -> str:
    sections = [
        "# Mechanical Ethics — Book v0.1 — Full Reader\n\n"
        "Status: first full wide-pass draft with value-spine propagation across Parts 1-15. "
        "Not canon. Not public release. Not validation. Not final moral law.\n\n"
        "Generated from source files in `01_BOOK_DRAFT/ME_BOOK_v0_1/`.\n"
    ]
    for rel in FULL_READER_SOURCES:
        source_path = repo_root / BOOK_DIR / rel
        sections.append("\n---\n\n")
        sections.append(f"<!-- Source: {BOOK_DIR / rel} -->\n\n")
        sections.append(read_text(source_path))
    return "".join(sections)


def start_here(pack_name: str) -> str:
    return f"""
    # START HERE — Mechanical Ethics Book v0.1 Export Pack

    Pack: `{pack_name}`

    Status:

    ```trace
    ME_book_v0_1_export_status :=
      first_full_wide_pass_draft
      + value_spine_propagated_parts_1_to_15
      + compact_export_pack
      + not_canon
      + not_public_release
      + not_validation
      + not_final_moral_law
    ```

    Use this pack for review, reading, or model ingestion where a small number of files is preferable.

    Current spine:

    ```trace
    ME_book_current_spine :=
      answerable_transition_under_uncertainty
      + viable_becoming_candidate
      + claimed_good_audit
      + honest_burden_record
      + residue_visibility
      + actor_answerability
    ```

    File count discipline:

    ```trace
    export_pack_file_count_target := <= 10
    actual_file_count := 7
    ```

    Suggested reading order:

    1. `01_START_HERE.md`
    2. `02_ME_BOOK_v0_1_FULL_READER.md`
    3. `03_STATUS_LIMITS_AND_OPEN_WOUNDS.md`
    4. `04_STRUCTURAL_REVIEW.md`
    5. `05_REVIEW_PROMPT.md`
    6. `06_CASE_RECORD_TEMPLATE.md`
    7. `07_NEXT_PASS_PLAN.md`
    """


def status_limits() -> str:
    return """
    # Status, Limits, and Open Wounds

    ```trace
    status :=
      first_full_wide_pass_draft
      + value_spine_propagated_parts_1_to_15
      + structurally_reviewed_in_loop
      + not_validated
    ```

    This pack is not canon, not public release, not validation, and not final moral law.

    Current structural achievements:

    ```trace
    achieved :=
      middle_out_origin_preserved
      + TRACE_in_the_walls
      + description_is_not_permission
      + first_gates_earned
      + protection_as_viable_becoming_added
      + correction_repair_residue_split
      + repair_as_reopened_viable_future
      + dirty_conflict_as_incompatible_viable_becoming
      + responsibility_for_seen_openings_and_closures
      + power_over_viable_becoming
      + civilization_as_shared_correctability_and_shared_viable_becoming
      + AI_split_preserved
      + local_reward_not_structural_good
      + claimed_good_audit_added
      + protocol_minimization_rule_preserved
    ```

    Remaining open wounds:

    ```trace
    open_wounds :=
      final_floor_foundation_for_scope_protection
      + final_theory_of_the_good
      + acceptable_sacrifice
      + full_legitimacy_theory
      + punishment_and_desert
      + dignity_beyond_recognition
      + artificial_moral_standing
      + future_mind_recognition
      + corrigibility_vs_binding_commitment
      + value_lock_in
      + validation_of_usefulness
    ```

    Current value-spine limit:

    ```trace
    viable_becoming_status :=
      candidate_structural_account
      + not_final_theory_of_good
      + must_remain_scoped
      + must_remain_revisable
    ```

    Main next-pass risk:

    ```trace
    next_pass_risk :=
      prose_polish_before_case_pressure
      + viable_becoming_used_as_slogan
      + claimed_good_used_as_clearance
    ```

    Do not polish yet. Add small case pressure first.
    """


def case_record_template() -> str:
    return """
    # Minimum Case Record Template

    Use this only when a case needs Mechanical Ethics. Low-fit cases should stay small.

    ```trace
    minimum_viable_case_record :=
      decision_or_question_on_the_table
      + transition_description
      + at_least_one_affected_scope
      + future_space_comparison_for_that_scope
      + viable_becoming_record
      + at_least_one_clock_using_TRACE_bands
      + first_gates_results
      + router_finding
      + prescription_audit
    ```

    ## 1. Decision or question on the table

    What is being decided, reviewed, paused, repaired, escalated, or challenged?

    ## 2. Transition description

    What changed, or what is proposed to change?

    ## 3. Affected scope or scopes

    Who or what may have future-space or viable becoming changed?

    ## 4. Future-space comparison

    Record options, reachability, and usable information where possible. Do not fake scalar math.

    ## 5. Viable becoming record

    ```trace
    viable_becoming_record :=
      affected_scope
      + continuation_change
      + orientation_change
      + capacity_change
      + relation_change
      + repairability_change
      + meaningful_future_space_change
      + confidence
    ```

    ## 6. Clock

    Identify loss clock, opportunity clock, correction timing, or UNKNOWN.

    ## 7. Claimed-good audit

    ```trace
    claimed_good_audit :=
      what_good_is_claimed
      + for_whom
      + what_viable_becoming_expands
      + what_viable_becoming_contracts
      + who_carries_cost_or_risk
      + what_correction_stays_live
      + what_residue_remains
    ```

    ## 8. First gates

    Check hidden loss, erased scopes, uncertainty, residue, channel harm, clock-setting, emergency laundering, and benefit laundering.

    ## 9. Router finding

    Use findings narrowly. Findings are not authorizations.

    ## 10. Prescription audit

    Name value priority added, claimed good, dirty or unrepaired loss, residue, responsibility remaining, and laundering risk.
    """


def next_pass_plan() -> str:
    return """
    # Next Pass Plan

    The next pass should add case pressure, not line polish.

    ```trace
    next_pass_order :=
      integrity_check
      -> small_case_threads
      -> positive_route_with_burden_case
      -> administrative_delay_late_correction_case
      -> algorithmic_classification_false_positive_case
      -> dirty_conflict_case
      -> only_then_prose_tightening
    ```

    Case threads should be small and recurring. Do not turn the book into a casebook yet.

    Candidate case set:

    ```trace
    case_set :=
      routine_low_fit_coordination
      + positive_route_with_burden
      + administrative_delay_late_correction
      + algorithmic_classification_false_positive
      + animal_ecology_dirty_conflict
      + emergency_power_with_prior_neglect
    ```

    Immediate test questions:

    ```trace
    immediate_test_questions :=
      does_the_value_spine_catch_real_good_without_cleaning_loss
      + does_claimed_good_audit_prevent_benefit_laundering
      + does_viable_becoming_remain_probe_not_total_doctrine
      + does_low_fit_case_return_small_output
    ```

    File discipline:

    ```trace
    future_export_pack_rule :=
      target_zip_files <= 10
      prefer_consolidated_reader
      avoid_appendix_sprawl
      add_new_files_only_when_the_reader_needs_them
    ```
    """


def build_pack(repo_root: Path, out_dir: Path, stamp: str) -> tuple[Path, Path, str]:
    require_sources(repo_root)

    pack_name = f"ME_BOOK_v0_1_EXPORT_PACK_{stamp}"
    pack_dir = out_dir / pack_name
    if pack_dir.exists():
        shutil.rmtree(pack_dir)
    pack_dir.mkdir(parents=True)

    write_text(pack_dir / "01_START_HERE.md", start_here(pack_name))
    write_text(pack_dir / "02_ME_BOOK_v0_1_FULL_READER.md", build_full_reader(repo_root))
    write_text(pack_dir / "03_STATUS_LIMITS_AND_OPEN_WOUNDS.md", status_limits())

    for target, source in COPY_FILES.items():
        shutil.copyfile(repo_root / BOOK_DIR / source, pack_dir / target)

    write_text(pack_dir / "06_CASE_RECORD_TEMPLATE.md", case_record_template())
    write_text(pack_dir / "07_NEXT_PASS_PLAN.md", next_pass_plan())

    files = sorted(path for path in pack_dir.iterdir() if path.is_file())
    if len(files) > PACK_FILE_LIMIT:
        raise RuntimeError(f"Export pack has {len(files)} files; limit is {PACK_FILE_LIMIT}")

    zip_path = out_dir / f"{pack_name}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, arcname=f"{pack_name}/{path.name}")

    return pack_dir, zip_path, sha256_file(zip_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build ME book v0.1 compact export pack")
    parser.add_argument("--date", default=date.today().strftime("%Y_%m_%d"), help="Date stamp, e.g. 2026_06_27")
    parser.add_argument("--out-dir", default="dist", help="Output directory")
    args = parser.parse_args()

    repo_root = Path.cwd()
    out_dir = Path(args.out_dir)
    pack_dir, zip_path, digest = build_pack(repo_root, out_dir, args.date)

    print(f"Export pack directory: {pack_dir}")
    print(f"Export pack zip:       {zip_path}")
    print("File count:            7")
    print(f"SHA256:                {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
