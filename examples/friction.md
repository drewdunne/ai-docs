---
type: friction
id: F-9001
title: Export failure required manual diagnosis
intent: 9001-export-errors
kind: toil
status: remediated
detector: 'tests/export-errors/run'
---

## What happened
In this fictional scenario, the person had to remind an agent to inspect destination permissions.

## Cases
- 2026-10-23, intent 9001: The export failed without explaining the unwritable destination. Provider, app, model, and effort are unknown in this fictional example. Caught by the agent in the same turn. <!-- case example-export-1 -->

## Remediation
The fictional export tool now checks the failure and returns actionable context. Its illustrative
detector covers missing/unwritable destinations, failure status, and input preservation.

## Residual
A user still chooses an output folder they are permitted to write. That ordinary product action
is separate from asking the person to diagnose an unexplained agent failure.

This is a format example. The detector path does not exist in this documentation repository.
