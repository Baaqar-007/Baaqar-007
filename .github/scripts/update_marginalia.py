#!/usr/bin/env python3
"""
Writes a quiet, factual activity note into README.md between the
START_SECTION:activity / END_SECTION:activity markers.

Deliberately avoids vanity metrics (stars, followers, commit counts).
Reports: what's currently being touched, and when it last was.

Uses only the standard library and the GITHUB_TOKEN GitHub Actions
provides automatically, so no secrets need to be configured by hand.
If the API is unreachable or returns something unexpected, the script
exits quietly and leaves README.md untouched — a stale section is
preferable to a broken workflow run.
"""

import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone

USERNAME = "Baaqar-007"
README_PATH = "README.md"
START = "<!--START_SECTION:activity-->"
END = "<!--END_SECTION:activity-->"


def api_get(path):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN', '')}",
            "User-Agent": USERNAME,
        },
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode())


def relative_time(iso_ts):
    then = datetime.fromisoformat(iso_ts.replace("Z", "+00:00"))
    delta = datetime.now(timezone.utc) - then
    days = delta.days
    if days <= 0:
        return "today"
    if days == 1:
        return "yesterday"
    if days < 14:
        return f"{days} days ago"
    weeks = days // 7
    if weeks < 8:
        return f"{weeks} weeks ago"
    return f"{days // 30} months ago"


def build_block():
    repos = api_get(f"/users/{USERNAME}/repos?sort=pushed&direction=desc&per_page=5")
    repos = [r for r in repos if not r.get("fork")]
    if not repos:
        raise ValueError("no repositories returned")

    top = repos[:3]
    languages = [r["language"] for r in top if r.get("language")]
    seen = []
    for lang in languages:
        if lang not in seen:
            seen.append(lang)

    fence = ["```"]
    for r in top:
        date = r["pushed_at"][:10]
        name = r["name"]
        fence.append(f"{date}  {name:<28} touched")
    if seen:
        fence.append("")
        fence.append(f"primary language, recent pushes — {seen[0]}")
    fence.append("```")

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    fence.append("")
    fence.append(f"checked {stamp}")

    return "\n".join(fence)


def main():
    try:
        block = build_block()
    except Exception as e:
        # Fail quietly — leave README untouched rather than break the run.
        print(f"skipping update, could not build activity block: {e}", file=sys.stderr)
        return 0

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    replacement = f"{START}\n{block}\n{END}"

    if pattern.search(content) is None:
        print("markers not found in README.md, nothing to do", file=sys.stderr)
        return 0

    new_content = pattern.sub(replacement, content)

    if new_content == content:
        print("no change", file=sys.stderr)
        return 0

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("README.md updated", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
