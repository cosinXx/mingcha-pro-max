#!/usr/bin/env python3
"""按固定顺序拼接 parts/ 分片为 output/report.md，并按正文首次出现顺序校正引用编号。

用法:
    python3 scripts/assemble_report.py [--parts DIR] [--output FILE]

规则:
- parts/ 下按文件名排序(01-*, 02-* ...)拼接。
- 正文中所有句末引用 [n] 按首次出现顺序重编号为 [1]...[N]。
- 文末"参考文献/References"章节中的编号条目按新顺序重排。
"""
import argparse
import re
from pathlib import Path

REF_HEADINGS = re.compile(r"^#{1,4}\s*(参考文献|References|参考来源)", re.MULTILINE)
CITE_RE = re.compile(r"\[(\d+)\]")


def split_refs(text: str) -> tuple[str, str]:
    """将正文与参考文献章节分开。返回 (正文, 参考文献部分或空串)。"""
    m = REF_HEADINGS.search(text)
    if not m:
        return text, ""
    return text[: m.start()], text[m.start():]


def renumber(body: str) -> tuple[str, dict[int, int]]:
    """按首次出现顺序重编号引用，返回 (新正文, 旧->新映射)。"""
    mapping: dict[int, int] = {}
    counter = 0

    def repl(m: re.Match) -> str:
        nonlocal counter
        old = int(m.group(1))
        if old not in mapping:
            counter += 1
            mapping[old] = counter
        return f"[{mapping[old]}]"

    return CITE_RE.sub(repl, body), mapping


def reorder_refs(refs: str, mapping: dict[int, int]) -> str:
    """参考文献章节内按 [n] 起始的条目重排为新编号顺序。"""
    lines = refs.splitlines(keepends=True)
    header = []
    items: list[tuple[int, str]] = []
    tail: list[str] = []
    cur: list[str] = []
    cur_num: int | None = None

    for line in lines:
        m = re.match(r"^\s*\[(\d+)\]\s+", line)
        if m:
            if cur_num is not None:
                items.append((cur_num, "".join(cur)))
            cur_num = int(m.group(1))
            cur = [line]
        elif cur_num is None:
            header.append(line)
        else:
            cur.append(line)
    if cur_num is not None:
        items.append((cur_num, "".join(cur)))

    # 只重排正文中出现的编号，未出现的保持原顺序追加
    seen = {v: k for k, v in mapping.items()}
    ordered = []
    for new, old in sorted(seen.items()):
        match = next((it for it in items if it[0] == old), None)
        if match:
            ordered.append((new, match[1]))
    used = {old for old in seen.values()}
    for num, text in items:
        if num not in used:
            ordered.append((num, text))

    if not ordered:
        return "".join(header + [t for _, t in items])
    out = "".join(header)
    for new, text in ordered:
        out += re.sub(r"^(\s*)\[\d+\]", rf"\1[{new}]", text, count=1)
    out += "".join(tail)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="拼接分片并校正引用编号")
    ap.add_argument("--parts", default="parts", help="分片目录，默认 parts")
    ap.add_argument("--output", default="output/report.md", help="输出文件，默认 output/report.md")
    args = ap.parse_args()

    parts_dir = Path(args.parts)
    files = sorted(parts_dir.glob("*.md"))
    if not files:
        raise SystemExit(f"错误: {parts_dir} 下没有 .md 分片")

    body, refs = split_refs("".join(f.read_text(encoding="utf-8") for f in files))
    new_body, mapping = renumber(body)
    new_refs = reorder_refs(refs, mapping) if refs else ""
    out = new_body + "\n" + new_refs
    out = re.sub(r"\n{3,}", "\n\n", out).strip() + "\n"

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(out, encoding="utf-8")
    print(f"✅ 已拼接 {len(files)} 个分片 -> {args.output}，共重编号 {len(mapping)} 处引用")


if __name__ == "__main__":
    main()
