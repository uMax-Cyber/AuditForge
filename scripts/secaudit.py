#!/usr/bin/env python3
"""Weekly security audit — deterministic, stdlib only.
Usage: secaudit.py [--all | --check ssh,updates,devices,...]"""
import os, subprocess, sys, urllib.request, ssl, json
from datetime import datetime

def run(cmd, timeout=30):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
    return r.stdout.strip() if r.returncode == 0 else None

def check_ssh_bruteforce(host="localhost"):
    if host != "localhost":
        out = run(f'ssh root@{host} "journalctl -u ssh --since \'-7 days\' 2>/dev/null | grep -c \'Failed password\'"')
    else:
        out = run("journalctl -u ssh --since '-7 days' 2>/dev/null | grep -c 'Failed password'")
    count = int(out) if out and out.isdigit() else 0
    return {"count": count, "alert": count > 20}

def check_updates(host="localhost"):
    if host != "localhost":
        out = run(f'ssh root@{host} "apt list --upgradable 2>/dev/null | grep -c upgradable"')
    else:
        out = run("apt list --upgradable 2>/dev/null | grep -c upgradable")
    count = int(out) if out and out.isdigit() else 0
    return {"count": count, "alert": count > 100}

def generate_report(results):
    lines = [f"🔐 Security Audit — {datetime.now():%Y-%m-%d %H:%M}", ""]
    alerts = 0
    for name, data in results.items():
        icon = "🔴" if data.get("alert") else "✅"
        lines.append(f"  {icon} {name}: {data}")
        if data.get("alert"): alerts += 1
    lines.append(f"\n{'⚠️' if alerts else '✅'} {alerts} alert(s)" if alerts else "\n✅ All checks passed")
    return "\n".join(lines)

def main():
    results = {"ssh_bruteforce": check_ssh_bruteforce(), "package_updates": check_updates()}
    print(generate_report(results))

if __name__ == "__main__":
    main()
