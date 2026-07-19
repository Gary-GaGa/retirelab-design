#!/usr/bin/env python3
"""audit_tokens.py — deterministic drift detection between DESIGN_SPEC and source.

Parses the machine-readable TOKENS block in a DESIGN_SPEC, scans source files
for hex colors and font-family declarations, and reports any value not in spec.

Exit codes:
  0  clean
  1  violations found (report on stdout)         — default mode
  2  violations found (report on stderr)         — --hook mode, for Claude Code
                                                    hooks that feed stderr back
                                                    to the model on exit code 2

Usage:
  python audit_tokens.py --spec design/DESIGN_SPEC.md --src src/
  python audit_tokens.py --spec design/DESIGN_SPEC.md --src src/ --hook
  python audit_tokens.py --spec ... --src ... --files a.css b.tsx   # only these
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SCAN_EXT = {".css", ".scss", ".sass", ".less", ".html", ".htm", ".vue",
            ".jsx", ".tsx", ".js", ".ts", ".svelte"}
SKIP_DIRS = {"node_modules", "dist", "build", ".next", ".git", "coverage",
             "vendor", "out", "archive"}

TOKENS_RE = re.compile(r"TOKENS:BEGIN(.*?)TOKENS:END", re.S)
HEX_RE = re.compile(r"#(?:[0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})\b")
FONT_DECL_RE = re.compile(r"font-?family\s*:\s*([^;}\n]+)", re.I)  # CSS + RN camelCase
QUOTED_FONT_RE = re.compile(r"[\"']([^\"']+)[\"']")

GENERIC_FONTS = {"serif", "sans-serif", "monospace", "system-ui", "ui-serif",
                 "ui-sans-serif", "ui-monospace", "cursive", "fantasy",
                 "inherit", "initial", "unset", "var"}


def norm_hex(h: str) -> str:
    h = h.lower().lstrip("#")
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    if len(h) == 8:          # drop alpha channel for comparison
        h = h[:6]
    return "#" + h


def parse_spec(spec_path: Path):
    text = spec_path.read_text(encoding="utf-8", errors="replace")
    m = TOKENS_RE.search(text)
    if not m:
        sys.stderr.write(f"[audit] no TOKENS block in {spec_path}\n")
        sys.exit(3)
    block = m.group(1)
    colors, fonts, extra = set(), set(), set()
    for line in block.splitlines():
        line = line.strip()
        if line.lower().startswith("colors:"):
            colors |= {norm_hex(h) for h in HEX_RE.findall(line)}
        elif line.lower().startswith("fonts:"):
            fonts |= {f.strip().lower() for f in QUOTED_FONT_RE.findall(line)}
        elif line.lower().startswith("allow-extra:"):
            extra |= {t.strip().lower()
                      for t in line.split(":", 1)[1].split(",") if t.strip()}
    return colors, fonts, extra


def iter_files(src: Path, only: list[str] | None):
    if only:
        for f in only:
            p = Path(f)
            if p.suffix.lower() in SCAN_EXT and p.is_file():
                yield p
        return
    for p in sorted(src.rglob("*")):
        if p.is_file() and p.suffix.lower() in SCAN_EXT \
                and not (SKIP_DIRS & set(p.parts)):
            yield p


def audit(spec: Path, src: Path, only: list[str] | None):
    colors, fonts, extra = parse_spec(spec)
    violations = []
    for f in iter_files(src, only):
        try:
            lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for i, line in enumerate(lines, 1):
            # single predictable rule: any hex not in spec colors/extra
            for h in HEX_RE.findall(line):
                nh = norm_hex(h)
                if nh not in colors and nh.lstrip("#") not in extra:
                    violations.append((str(f), i, "color", h.strip()))
            for decl in FONT_DECL_RE.findall(line):
                names = QUOTED_FONT_RE.findall(decl)
                if not names:  # unquoted stacks: split on commas
                    names = [t.strip() for t in decl.split(",")]
                for name in names:
                    n = name.strip().strip("\"'").lower()
                    if not n or n in GENERIC_FONTS or n.startswith("var("):
                        continue
                    if n not in fonts and n not in extra:
                        violations.append((str(f), i, "font", name.strip()))
    # dedupe while preserving order
    seen, uniq = set(), []
    for v in violations:
        if v not in seen:
            seen.add(v)
            uniq.append(v)
    return uniq, colors, fonts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--src", required=True)
    ap.add_argument("--files", nargs="*", default=None,
                    help="restrict scan to these files (e.g. from hook env)")
    ap.add_argument("--hook", action="store_true",
                    help="report to stderr and exit 2 on violations")
    args = ap.parse_args()

    uniq, colors, fonts = audit(Path(args.spec), Path(args.src), args.files)

    if not uniq:
        print(f"[audit] OK — {len(colors)} colors, {len(fonts)} fonts in spec; "
              f"no off-token values found.")
        sys.exit(0)

    out = sys.stderr if args.hook else sys.stdout
    out.write(f"[audit] {len(uniq)} off-token value(s) — rubric T1-10:\n")
    for path, ln, kind, val in uniq:
        out.write(f"  {path}:{ln}  [{kind}]  {val}  → not in DESIGN_SPEC tokens\n")
    out.write("[audit] fix: use spec tokens, or update DESIGN_SPEC via "
              "design-director (outer-loop gated).\n")
    sys.exit(2 if args.hook else 1)


if __name__ == "__main__":
    main()
