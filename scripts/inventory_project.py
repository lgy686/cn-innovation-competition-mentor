#!/usr/bin/env python3
"""Create a deterministic inventory of a competition-project workspace."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


IGNORE_DIRS = {".git", ".svn", "__pycache__", "node_modules", ".idea", ".vscode"}
KEYWORDS = {
    "competition": ("赛事", "比赛", "赛道", "组委会", "评分", "评审", "通知", "申报", "答辩", "模板", "揭榜"),
    "project_source": ("项目", "计划书", "商业", "技术", "产品", "市场", "论文", "方案", "路演"),
    "evidence": ("专利", "软著", "合同", "协议", "证书", "检测", "查新", "证明", "发票", "财务", "报道", "截图", "照片"),
    "technical_reference": ("参考文献", "核心技术文献", "技术文献", "literature", "reference", "paper"),
    "case_or_template": ("案例", "获奖", "优秀", "模板", "样例"),
}


def classify(path: Path) -> str:
    text = " ".join(part.lower() for part in path.parts)
    matched = [label for label, words in KEYWORDS.items() if any(word in text for word in words)]
    return ";".join(matched) if matched else "unclassified"


def should_skip(path: Path) -> bool:
    return any(part in IGNORE_DIRS or part.startswith("~$") for part in path.parts)


def main() -> int:
    parser = argparse.ArgumentParser(description="Inventory files without modifying the project.")
    parser.add_argument("root", nargs="?", default=".", help="Project root; defaults to current directory")
    parser.add_argument("--output", help="CSV output path; defaults to <root>/project_inventory.csv")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    output = Path(args.output).resolve() if args.output else root / "project_inventory.csv"
    rows = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or should_skip(path.relative_to(root)) or path.resolve() == output:
            continue
        stat = path.stat()
        rows.append({
            "relative_path": path.relative_to(root).as_posix(),
            "extension": path.suffix.lower() or "[none]",
            "bytes": stat.st_size,
            "modified_utc": __import__("datetime").datetime.fromtimestamp(stat.st_mtime, __import__("datetime").timezone.utc).isoformat(),
            "semantic_categories": classify(path.relative_to(root)),
        })
    with output.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]) if rows else ["relative_path", "extension", "bytes", "modified_utc", "semantic_categories"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} file(s) to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
