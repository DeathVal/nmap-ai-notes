from datetime import datetime

def build_markdown_report(parsed):
    lines = []
    lines.append("# Nmap Summary Report")
    lines.append("")
    lines.append(f"- Target: {parsed['target']}")
    lines.append(f"- Generated: {datetime.utcnow()} UTC")
    lines.append("")
    lines.append("## Open Ports")
    lines.append("")

    if not parsed["open_ports"]:
        lines.append("No open ports found.")
    else:
        for p in parsed["open_ports"]:
            lines.append(f"- {p['port']}/{p['proto']} → {p['service']} {p['extra']}")

    lines.append("")
    lines.append("## Notes")
    lines.append("This report was generated automatically. Validate findings manually.")
    return "\n".join(lines)
