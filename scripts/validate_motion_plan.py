#!/usr/bin/env python3
"""Validate a structured image-to-video motion plan.

The validator checks schema shape and high-signal cinematography risks. It does
not replace visual review or provider schema validation.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


LEVELS = {"low", "medium", "high"}
TRAVEL = {"minimal", "small", "medium", "large"}
SPEEDS = {"very-slow", "slow", "medium", "fast"}
PRODUCT_CLASSES = {
    "website-ui",
    "software-interface",
    "consumer-electronics",
    "industrial-product",
    "food-beverage",
    "beauty-packaging",
    "fashion-accessory",
    "vehicle",
    "architecture-interior",
    "person-character",
    "artwork-graphic",
    "environment",
    "other",
    "unknown",
}
SUBJECT_TYPES = {
    "product",
    "portrait",
    "character",
    "landscape",
    "architecture",
    "food",
    "artwork",
    "other",
}
MOVES = {
    "",
    "static",
    "push-in",
    "pull-out",
    "dolly-in",
    "dolly-out",
    "pan-left",
    "pan-right",
    "tilt-up",
    "tilt-down",
    "truck-left",
    "truck-right",
    "pedestal-up",
    "pedestal-down",
    "crane-up",
    "crane-down",
    "orbit-left",
    "orbit-right",
    "arc-left",
    "arc-right",
    "tracking",
    "follow",
    "lead",
    "handheld",
    "steadicam",
    "whip-pan-left",
    "whip-pan-right",
    "roll-left",
    "roll-right",
    "zoom-in",
    "zoom-out",
    "crash-zoom-in",
    "crash-zoom-out",
    "dolly-zoom-in",
    "dolly-zoom-out",
    "drone-push",
    "aerial-rise",
    "macro-glide",
    "rack-focus",
}
HIGH_RECONSTRUCTION_MOVES = {
    "orbit-left",
    "orbit-right",
    "crane-up",
    "crane-down",
    "dolly-zoom-in",
    "dolly-zoom-out",
    "drone-push",
    "aerial-rise",
}
TRANSLATION_MOVES = {
    "push-in",
    "pull-out",
    "dolly-in",
    "dolly-out",
    "truck-left",
    "truck-right",
    "pedestal-up",
    "pedestal-down",
    "crane-up",
    "crane-down",
    "orbit-left",
    "orbit-right",
    "arc-left",
    "arc-right",
    "tracking",
    "follow",
    "lead",
    "steadicam",
    "drone-push",
    "aerial-rise",
    "macro-glide",
}


def load_plan(path: str) -> dict[str, Any]:
    if path == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(path).read_text(encoding="utf-8")
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("top-level JSON value must be an object")
    return data


def validate(plan: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for section in ("classification", "source", "direction", "preserve", "prompt"):
        if section not in plan:
            errors.append(f"missing required top-level field: {section}")

    classification = plan.get("classification", {})
    source = plan.get("source", {})
    direction = plan.get("direction", {})
    prompt = plan.get("prompt", {})
    preserve = plan.get("preserve", [])

    if not isinstance(classification, dict):
        errors.append("classification must be an object")
        classification = {}
    if not isinstance(source, dict):
        errors.append("source must be an object")
        source = {}
    if not isinstance(direction, dict):
        errors.append("direction must be an object")
        direction = {}
    if not isinstance(prompt, dict):
        errors.append("prompt must be an object")
        prompt = {}
    if not isinstance(preserve, list) or not any(str(item).strip() for item in preserve):
        errors.append("preserve must contain at least one non-empty constraint")

    product_class = classification.get("product_class")
    if product_class not in PRODUCT_CLASSES:
        errors.append(f"classification.product_class must be one of {sorted(PRODUCT_CLASSES)}")
    if classification.get("confidence") not in LEVELS:
        errors.append(f"classification.confidence must be one of {sorted(LEVELS)}")
    evidence = classification.get("evidence", [])
    if not isinstance(evidence, list) or not any(str(item).strip() for item in evidence):
        errors.append("classification.evidence must contain at least one non-empty item")
    required_assets = classification.get("required_assets", [])
    if not isinstance(required_assets, list) or not any(
        str(item).strip() for item in required_assets
    ):
        errors.append("classification.required_assets must contain at least one non-empty item")
    if not str(classification.get("proposed_workflow", "")).strip():
        errors.append("classification.proposed_workflow must be non-empty")
    if product_class == "unknown":
        errors.append("classification.product_class cannot remain unknown before motion planning")
    if classification.get("user_confirmed") is not True:
        errors.append("classification.user_confirmed must be true before motion planning or generation")

    subject_type = source.get("subject_type")
    if subject_type not in SUBJECT_TYPES:
        errors.append(f"source.subject_type must be one of {sorted(SUBJECT_TYPES)}")

    for key in ("depth_confidence", "edge_reserve", "occlusion_risk", "geometry_risk"):
        if source.get(key) not in LEVELS:
            errors.append(f"source.{key} must be one of {sorted(LEVELS)}")

    safe_movement = source.get("maximum_safe_movement")
    if safe_movement not in TRAVEL:
        errors.append(f"source.maximum_safe_movement must be one of {sorted(TRAVEL)}")

    primary = str(direction.get("primary_move", "")).strip()
    secondary = str(direction.get("secondary_move", "")).strip()
    if primary not in MOVES or not primary:
        errors.append("direction.primary_move is missing or unsupported")
    if secondary not in MOVES:
        errors.append("direction.secondary_move is unsupported")
    if secondary == "static":
        errors.append("direction.secondary_move cannot be static")
    if primary == "static" and secondary:
        errors.append("a static primary move cannot have a secondary camera move")
    if primary and secondary and primary in TRANSLATION_MOVES and secondary in TRANSLATION_MOVES:
        warnings.append("two translating camera moves compete; keep one dominant move")

    travel = direction.get("travel")
    if travel not in TRAVEL:
        errors.append(f"direction.travel must be one of {sorted(TRAVEL)}")
    elif primary == "static" and travel != "minimal":
        errors.append("a static primary move requires minimal travel")
    speed = direction.get("speed")
    if speed not in SPEEDS:
        errors.append(f"direction.speed must be one of {sorted(SPEEDS)}")

    duration = direction.get("duration_seconds")
    if not isinstance(duration, (int, float)) or isinstance(duration, bool):
        errors.append("direction.duration_seconds must be numeric")
    else:
        if duration <= 0:
            errors.append("direction.duration_seconds must be greater than zero")
        elif duration > 15:
            warnings.append("duration exceeds the common 15-second I2V range; verify provider support")
        elif duration > 8:
            warnings.append("long I2V shots often drift; consider chained shorter shots")
        elif duration < 3 and (primary in TRANSLATION_MOVES or secondary):
            warnings.append("the requested camera development may be too dense for a sub-3-second shot")

    if direction.get("single_take") is not True:
        warnings.append("default professional I2V direction is one continuous shot; verify multi-shot support")

    orbit = direction.get("orbit_degrees", 0)
    if not isinstance(orbit, (int, float)) or isinstance(orbit, bool) or orbit < 0:
        errors.append("direction.orbit_degrees must be a non-negative number")
        orbit = 0
    if primary.startswith("orbit") or primary.startswith("arc"):
        if orbit == 0:
            warnings.append("orbit or arc move should declare a bounded orbit_degrees value")
        if orbit > 90:
            errors.append("orbit above 90 degrees from one still requires additional views or explicit 3D support")
        elif orbit > 45:
            warnings.append("orbit above 45 degrees has high unseen-surface risk")
    elif orbit:
        warnings.append("orbit_degrees is set but the primary move is not orbit or arc")

    depth = source.get("depth_confidence")
    edge = source.get("edge_reserve")
    geometry = source.get("geometry_risk")
    if depth == "low" and primary in HIGH_RECONSTRUCTION_MOVES:
        errors.append("high-reconstruction camera move conflicts with low depth confidence")
    if edge == "low" and travel == "large" and primary in TRANSLATION_MOVES:
        errors.append("large camera translation conflicts with low edge reserve")
    if safe_movement in {"minimal", "small"} and travel in {"medium", "large"}:
        errors.append("requested travel exceeds source.maximum_safe_movement")
    if subject_type == "product" and geometry == "high" and orbit > 25:
        warnings.append("rigid product geometry and labels are at risk above a small inspection arc")
    if subject_type in {"portrait", "character"} and orbit > 30:
        warnings.append("large portrait orbit may invent face profile, hair, ears, and body geometry")
    if product_class in {"website-ui", "software-interface"} and (
        primary in HIGH_RECONSTRUCTION_MOVES
        or primary.startswith("arc")
        or travel in {"medium", "large"}
    ):
        warnings.append(
            "interface work should normally use deterministic pan, tilt, zoom, scroll, or compositing instead of 3D reconstruction"
        )

    positive = str(prompt.get("positive", "")).strip()
    if not positive:
        errors.append("prompt.positive must contain a model-ready motion prompt")
    else:
        if len(positive) > 1400:
            warnings.append("positive prompt is long; remove image restatement and competing instructions")
        lowered = positive.lower()
        negative_phrases = ("don't ", "do not ", "no camera", "without changing")
        if any(phrase in lowered for phrase in negative_phrases):
            warnings.append("positive prompt contains negative phrasing; rewrite as direct desired behavior")

    generation = plan.get("generation", {})
    if generation and not isinstance(generation, dict):
        errors.append("generation must be an object when provided")
    elif isinstance(generation, dict):
        negative = str(prompt.get("negative", "")).strip()
        if negative and generation.get("supports_negative_prompt") is not True:
            warnings.append("negative prompt is populated without confirmed provider support")

    fallback = plan.get("fallback", {})
    if fallback and not isinstance(fallback, dict):
        errors.append("fallback must be an object when provided")
        fallback = {}
    if primary in HIGH_RECONSTRUCTION_MOVES and not str(fallback.get("move", "")).strip():
        warnings.append("high-risk motion should include a safer fallback move")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", help="Path to motion-plan JSON, or - for stdin")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable results")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return a failing exit code when warnings are present",
    )
    args = parser.parse_args()

    try:
        plan = load_plan(args.plan)
        errors, warnings = validate(plan)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        errors, warnings = [str(exc)], []

    valid = not errors and (not args.strict or not warnings)
    if args.json:
        print(json.dumps({"valid": valid, "errors": errors, "warnings": warnings}, indent=2))
    else:
        for item in errors:
            print(f"ERROR: {item}")
        for item in warnings:
            print(f"WARNING: {item}")
        if valid:
            print("OK: motion plan passed validation")

    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
