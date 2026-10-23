# Failure paths and recovery

[Home](../README.md) · [Reading guide](README.md) · [Next: examples](examples.md)

The workflow is useful partly because its failure states have durable names and explicit
ownership. A failed command, a stopped agent, a stale card, and an unfinished intent are not
interchangeable. Recovery begins by finding which layer stopped and whether an action may
already have happened.

## Routing and startup

| Symptom | Current behavior | Recovery obligation |
|---|---|---|
| Central copy cannot be reached during ID claim | Claim may fail or report a local unclaimed fallback | Do not invent a number or start on an unreserved ID; restore publication and verify ownership |
| Dispatcher says prerequisites remain open | No new work starts; never-started work can be queued; exit 3 | Resolve or finish prerequisites, or use `--no-wait` only at the person's word |
| Interactive session is full | No workspace opens; intent becomes queued; exit 3 | Report accurately, use background if that is the correct triage, or obtain authorized override/shelving |
| Session is already at the hard ceiling | Override cannot add more | Shelve appropriate work before dispatching |
| herdr client and server differ | Dispatch refuses rather than assuming compatibility | Inspect versions and running work; do not casually restart a server and kill others' panes |
| Agent startup stops at login/trust | Placement may already exist and state may already be active/background | Inspect that pane, handle only the real missing step, and send its existing brief when ready |
| Pinboard installation warns | Dispatch may still complete | Repair visibility without pretending the work never started |

These paths are grounded in [E-CLAIM, E-DISPATCH, E-SLOTS](sources.md#e-dispatch). Exit 3 is
contextual: for dispatch it commonly means deferred startup, while for review it means quota
unavailable, and for friction publication it can mean local-only recording.

## A background run stops

The stalled-agent check can prompt an eligible idle background worker once, then notify the
person if it remains stopped or stops again too soon. It does not universally restart every
failed process. Inspect the pane, lifecycle, pinboard, and quota/tool output before deciding
whether to resume or replace it.

If a worker is replaced, preserve the intent, its home, log, and workspace association. Verify
the replacement's session/socket/pane context. A process launched from another conversation
can inherit that conversation's `HERDR_*` variables; blindly calling a close command could
target the wrong session. Explicitly establishing identity is a real recovery check, not
ceremony. [Evidence: E-STALLED, E-WRAP](sources.md#e-stalled).

If ongoing work was started by another worker that is wrapping, its undertaker takes over
watching. If the watcher cannot see a session, uncertainty must not be treated as proof that a
target has gone. The handoff tool distinguishes unreadable state from an absent pane.

## Quota and independent review

A weekly or short-term provider limit can stop a worker before it begins or during work. The
dispatcher does not provide a universal quota-aware failover service. An authorized supervising
agent can substitute a worker and preserve ownership; otherwise the limitation remains visible.

The review runner reads usage, chooses configured effort within its rules, and can wait for a
near reset. `--no-wait` returns instead of waiting for quota. If no review can be obtained, log
the reason and proceed where policy allows, describing the result as unreviewed. Do not call an
unavailable reviewer an approval.

## Ambiguous mutations

A timeout can mean the caller did not receive the answer, not that nothing happened. Examples
include a case push, a card action, a prompt send, or remote publication. Check the canonical
record before retrying a non-idempotent action.

Friction cases have occurrence markers to avoid duplicate append. Stalled recovery records a
prompt attempt before sending it to avoid repeatedly prompting after uncertain delivery. Kerdr
actions report uncertainty rather than blindly retrying an operation whose result may already
be saved. These mechanisms are specific to their operation; there is no global exactly-once
execution guarantee. [Evidence: E-FRICTION, E-STALLED, E-ACTIONS](sources.md#e-actions).

## Detector disagreement

| Observation | What to investigate |
|---|---|
| Open toil detector fails | Is it relevant here? Is the underlying condition still present? |
| Remediated detector fails | Regression, wrong machine, stale detector, or incomplete rollout |
| Accepted/gate detector fails | Whether the residual/checkpoint remains expected; global exit alone will not expose it |
| Detector passes but intervention recurs | The detector may be too weak or the agent may not use the remedy |
| Preflight exits zero with some FAIL rows | Expected semantics when no failing row is open toil; inspect the rows |

Preflight suppresses detector output and times each at 15 seconds. A focused diagnostic run
may be needed. A nonzero overall preflight is evidence of a failing open toil detector somewhere,
not an automatic prohibition on all unrelated work. [Exact semantics](friction.md#detectors-and-preflight).

## Shared working copy and Git

Agents may edit one checkout concurrently. The allocator and case publisher use separate
indexes for their narrow operations, but ordinary manual Git commands still share the real
index. Before committing, inspect both working-tree and staged changes. Save only the files
owned by this task.

If another agent has staged files, do not unstage, amend, reset, stash, or commit them as a
convenience. A narrowly scoped `git commit --only -- PATHS...` can commit owned paths while
leaving unrelated index entries alone. Verify the resulting commit's file list and the remaining
index. If a file itself contains another agent's unfinished edits, resolve ownership before
including it; selecting its path does not isolate mixed edits inside that file.

The usual hook pushes a commit to the central copy. A local commit and successful hook process
are not sufficient evidence of remote publication: inspect branch/remote state or the push
result. A push warning must remain visible until resolved. `ark-pull` likewise reports stale or
stuck updates rather than permission to discard edits.
[Evidence: E-SYNC, E-RULES](sources.md#e-sync).

## An intent is closed but the pane remains

Check whether completion really occurred, the result was recorded, and the closing operation
ran in the right environment. Wrap closes the worker's pane last; it must not close another
agent's conversation to make the display tidy. The pinboard drawer may remain if other panes
still need the tab.

The dispatcher has a fallback cleanup for old closed background workspaces on a later dispatch.
That is not a replacement for normal wrap, and it does not prove a closed intent's acceptance
criteria were met. If the metadata was wrong, correct the record and resume the real work.

## When only the person can resolve it

Prepare the concrete decision, record friction before asking, set the right attention status,
and ask once with the necessary context. Do not hand over a command just because the agent did
not try a reachable machine or available tool. Do not infer approval from silence. The system's
goal is fewer avoidable interruptions while retaining the decisions that belong to the person.
