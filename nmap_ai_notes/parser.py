import re

PORT_LINE = re.compile(r"^(\d+)\/(\w+)\s+open\s+(\S+)(?:\s+(.*))?$")

def parse_nmap_normal(text):
    target = "unknown"
    open_ports = []

    for line in text.splitlines():
        line = line.strip()

        if line.lower().startswith("nmap scan report for"):
            target = line.split("for", 1)[1].strip()

        match = PORT_LINE.match(line)
        if match:
            port, proto, service, extra = match.groups()
            open_ports.append({
                "port": int(port),
                "proto": proto,
                "service": service,
                "extra": extra or ""
            })

    return {
        "target": target,
        "open_ports": open_ports
    }
