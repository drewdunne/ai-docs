# Reviews, verification, and completion

[Home](../README.md) · [Reading guide](README.md) · [Next: recovery](recovery.md)

An intent records the outcome. Verification establishes whether that outcome was delivered.
A review supplies another perspective on the change. Neither a review nor a passing command
substitutes for the whole acceptance decision.

## Review gates depend on the work

For an intent triaged review, the agent writes a technical design or product spec and waits for
the person's approval of the direction. By default the design first receives a review from the
other provider. That review is a default, not a veto: the person may skip it, and unavailable
quota must be stated rather than used to withhold the design indefinitely.

Retrospective documentation of an already authorized system is not automatically a new design
proposal because it includes diagrams or explains architecture. The triage and actual task
determine the approval boundary.

High-value code and operational changes also get another provider's review under the workflow's
review policy. Small reversible changes can use judgment. The audited defaults pair Claude
work with Codex review and Codex work with Claude review, with configured model/effort and
usage-aware adjustments. These defaults are not hardcoded truths about the providers forever.
[Evidence: E-REVIEW, E-RULES](sources.md#e-review).

## The runner makes review a concrete operation

```sh
bin/ark-code-review intents/9001-export-errors \
  --repo /path/to/example-project \
  --diff worktree \
  path/to/new-file \
  --no-wait \
  --what "Check failure behavior and whether the stated acceptance criteria are met."
```

The runner gives the reviewer the intent, triage, optional design/spec, selected diff, and
relevant complete file contents inline. An untracked new file is not included by a tracked
worktree diff alone; name it explicitly. Ranges and multiple selected commits can isolate an
agent's own change when unrelated work exists nearby.

The reviewer is asked to assess correctness, failure paths, security, scope, and criteria from
that supplied text. It is not a claim that the reviewer ran the project's tests. The runner can
operate when the reviewer cannot read the working tree directly, because the material is in
the input.

Inside herdr it normally creates a helper tab in the caller's workspace. Otherwise it can use
a detached fallback. Startup and progress are visible, and the runner preserves the answer
unedited under the intent's reviews folder on a successful review.

## Waiting has a defined end

The runner records a run ID, holds a lock while reviewing, and writes an ended record. Its wait
uses that protocol rather than searching process command lines for the reviewer. A process-name
search can match its own waiting shell and continue forever.

Use the tool's `wait` or `status`, inspect the result, and act on it. The worker's pinboard should
say it is waiting on review if it ends a turn while that job runs. A finished review notification
does not finish the intent until the primary worker reads it.

| Exit | Meaning |
|---|---|
| `0` | Review completed and its answer was saved |
| `1` | Runner input/operation error |
| `2` | Review failed, timed out, produced no usable review, or could not save it |
| `3` | Reviewer quota unavailable |
| `4` | Reviewer explicitly could not review |
| `5` | A status/timed wait finds it still running |

An unavailable review is neither an approval nor a finding that nothing was wrong. The worker
records the limitation and continues where the task and policy allow it. It must not invent a
review or silently substitute its own opinion for an independent result.

## Verify the outcome, not just the implementation

Choose checks based on what could fail. For an export-error change, include failure cases and
input preservation. For a publication, check actual anonymous retrieval, licenses, links,
diagrams, and privacy. For a routing change, exercise capacity, dependency, and partial startup
paths in an isolated environment.

Tests should not merely repeat the implementation's branch conditions as assertions. A
detector that checks a string in a source file can be useful evidence that a rule exists, but is
weaker than observing the agent or executable handle the real trigger.

Record commands and actual outputs in the owning intent's log, with meaningful limits. If a
shared preflight has unrelated failures, say so; if a remote check could not run, say that too.
Re-running unrelated suites without a new concern adds less confidence than checking the
relevant boundary well.

## Interactive delivery and background completion differ

An interactive intent remains open after delivery while the person may continue the
conversation. A passing check is not permission to close it. The person explicitly asks to
wrap or close that intent.

A background intent finishes autonomously after all work is resolved. It records the result
and wraps without waiting for the person to ask. A background worker that stops with “let me
know if you want me to finish” has failed the lane's purpose.

Both paths require fresh relevant checks, current history, no unresolved friction that prevents
closure under policy, and ownership of any agents still running. `ark-state` changes metadata;
the [wrap protocol](background.md#completion-is-an-explicit-protocol) connects that mutation to
the real completion conditions.

For this publication's own checks and review availability, see [verification](verification.md).
