#!/usr/bin/env python3
"""Structure and frontmatter checks for the more-ambitious repository.

Usage: python3 scripts/validate.py [repo_root]
Exits non-zero on any error.
"""
import json
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
errors = []

def err(msg):
    errors.append(msg)

# --- Skills -----------------------------------------------------------------
skills_dir = root / "skills"
skills = sorted(p for p in skills_dir.iterdir() if p.is_dir()) if skills_dir.is_dir() else []
if not skills:
    err("no skills found under skills/")

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
for skill in skills:
    md = skill / "SKILL.md"
    if not md.is_file():
        err(f"{skill.name}: SKILL.md missing")
        continue
    text = md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        err(f"{skill.name}: SKILL.md has no YAML frontmatter")
        continue
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not name:
        err(f"{skill.name}: frontmatter 'name' missing")
    elif name != skill.name:
        err(f"{skill.name}: frontmatter name '{name}' must match folder name")
    elif not NAME_RE.match(name) or len(name) > 64:
        err(f"{skill.name}: name must be kebab-case, max 64 chars")
    if not desc:
        err(f"{skill.name}: frontmatter 'description' missing")
    elif len(desc) > 1024:
        err(f"{skill.name}: description longer than 1024 chars ({len(desc)})")
    elif "<" in desc or ">" in desc:
        err(f"{skill.name}: description must not contain angle brackets")
    body_lines = text[m.end():].count("\n")
    if body_lines > 500:
        err(f"{skill.name}: SKILL.md body is {body_lines} lines; keep it under 500")
    # Hygiene: no absolute local paths or obvious secrets.
    for pat, label in [
        (r"/(Users|home|root)/[A-Za-z0-9_.-]+/", "absolute local path"),
        (r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*\S{12,}", "possible secret"),
        (r"sk-[A-Za-z0-9]{20,}", "possible API key"),
    ]:
        if re.search(pat, text):
            err(f"{skill.name}: {label} found in SKILL.md")

# --- Plugin manifests ---------------------------------------------------------
def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        err(f"{path.relative_to(root)} missing")
    except json.JSONDecodeError as e:
        err(f"{path.relative_to(root)} is not valid JSON: {e}")
    return None

plugin = load(root / ".claude-plugin" / "plugin.json")
market = load(root / ".claude-plugin" / "marketplace.json")
if plugin and market:
    names = [p.get("name") for p in market.get("plugins", [])]
    if plugin.get("name") not in names:
        err("plugin.json name is not listed in marketplace.json")
    for p in market.get("plugins", []):
        if p.get("version") and p["version"] != plugin.get("version"):
            err(f"version mismatch: plugin.json {plugin.get('version')} vs marketplace {p['version']}")

# --- Evals --------------------------------------------------------------------
ev = load(root / "evals" / "triggers.json")
if ev:
    for key in ("should_trigger", "should_not_trigger"):
        if len(ev.get(key, [])) < 5:
            err(f"evals/triggers.json: '{key}' needs at least 5 cases")

for f in ("README.md", "LICENSE", "CHANGELOG.md"):
    if not (root / f).is_file():
        err(f"{f} missing")

if errors:
    print("Validation failed:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"OK: {len(skills)} skill(s), manifests and evals valid.")
