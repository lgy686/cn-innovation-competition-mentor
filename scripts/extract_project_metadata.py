#!/usr/bin/env python3
"""Extract lightweight, deterministic metadata from common project files."""

from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main", "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def text_from_xml(data: bytes, namespace: str) -> str:
    root = ET.fromstring(data)
    return "".join(node.text or "" for node in root.findall(f".//{namespace}:t", NS)).strip()


def inspect_office(path: Path) -> dict:
    result = {"path": str(path), "kind": path.suffix.lower(), "readable": True}
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            if path.suffix.lower() == ".docx":
                document = archive.read("word/document.xml")
                result.update({"paragraph_text": text_from_xml(document, "w"), "paragraph_count": document.count(b"<w:p")})
            elif path.suffix.lower() == ".pptx":
                slides = sorted(name for name in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", name))
                texts = [text_from_xml(archive.read(name), "a") for name in slides]
                result.update({"slide_count": len(slides), "slide_text": texts})
            elif path.suffix.lower() == ".xlsx":
                sheets = sorted(name for name in names if re.fullmatch(r"xl/worksheets/sheet\d+\.xml", name))
                result.update({"worksheet_count": len(sheets)})
    except (OSError, KeyError, zipfile.BadZipFile, ET.ParseError) as exc:
        result.update({"readable": False, "error": str(exc)})
    return result


def inspect_text(path: Path) -> dict:
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
        headings = [line.strip().lstrip("#").strip() for line in content.splitlines() if re.match(r"^#{1,6}\s+", line)]
        return {"path": str(path), "kind": path.suffix.lower(), "readable": True, "character_count": len(content), "headings": headings}
    except OSError as exc:
        return {"path": str(path), "kind": path.suffix.lower(), "readable": False, "error": str(exc)}


def inspect_pdf(path: Path) -> dict:
    try:
        data = path.read_bytes()
        page_markers = len(re.findall(rb"/Type\s*/Page\b", data))
        return {"path": str(path), "kind": ".pdf", "readable": data.startswith(b"%PDF"), "bytes": len(data), "approx_page_count": page_markers or None}
    except OSError as exc:
        return {"path": str(path), "kind": ".pdf", "readable": False, "error": str(exc)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract lightweight metadata without changing input files.")
    parser.add_argument("path", help="A file or project directory")
    parser.add_argument("--output", help="JSON output file; default is stdout")
    args = parser.parse_args()
    target = Path(args.path).resolve()
    supported = {".docx", ".pptx", ".xlsx", ".pdf", ".md", ".txt"}
    files = [target] if target.is_file() else sorted(p for p in target.rglob("*") if p.suffix.lower() in supported)
    result = [inspect_office(file) if file.suffix.lower() in {".docx", ".pptx", ".xlsx"} else inspect_pdf(file) if file.suffix.lower() == ".pdf" else inspect_text(file) for file in files]
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
        print(f"Wrote metadata for {len(result)} file(s) to {Path(args.output).resolve()}")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
