#!/usr/bin/env python3
"""Validate a provider-neutral music-video plan."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def close(a: float, b: float, tolerance: float = 0.11) -> bool:
    return math.isclose(a, b, abs_tol=tolerance)


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read valid JSON: {exc}"]

    project = data.get("project") or {}
    scenes = data.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        return ["scenes must be a non-empty array"]

    try:
        project_duration = float(project["duration_seconds"])
    except (KeyError, TypeError, ValueError):
        return ["project.duration_seconds must be numeric"]

    indexes = [scene.get("scene_index") for scene in scenes]
    if indexes != list(range(len(scenes))):
        fail("scene_index values must be unique and sequential from 0", errors)

    output_paths: set[str] = set()
    previous_end = 0.0
    previous_opening: tuple[str | None, str | None] | None = None

    for position, scene in enumerate(scenes):
        label = f"scene {position}"
        try:
            start = float(scene["start_seconds"])
            end = float(scene["end_seconds"])
            duration = float(scene["duration"])
        except (KeyError, TypeError, ValueError):
            fail(f"{label}: start_seconds, end_seconds, and duration must be numeric", errors)
            continue

        if not close(start, previous_end):
            fail(f"{label}: timeline gap/overlap; starts at {start}, expected {previous_end}", errors)
        if end <= start or not close(duration, end - start):
            fail(f"{label}: duration must equal end_seconds - start_seconds", errors)
        if len(scenes) > 1 and not 9.9 <= duration <= 15.1:
            fail(f"{label}: duration {duration}s is outside the default 10–15s range", errors)
        previous_end = end

        for prompt_key in ("image_prompt", "video_prompt"):
            if not isinstance(scene.get(prompt_key), str) or not scene[prompt_key].strip():
                fail(f"{label}: {prompt_key} must be non-empty", errors)

        if scene.get("performance_mode") == "direct_lipsync":
            if not (scene.get("avatar_lipsync") or {}).get("eligible"):
                fail(f"{label}: direct_lipsync requires avatar_lipsync.eligible=true", errors)

        composition = scene.get("composition") or {}
        opening = (composition.get("framing"), composition.get("movement"))
        if previous_opening == opening and all(opening):
            fail(f"{label}: repeats the preceding opening framing and movement", errors)
        previous_opening = opening

        shots = scene.get("shots") or []
        if not isinstance(shots, list) or not shots:
            fail(f"{label}: shots must be a non-empty array", errors)
        else:
            shot_cursor = 0.0
            for shot_index, shot in enumerate(shots):
                try:
                    shot_start = float(shot["start_seconds"])
                    shot_end = float(shot["end_seconds"])
                except (KeyError, TypeError, ValueError):
                    fail(f"{label} shot {shot_index}: invalid timing", errors)
                    continue
                if not close(shot_start, shot_cursor):
                    fail(f"{label} shot {shot_index}: starts at {shot_start}, expected {shot_cursor}", errors)
                if shot_end <= shot_start:
                    fail(f"{label} shot {shot_index}: end must be after start", errors)
                shot_cursor = shot_end
            if not close(shot_cursor, duration):
                fail(f"{label}: internal shots end at {shot_cursor}, expected {duration}", errors)

        output_path = (scene.get("generation") or {}).get("output_path")
        if output_path:
            if output_path in output_paths:
                fail(f"{label}: duplicate generation.output_path {output_path}", errors)
            output_paths.add(output_path)

    if not close(previous_end, project_duration):
        fail(f"timeline ends at {previous_end}, expected project duration {project_duration}", errors)
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_plan.py <music-video-plan.json>", file=sys.stderr)
        return 2
    errors = validate(Path(sys.argv[1]))
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
