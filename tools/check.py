#!/usr/bin/env python3
"""Check this handbook's local links, fragments, JSON, fences, and optional public URLs.

Uses only the Python standard library. This checks documentation structure, not whether the
private implementation claims are true. The source audit is described in docs/sources.md.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def unfenced(text):
    out, fence = [], None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            mark = match.group(1)
            if fence is None:
                fence = mark
            elif mark[0] == fence[0] and len(mark) >= len(fence):
                fence = None
            out.append("")
        else:
            out.append(line if fence is None else "")
    if fence:
        raise ValueError("unclosed Markdown fence")
    return "\n".join(out)


def anchors(text):
    found, repeats = set(), {}
    for line in unfenced(text).splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        heading = re.sub(r"<[^>]*>", "", match.group(1)).lower()
        slug = "".join(c for c in heading if c in " -_" or unicodedata.category(c)[0] in "LN")
        slug = slug.replace(" ", "-")
        n = repeats.get(slug, 0)
        repeats[slug] = n + 1
        found.add(f"{slug}-{n}" if n else slug)
    return found


def public_get(url):
    # No GitHub CLI, authentication headers, cookies, or local credential helpers are used.
    request = urllib.request.Request(url, headers={"User-Agent": "ai-docs-link-check/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=40) as response:
            response.read(1024)
            return url, response.status, None
    except (OSError, urllib.error.URLError) as error:
        return url, None, str(error)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--network", action="store_true", help="also GET unique external URLs anonymously")
    args = parser.parse_args()
    failures, external, links, diagrams = [], set(), 0, 0
    files = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts and "node_modules" not in p.parts)
    for path in files:
        text = path.read_text(encoding="utf-8")
        try:
            body = unfenced(text)
        except ValueError as error:
            failures.append(f"{path.relative_to(ROOT)}: {error}")
            continue
        diagrams += len(re.findall(r"^```mermaid\s*$", text, re.M))
        for match in re.finditer(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)", body):
            target = match.group(1).strip("<>")
            parsed = urllib.parse.urlsplit(target)
            links += 1
            if parsed.scheme in ("http", "https"):
                external.add(urllib.parse.urlunsplit(parsed._replace(fragment="")))
                continue
            if parsed.scheme:
                failures.append(f"{path.relative_to(ROOT)}: unsupported link scheme {target}")
                continue
            linked = (path.parent / urllib.parse.unquote(parsed.path)).resolve() if parsed.path else path
            try:
                linked.relative_to(ROOT)
            except ValueError:
                failures.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not linked.exists():
                failures.append(f"{path.relative_to(ROOT)}: missing {target}")
            elif parsed.fragment and linked.suffix == ".md":
                fragment = urllib.parse.unquote(parsed.fragment)
                if fragment not in anchors(linked.read_text(encoding="utf-8")):
                    failures.append(f"{path.relative_to(ROOT)}: missing fragment {target}")
    json_files = sorted(p for p in ROOT.rglob("*.json") if ".git" not in p.parts and "node_modules" not in p.parts)
    for path in json_files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, OSError) as error:
            failures.append(f"{path.relative_to(ROOT)}: invalid JSON: {error}")
    print(f"Checked {len(files)} Markdown files, {links} links/fragments, {len(json_files)} JSON files, {diagrams} Mermaid fences.")
    print("Local links, fragments, JSON, and fence structure: " + ("FAIL" if failures else "PASS"))
    if args.network:
        with ThreadPoolExecutor(max_workers=4) as pool:
            for url, status, error in pool.map(public_get, sorted(external)):
                print(f"Anonymous GET {status if status else 'FAIL'} {url}")
                if error:
                    failures.append(f"{url}: {error}")
    for failure in failures:
        print(failure, file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
