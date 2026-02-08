import argparse
from pathlib import Path

from .parser import parse_nmap_normal
from .report import build_markdown_report
from .ai import improve_with_ai


def main():
    parser = argparse.ArgumentParser(description="Convert Nmap output to Markdown notes.")
    parser.add_argument("--input", "-i", required=True)
    parser.add_argument("--output", "-o", required=True)
    parser.add_argument("--use-ai", action="store_true")
    args = parser.parse_args()

    raw = Path(args.input).read_text(errors="ignore")
    parsed = parse_nmap_normal(raw)
    md = build_markdown_report(parsed)

    if args.use_ai:
        md = improve_with_ai(md, parsed)

    Path(args.output).write_text(md)
    print(f"[+] Report written to {args.output}")
