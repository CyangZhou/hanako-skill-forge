from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


DEFAULT_TERMS = [
    "> 状态：",
    "> 层级：",
    "> 作用：",
    "TODO",
    "FIXME",
    "占位脚本",
    "__pycache__",
]

REF_RE = re.compile(r"([A-Za-z0-9_./\-\u4e00-\u9fff]+\.md)")
ALLOWED_ACTIONS = {"module_index", "audit_refs", "audit_terms", "audit_skill"}


def ensure_utf8() -> None:
    stdout_reconfigure = getattr(sys.stdout, "reconfigure", None)
    stderr_reconfigure = getattr(sys.stderr, "reconfigure", None)
    if callable(stdout_reconfigure):
        stdout_reconfigure(encoding="utf-8")
    if callable(stderr_reconfigure):
        stderr_reconfigure(encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="hanako-skill-forge helper")
    parser.add_argument("--action", required=True)
    parser.add_argument("--root", default=".")
    parser.add_argument("--input")
    return parser.parse_args(argv)


def repo_root(root: str) -> Path:
    return Path(root).resolve()


def load_input(raw: str | None) -> dict:
    if not raw:
        return {}
    return json.loads(raw)


def md_files(base: Path) -> list[Path]:
    paths = [base / "SKILL.md"]
    for folder in ["guides", "modules"]:
        target = base / folder
        if target.exists():
            paths.extend(sorted(target.rglob("*.md")))
    return [path for path in paths if path.exists()]


def schema_file(base: Path) -> Path:
    return base / "schemas" / "actions_contracts.json"


def load_actions_contract(base: Path) -> dict[str, Any]:
    target = schema_file(base)
    return json.loads(target.read_text(encoding="utf-8"))


def action_names_from_contract(base: Path) -> set[str]:
    payload = load_actions_contract(base)
    direct_actions = payload.get("actions")
    if isinstance(direct_actions, dict) and direct_actions:
        return set(direct_actions.keys())

    schema_actions = (
        payload.get("properties", {})
        .get("actions", {})
        .get("properties", {})
    )
    if isinstance(schema_actions, dict):
        return set(schema_actions.keys())
    return set()


def audit_action_contract(base: Path) -> dict:
    schema_path = schema_file(base)
    if not schema_path.exists():
        return {
            "ok": False,
            "missing_schema": True,
            "schema_path": str(schema_path.relative_to(base)),
            "declared_actions": [],
            "script_actions": sorted(ALLOWED_ACTIONS),
            "missing_in_schema": sorted(ALLOWED_ACTIONS),
            "extra_in_schema": [],
        }

    declared = action_names_from_contract(base)
    missing_in_schema = sorted(ALLOWED_ACTIONS - declared)
    extra_in_schema = sorted(declared - ALLOWED_ACTIONS)
    return {
        "ok": not missing_in_schema and not extra_in_schema,
        "missing_schema": False,
        "schema_path": str(schema_path.relative_to(base)),
        "declared_actions": sorted(declared),
        "script_actions": sorted(ALLOWED_ACTIONS),
        "missing_in_schema": missing_in_schema,
        "extra_in_schema": extra_in_schema,
    }


def scan_refs(base: Path) -> dict:
    checked = 0
    missing: list[dict[str, str]] = []
    for file_path in md_files(base):
        text = file_path.read_text(encoding="utf-8")
        for match in REF_RE.findall(text):
            if match.startswith("http") or "*" in match or "<" in match:
                continue
            if not match.startswith(("guides/", "modules/", "SKILL.md")):
                continue
            checked += 1
            target = base / match
            if not target.exists():
                missing.append(
                    {"file": str(file_path.relative_to(base)), "missing": match}
                )
    return {"checked_refs": checked, "missing_refs": missing}


def scan_terms(base: Path, terms: list[str], exclude: list[str] | None = None) -> dict:
    hits: list[dict[str, object]] = []
    excluded = {item.replace("/", "\\") for item in (exclude or [])}
    scan_paths = md_files(base)
    scripts_dir = base / "scripts"
    if scripts_dir.exists():
        scan_paths.extend(sorted(scripts_dir.rglob("*.py")))
    for file_path in scan_paths:
        relative = str(file_path.relative_to(base))
        if relative.replace("/", "\\") in excluded:
            continue
        text = file_path.read_text(encoding="utf-8")
        for term in terms:
            line_no = 0
            for idx, line in enumerate(text.splitlines(), start=1):
                if term in line:
                    line_no = idx
                    hits.append(
                        {
                            "file": relative,
                            "term": term,
                            "line": line_no,
                        }
                    )
    return {"terms": terms, "hits": hits}


def module_index() -> dict:
    modules = [
        {"name": "route", "role": "任务卡与总控路由"},
        {"name": "research", "role": "对标与能力注入"},
        {"name": "build", "role": "架构与落地"},
        {"name": "maintenance", "role": "维护与巡检"},
        {"name": "extension", "role": "扩展治理"},
        {"name": "recovery", "role": "自愈与收敛"},
        {"name": "review", "role": "验收与发布"},
        {"name": "templates", "role": "结构化模板"},
    ]
    return {"ok": True, "modules": modules}


def audit_skill(base: Path) -> dict:
    refs = scan_refs(base)
    terms = scan_terms(base, DEFAULT_TERMS, exclude=["scripts/main.py"])
    contract = audit_action_contract(base)
    return {
        "ok": len(refs["missing_refs"]) == 0 and len(terms["hits"]) == 0 and contract["ok"],
        "docs": len(md_files(base)),
        "checked_refs": refs["checked_refs"],
        "missing_refs": refs["missing_refs"],
        "term_hits": terms["hits"],
        "action_contract": contract,
    }


def emit(payload: dict) -> int:
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    ensure_utf8()
    args = parse_args(argv)
    base = repo_root(args.root)
    input_data = load_input(args.input)
    action = args.action.strip()

    if action not in ALLOWED_ACTIONS:
        return emit(
            {
                "ok": False,
                "error": f"unknown action: {action}",
                "allowed_actions": sorted(ALLOWED_ACTIONS),
            }
        )

    if action == "module_index":
        return emit(module_index())
    if action == "audit_refs":
        result = scan_refs(base)
        return emit({"ok": len(result["missing_refs"]) == 0, **result})
    if action == "audit_terms":
        terms = input_data.get("terms") or DEFAULT_TERMS
        exclude = input_data.get("exclude") or ["scripts/main.py"]
        result = scan_terms(base, list(terms), list(exclude))
        return emit({"ok": len(result["hits"]) == 0, **result})
    if action == "audit_skill":
        return emit(audit_skill(base))

    return emit({"ok": False, "error": f"unhandled action: {action}"})


if __name__ == "__main__":
    raise SystemExit(main())
