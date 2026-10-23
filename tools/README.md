# Documentation checks

[Handbook verification](../docs/verification.md)

From the repository root, run the structural checker with Python 3:

```sh
python3 tools/check.py
python3 tools/check.py --network
```

It checks relative Markdown targets and local heading fragments, JSON syntax, and balanced code
fences. Network mode uses anonymous HTTP GET requests for unique public targets with their
fragments removed. It does not use GitHub credentials. External fragment validity and the
truth of prose still require inspection.

To render diagrams, separately install the Mermaid command-line renderer and provide its path:

```sh
python3 tools/render_diagrams.py \
  --mmdc /path/to/mmdc \
  --output /tmp/ai-docs-diagrams \
  --puppeteer-config /path/to/local-puppeteer.json
```

The optional Puppeteer configuration selects a locally available browser. The script extracts
each Mermaid block and renders SVG and PNG artifacts to the requested output directory. It
fails if a render fails. It does not install packages, modify private source, or publish anything.
Inspect the PNGs: valid syntax alone cannot establish readable labels or sensible flow.

The source manifest is a publication-time audit artifact. The public checker can validate its
JSON syntax, but cannot compare its digests against unavailable private source. An authorized
maintainer can perform that comparison in the private checkout.
