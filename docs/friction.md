# Friction capture: turning interventions into evidence

[Home](../README.md) · [Reading guide](README.md) · [Next: reconciliation](reconciliation.md)

Friction is a record that the person had to intervene or perform a manual step. Its purpose is
to change future work, not to produce a blame log. The distinction between avoidable toil and
an intentional human checkpoint determines what a good remedy looks like.

## What gets recorded

There are two entry paths. Before asking the person to do something, an agent creates a friction
record. Separately, when the person steps in without being asked, the agent records that
intervention in the same turn.

| Situation | Typical treatment |
|---|---|
| A reminder to do something already required | Friction; the process did not reliably carry its rule |
| A repeated request after a partial delivery | Friction; the prior completion boundary was wrong |
| A manual command the agent could have run itself | Usually toil |
| A password, physical action, or genuinely personal choice | Usually a gate to make inexpensive |
| A new request, ordinary question, approval, or initial scope clarification | Not automatically a stepping-in case |

The agent still uses judgment. Cue words are not a verdict, and a person can correct the
classification. A gate is not a defect to remove indiscriminately: keeping an intentional
authorization boundary may be the correct result.
[Evidence: E-PERSONAL, E-RULES](sources.md#e-personal).

## Search before creating

```sh
bin/ark-friction find export error
bin/ark-new-friction export-error-needs-manual-diagnosis
```

If the same problem already has an entry, append a case instead of creating another category.
An entry describes a recurring problem and its remedy; a case describes one occurrence.
That distinction lets recurrence test whether a claimed fix held.

`ark-new-friction` uses the shared ID-claiming mechanism and publishes a skeleton. The agent
then fills in what happened, the intent, classification, detector, remedy, and residual work.
As with intents, claiming a skeleton is not evidence that its content is finished.

## Entry format

```yaml
---
type: friction
id: F-9001
title: Export failure required manual diagnosis
intent: 9001-export-errors
kind: toil
status: open
detector: 'tests/export-errors/run'
---
```

The body has sections for what happened, cases, remediation, and residual manual work. The
detector is an executable shell command, not merely a prose promise. Toil needs a command that
fails while the problem is present and passes once the remedy works. The fixture in
[examples/friction.md](../examples/friction.md) is fictional and its detector path is illustrative.

| Field/value | Meaning |
|---|---|
| `kind: toil` | Avoidable work to remove |
| `kind: gate` | A deliberate checkpoint to preserve and make cheap |
| `status: open` | Unresolved; investigate or perform the remaining checkpoint |
| `status: remediated` | A remedy has been applied and checked |
| `status: accepted` | The person deliberately accepts what remains; agents cannot grant this themselves |

“Remediated” should say what changed and how it was checked. It is not synonymous with a detector
returning zero once. A weak detector can pass while the underlying behavior remains wrong.

## Appending cases and publication semantics

```sh
bin/ark-friction case F-9001 --intent 9001 --id example-export-1 "The export failed without explaining the unwritable destination."
```

The case command adds a dated occurrence with intent attribution and a marker for deduplication.
By default its occurrence ID incorporates session identity and a digest of the supplied text;
an explicit `--id` supports stable idempotent callers.

On ordinary recurrence, a remediated entry is reopened. `--past` records an occurrence from
before the remedy without reopening it; `--missed` says the person had to point out the missed
friction. Accepted entries are not automatically rewritten into a different acceptance decision.

Publishing constructs a commit against the central copy using a separate index. It retries
contention and reports a precise result:

| Message | What the agent may claim |
|---|---|
| `recorded and published` | The case reached the central copy |
| `already recorded` | That occurrence marker was already present |
| `recorded here, not yet published` | A local record exists; cross-machine publication is incomplete |
| Failure after retries | Do not claim the case was recorded successfully |

The command screens for several secret-like patterns, including common token formats and
key material. This is a useful rejection check, not a comprehensive privacy classifier. The
agent must paraphrase private details before recording anything in an inappropriate store.
[Evidence: E-FRICTION, E-CLAIM](sources.md#e-friction).

## The prompt hook is a reminder

`ark-friction check` reads a prompt-hook JSON payload. It extracts the latest relevant user
input, removes certain quoted/relayed blocks, ignores known automation openings, and compares
the beginning of the remaining message against cue patterns. Voice delegation has special
handling so repeated older conversation does not fire again as a new correction.

When cues match, the hook gives the agent extra context reminding it to decide whether to
record friction or a win. The person does not see a new modal dialog. The hook is designed not
to fail the prompt. It skips applicable noninteractive execution paths and can be switched off
or forced in tests.

It **does not** create the friction entry, choose toil versus gate, diagnose a cause, accept a
residual, allocate an improvement intent, or dispatch work. Those are agent actions.

The local cue-hit log stores time, session, and cue kinds, never the full message. Old hits are
trimmed on a bounded retention policy. That statement concerns this log only; it says nothing
about the agent application's separate transcript retention.

## Misses become regression cases

If the person must point out that friction itself was missed, the agent records the underlying
problem as a missed case, also records the capture failure, and adds an appropriate cue test.
If the cue matched but the agent ignored it, changing the regex is not an honest explanation of
the failure. The remedy may need instructions or agent-behavior verification instead.

The rule also requires attribution by provider, application, model, and reasoning effort when
known. Missing values are marked unknown instead of inferred from a global default. The current
case tool primarily stores the text the agent supplies; it does not independently discover and
validate all of that attribution. [Evidence: E-PERSONAL, E-CUES](sources.md#e-cues).

## Detectors and preflight

The implementation is unusually easy to state precisely:

1. Iterate over every matching `friction/F-*.md` entry.
2. Read its fields through the shared OKF reader.
3. Run its detector using `timeout 15 bash -c`, suppressing detector output.
4. Print PASS on status zero, otherwise FAIL, along with ID, kind, status, and title.
5. Remember a global failure only when the entry is both **toil** and **open** and its detector
   failed; exit nonzero if any such entry failed.

| Detector result | Entry kind/status | Printed | Makes overall exit nonzero? |
|---|---|---|---|
| Pass | Any | PASS | No |
| Fail or timeout | Open toil | FAIL | Yes |
| Fail or timeout | Remediated toil | FAIL | No |
| Fail or timeout | Accepted toil | FAIL | No |
| Fail or timeout | Any gate | FAIL | No |

This table is why both the per-entry output and exit status matter. A failed remediated detector
deserves investigation even though it does not change preflight's exit. The script itself does
not reopen that entry, create a task, or choose a remedy. A timeout is a failed command, not a
root-cause diagnosis.

Detectors execute shell commands with the running account's authority. They must be treated as
trusted code and kept appropriate to repeated execution. Preflight is not a safe sandbox for
arbitrary commands. [Evidence: E-PREFLIGHT](sources.md#e-preflight).

Next: [how agents reconcile the evidence into improvement work](reconciliation.md).
