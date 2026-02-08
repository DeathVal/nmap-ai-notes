![Python](https://img.shields.io/badge/python-3.9+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)


# nmap-ai-notes

Turn Nmap output into a clean Markdown summary for reporting.

## What it does
- Parses Nmap normal output (`-oN`)
- Extracts open ports/services
- Produces a Markdown report
- Optional: uses an LLM to improve the narrative

## What it does NOT do
- It does not scan targets
- It does not exploit anything

## Ethical use
This tool is intended for authorized security testing, education, and defensive reporting only.

## Install
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
