# Publication verification

[Home](../README.md) · [Reading guide](README.md) · [Source evidence](sources.md)

This is the verification record for the 2026-10-23 publication. It distinguishes source review,
structural checks, diagram inspection, independent review, and actual public delivery.

## Source and content review

The author inspected the implementation units named in the [source map](sources.md). The
[manifest](../audit/source-manifest.json) preserves digests and symbol locations without
publishing private source. Chapters distinguish manual triage from the planned judge, the
historical decision-replay experiment from deployed behavior, and agent reconciliation from
unverified scheduling.

An independent primary agent read the substantive chapters and fictional examples, checking
the claims against the private implementation. It reported no substantive text correction.
It identified overly wide diagrams, which were made vertical and checked again. This was a
second source audit by the same provider, not an other-provider review.

## Other-provider review limitation

The independent primary agent attempted `ark-code-review` from the actual background pane.
It exited **3** immediately: Claude's weekly usage was **100%**, with reset reported as
Saturday 03:00. No review ran, and no answer or approval exists. The publication proceeded under
the authorized unavailable-review policy, with source audit and direct checks recorded here.
There was no quota wait or retry.

## Structural and diagram checks

The repository includes [repeatable check tools](../tools/README.md). The structural run checked
**26 Markdown files, 215 links/fragments, three JSON files, and seven Mermaid fences**, with no
local target, fragment, JSON-syntax, or fence errors. The four example YAML headers parsed
successfully. All **six unique public external targets returned HTTP 200** through anonymous
GETs using no GitHub credentials. Counts describe that run; later evidence links can increase
the link count without changing the substantive chapters.

All seven Mermaid fences were independently rendered successfully. The two long improvement
chains were changed to top-to-bottom layout for the GitHub content column. The compacted
diagrams were re-rendered and visually inspected. Final visual inspection also simplified the
lifecycle diagram by putting resume/reopen transitions in an adjacent table, and removed a
layout-distorting return arrow from reconciliation. Those diagrams were re-rendered and checked.
Syntax/render checks and readability checks are separate pieces of evidence. The renderer was
Mermaid CLI 11.15.0 using local Chromium; temporary SVG/PNG artifacts are kept outside the public
repository.

## Privacy and scope

The public files are newly written prose, fictional examples, verification tools, and source
digests. They exclude private source-file contents, host inventory, production configuration,
transcripts, sensitive case details, private reports, and decision-replay datasets/results.
Public links point to public resources; private source locators are plain code text.

Pattern-based hygiene checks supplement file-by-file review. They are not a mathematical proof
that prose contains no private information. The scope was deliberately limited to workflow
mechanisms and safe invented records.

## Framework preflight baseline

The required startup `friction/preflight.sh` completed with exit **1** because unrelated open
toil detectors fail in the shared framework. This publication did not claim that full suite
passed or treat unrelated baseline entries as publication blockers. No friction entry was
raised for this intent. Scope additions about public visibility, thoroughness, and MIT licensing
were ordinary clarifications, not unsolicited stepping-in cases.

## Public delivery checks

The public delivery audit checks actual repository visibility, anonymous retrieval, license
detection/content, and saved file equality independently of authenticated GitHub CLI success.
The final observations are recorded with the public publication. Kerdr was already public with
a complete MIT license, copyright 2026 Andrew Dunne; this task did not change Kerdr.

## Limits of this verification

The checks do not install or replay the entire private framework, grant access to it, prove all
agents comply with policy, or verify an unobserved reconciliation schedule. The historical
experiment is not republished. Public companion projects can evolve after the audit date; use
their own documentation for current interfaces and releases.
