---
type: intent
id: 9001
title: Make export failures actionable
priority: normal
short: Explain export failures clearly
story: As a user I want actionable export errors so that I can recover without losing input.
stated_by: Andrew
stated_at: 2026-10-23
status: open
state: background
home: example-machine/default
---

## Intent (fictional request)
Make the export tool explain why it cannot write the destination, and keep the input untouched.

## Acceptance criteria
- A missing output directory produces an actionable error and a nonzero status.
- An unwritable output directory produces an actionable error and a nonzero status.
- Both failures leave the input intact.
- The worker records relevant verification and a concise result.

## Constraints
- Change the specified export failure behavior within the authorized project scope.
- Example only; no executable tool or test suite is included here.
