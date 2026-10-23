# Intents, intake, and manual triage

[Home](../README.md) · [Reading guide](README.md) · [Next: state and formats](data-model.md)

An intent is a durable unit of desired work. It preserves what was asked, defines what would
count as success, and gives every later agent a place to find the outcome and its history.
It may describe code, research, a machine fix, or documentation. It is broader than a pull
request: a pull request may be one delivery mechanism inside an intent.

The rule is to recognize an outcome request and perform intake without making the person learn
the orchestration commands. An agent should not respond to an authorized work request merely
with a plan or an offer to begin. [Evidence: E-RULES](sources.md#e-rules).

## 1. Start from current instructions

At session startup, agents load shared instructions and the project context. Instructions
define how work runs; lasting context records established direction and decisions. Live lists
of open work are obtained from status tools instead of copied into the context document.

Before starting work, `bin/ark-pull` brings the checkout current with its central Git copy.
This matters because a stale checkout carries stale rules, detectors, and dispatch behavior.
An inability to update must be made visible and resolved, rather than silently ignored.
The pull command has specific safeguards for local edits; it is not permission to reset other
agents' work. [Evidence: E-SYNC](sources.md#e-sync).

## 2. Claim the record before doing the work

```sh
bin/ark-new-intent improve-export-errors
```

The command allocates the next four-digit ID and creates an `intent.md` skeleton. The number
is not chosen by the agent. The claim is committed and published immediately, so another agent
or machine cannot legitimately take the same ID after a successful claim.

The implementation constructs a commit using a separate Git index against the central branch,
then publishes it. Concurrent successful claims can move that branch, so a loser retries with
the next available number. A local lock coordinates claims in one checkout; a central push lock
serializes updates to the central checked-out repository.

This is stronger than “pull, inspect the largest directory, add one.” That simpler sequence
leaves a race between machines. It is also narrower than a distributed task database: the
mechanism allocates Git-backed records and handles contention around their publication.
[Evidence: E-CLAIM](sources.md#e-claim).

An unavailable central copy has an explicit failure path. Some claim paths can write a local
fallback while reporting that the number is **not claimed**. Agents must treat that output as
unresolved allocation, not as authority to start work under an unreserved ID. Successful process
exit alone is insufficient; read what the command says.

## 3. Fill in outcome, criteria, and constraints

A useful intent contains:

- The requester's words, so interpretation can be checked against the original outcome.
- A short title for the workspace border and a user story for orientation.
- Observable acceptance criteria, including delivery and verification where relevant.
- Constraints such as visibility, scope, ownership, deployment permissions, or privacy.
- Priority only when the person specified it; otherwise normal.

An acceptance criterion such as “the export errors are better” leaves too much unresolved.
“An unavailable output folder produces an actionable error, preserves the input, and returns a
nonzero status” gives the agent a result it can check.

The [fictional export example](../examples/intent.md) shows the shape. Its IDs and outcomes are
illustrative, not historical case records. Skeleton fields are placeholders, not automatically
validated evidence that the intent is complete.

## 4. Run friction preflight

`friction/preflight.sh` runs the registered detector commands before an intent begins. Its output
can expose a known environmental problem or a regression relevant to the new work.

It executes **every** matching friction entry's detector with a 15-second timeout, including
entries marked accepted or remediated. It prints PASS or FAIL for each. The overall exit status
is nonzero only when at least one **open toil** detector fails.

A baseline failure elsewhere in the framework is not automatically a blocker for unrelated work.
The agent must inspect relevance, record the real output, and avoid claiming a global pass.
Equally, a successful preflight does not prove every detector passed or every human checkpoint
was satisfied. [Full explanation](friction.md#detectors-and-preflight).

## 5. Triage by hand

Every intent is triaged before work begins. The operating system currently uses an agent's
manual assessment, saved in `triage.md`, with answers to the relevant questions and the labeler.
The review judge appears in the direction and planning documents, but is not the deployed triage
mechanism. Some early overview prose describes the intended loop as if the judge decides; the
operational rule and source audit establish manual triage today.

| Outcome | Meaning | Agent's next obligation |
|---|---|---|
| `proceed` | Enough is settled to carry out the work | Implement and verify within the authorized scope |
| `escalate` | A focused answer is needed | Ask the necessary question, recording friction first |
| `review` | The direction needs an explicit design decision | Write `design.md` or `spec.md`, obtain review by default, and wait for the person's approval |

A triage file records the reasoning instead of merely stamping a label. Useful questions
include whether the outcome is clear, whether the action is authorized, whether the work is
hard to undo, and whether the person must take part along the way. The exact current private
triage documents vary; this handbook does not invent a deployed machine-readable judge schema.
[Evidence: E-TRIAGE](sources.md#e-triage).

## The lane is a separate decision

`lane: background` means the remaining work can be completed without further personal taste,
answers, or back-and-forth. It is not synonymous with `proceed`. An authorized proceed task can
still be interactive if it inherently needs collaboration.

One initial factual answer does not force the whole job into the interactive lane. The agent can
get that answer, then triage the settled remainder. Conversely, an agent should not label a task
background merely to avoid the interactive session's capacity limit.

The dispatcher consults the lane under specific routing conditions. An explicit placement flag
can change which routing branch is taken. [Dispatch precedence](dispatch.md#routing-precedence)
explains the exact exceptions; “the header always wins” would be inaccurate.

## Dependencies, children, and priority answer different questions

| Relationship | Question answered | Representation |
|---|---|---|
| Dependency | What has to finish before this may start? | `waits_on` |
| Child | Which existing piece of work is this supporting? | `parent` |
| Started by | Which agent initiated this run? | `started_by` |
| Priority | How does the person want it ordered? | `priority` |

A child intent is created with `--parent` and dispatched with `--here` into a supporting tab.
It cannot claim an independent workspace through the ordinary dispatcher. A dependency can exist
without parentage, and a background task started by another intent can be independent work rather
than a child. These relationships are used differently during dispatch and wrap.

Priority is the person's decision. The agent does not raise it because a task seems important.
High priority sorts before normal in relevant lists but does not bypass a dependency or open a
sixth interactive workspace. [Evidence: E-STATE, E-DISPATCH, E-SHELF](sources.md#e-state).

## Where intake stops being automatic

Claiming and routing a record do not grant new authority. If the request leaves an irreversible
or personal decision unresolved, the agent asks about that decision. If the work is already
authorized and the remaining choices are routine, it continues. This separation keeps autonomy
useful: meaningful decisions remain visible without turning every reversible implementation
choice into a new approval ceremony.

Next: [the file and state model](data-model.md), then [dispatch routing](dispatch.md).
