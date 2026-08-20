#!/usr/bin/env python3
"""Report structural issues in DOCX/PPTX files without modifying them."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main", "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def xml_text(data: bytes, prefix: str) -> str:
    root = ET.fromstring(data)
    return "".join(node.text or "" for node in root.findall(f".//{prefix}:t", NS))


def validate_docx(path: Path) -> list[str]:
    issues: list[str] = []
    with zipfile.ZipFile(path) as archive:
        doc = archive.read("word/document.xml")
        root = ET.fromstring(doc)
        style_ids = []
        captions = []
        for paragraph in root.findall(".//w:p", NS):
            text = "".join(node.text or "" for node in paragraph.findall(".//w:t", NS)).strip()
            style = paragraph.find("./w:pPr/w:pStyle", NS)
            if style is not None:
                style_ids.append(style.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val", ""))
            if re.match(r"^(图|表)\s*\d+[-.－]\d+", text):
                captions.append(text)
        if not style_ids:
            issues.append("未检测到段落样式；请确认是否使用了 Word 样式系统。")
        figure_numbers = [re.match(r"^图\s*(\d+[-.－]\d+)", item).group(1) for item in captions if item.startswith("图")]
        table_numbers = [re.match(r"^表\s*(\d+[-.－]\d+)", item).group(1) for item in captions if item.startswith("表")]
        if len(figure_numbers) != len(set(figure_numbers)):
            issues.append("存在重复图号。")
        if len(table_numbers) != len(set(table_numbers)):
            issues.append("存在重复表号。")
    return issues


def validate_pptx(path: Path) -> list[str]:
    issues: list[str] = []
    with zipfile.ZipFile(path) as archive:
        slides = sorted(name for name in archive.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", name))
        if not slides:
            issues.append("未发现幻灯片 XML。")
        for index, slide in enumerate(slides, 1):
            if not xml_text(archive.read(slide), "a").strip():
                issues.append(f"第 {index} 页未检测到可提取文字；请人工确认是否为预期的纯视觉页面。")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Check DOCX/PPTX structural invariants without modifying files.")
    parser.add_argument("target", help="A .docx/.pptx file or directory")
    args = parser.parse_args()
    target = Path(args.target).resolve()
    files = [target] if target.is_file() else sorted(p for p in target.rglob("*") if p.suffix.lower() in {".docx", ".pptx"})
    if not files:
        print("No DOCX/PPTX files found.")
        return 0
    any_issue = False
    for file in files:
        try:
            issues = validate_docx(file) if file.suffix.lower() == ".docx" else validate_pptx(file)
        except (OSError, KeyError, zipfile.BadZipFile, ET.ParseError) as exc:
            issues = [f"无法解析：{exc}"]
        print(file)
        if issues:
            any_issue = True
            for issue in issues:
                print(f"  WARNING: {issue}")
        else:
            print("  OK: 未发现本脚本可确定的结构问题。")
    return 1 if any_issue else 0


if __name__ == "__main__":
    raise SystemExit(main())
