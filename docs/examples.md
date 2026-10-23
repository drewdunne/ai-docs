# Worked examples

[Home](../README.md) · [Reading guide](README.md) · [Next: command reference](commands.md)

All examples in this chapter are fictional. The `9000`-series IDs are explanatory placeholders,
not numbers an agent should claim manually. Example commands assume the private framework is
already installed. They illustrate operations; do not run them against real records just to
try the documentation.

## A. An autonomous fix from request to result

The person asks: “Make the export tool explain why it cannot write the destination, and keep
the input untouched.” The agent recognizes a concrete outcome with observable failure behavior.

1. It updates the framework checkout and uses `ark-new-intent` to claim the actual ID.
2. It records the request, failure cases, preservation requirement, and scope in `intent.md`.
3. It runs preflight and inspects any relevant failures without claiming unrelated baseline
   failures passed.
4. It triages manually: the behavior is specified, the work is authorized, and no further
   personal choice is needed. It records proceed and `lane: background`.
5. It dispatches through the normal path. The background worker retains the origin home.
6. The worker implements the fix, checks both missing and unwritable output directories, and
   checks input preservation and nonzero failure status.
7. It obtains review if appropriate/available, resolves useful findings, and records evidence.
8. It verifies no unresolved friction prevents closure, hands off any remaining agents, records
   the one-line result, closes the intent, and wraps its own pane.

The [example intent](../examples/intent.md), [triage](../examples/triage.md), and
[dated log](../examples/log.md) show the durable record. The final result says what changed,
not “I can finish this if you want.” The background run's purpose is to complete the settled
outcome without another round of permission for routine work.

## B. A full interactive session

Three ordinary workspaces already occupy the session. A fourth interactive intent is ready.
The agent attempts dispatch without an override.

```text
Result: queued, not started
Exit: 3
New workspace: none
Intent home: the originating interactive session
```

The agent reports the situation in a sentence. If the person says to start anyway, it can use
`--override`, up to five. If five are already occupied, it must shelve first. High priority would
move the new intent earlier in relevant lists, but would not change either ceiling.

If investigation shows the task actually needs no ongoing interaction, the agent corrects the
triage and dispatches to background. That is a lane correction based on the work, not a silent
capacity bypass. A task that needs the person's taste should remain interactive even when that
is inconvenient.

## C. Prerequisites close, but the task does not launch itself

The export fix cannot start until a format migration and a dependency update finish:

```sh
bin/ark-state waits-on 9001 9002 9003
```

While either is open, dispatch refuses startup and prints the unfinished prerequisites. If the
task was never started, it can be queued. When `9002` closes, the log says one prerequisite
finished and another remains. When `9003` closes, the log and notification say the intent is free
to start.

The next action is a fresh dispatch by an agent or person. There is no assertion here of a
continuously running dependency scheduler. An explicit `--no-wait` is only appropriate if the
person authorizes starting early.

## D. Friction becomes an improvement

During another task, the person has to ask, “Did you check the destination permissions?” The
agent should already have investigated that cause before handing the failure back. It searches
for existing friction about the same problem and appends a case, or claims a new entry.

The first remedy might be a better troubleshooting command plus instructions to use it. A
detector exercises the command on a safe unwritable destination and checks actionable output.
The agent links the entry to its improvement intent and dispatches the work autonomously if
the remaining scope is settled.

After the implementation, the agent checks behavior, records the remedy and residual, and marks
the friction remediated. On a later recurrence, normal case capture reopens it. The next agent
investigates whether the command was missing, the instructions were ignored, the environment
changed, or the detector was too weak. It does not create a new category merely because the
symptom appeared in a different task.

This is [agent-led reconciliation](reconciliation.md). The example does not assume a daemon
woke up after the hook; the agent is the actor connecting the evidence to work.

## E. A gate stays a gate

A task requires the person to choose the wording of a public statement under their name. The
agent records a gate before asking. It prepares the exact text, supporting context, and the
smallest useful decision.

The improvement is making the checkpoint cheap and concrete. It is not removing the checkpoint
by inferring approval from silence. If the person accepts a residual manual step, that decision
is recorded by their authority; the agent cannot set accepted just to close faster.

An ordinary initial scope clarification is different from stepping in to correct a prior miss.
Both may inform the task, but only the latter is automatically the kind of unsolicited
intervention described by the capture rule.

## F. A stopped turn and a quota failure

A background worker becomes idle under Under way after a dropped turn. The observer sees an
eligible stable state for five minutes and prompts once. If it remains stopped another five
minutes, it tells the home session and sets waiting Andrew. Those times are defaults and are
sampled by the two-minute timer, so the reaction is not an exact wall-clock deadline.

If the actual problem is an exhausted provider subscription, a continuation prompt cannot
produce more quota. A supervising agent can inspect the failure and replace the worker when
authorized, preserving its intent and execution context. That intervention is recovery by an
agent, not built-in automatic provider failover.

## G. A review is unavailable

The worker requests the other provider's review with `ark-code-review --no-wait`. Usage checks
find the provider out of quota and exit 3. No review answer exists.

The worker records the limitation, performs its own source/behavior checks, and continues where
the workflow permits it. It never says “review passed.” If the task specifically required a
successful independent approval as a hard condition, that would remain unresolved; the general
review default does not let an agent rewrite a task's explicit acceptance criteria.

## H. A parent finishes before a helper

A primary worker has delivered its own result, but a supporting verification agent still runs.
Before wrapping, it calls the undertaker tool. The tool finds the leftover target and assigns
an undertaker intent to watch it. The primary records the handoff and can close its own pane.

The undertaker reads the helper's answer, checks what it means for the original delivery,
answers settled questions, and fixes or creates owned follow-up work. A new personal decision
comes back as a focused question. The helper is not left for the person to notice by accident.

## I. Kerdr backlog creation and dispatch

With an action adapter configured, the person creates a backlog item in Kerdr. The private
adapter claims the ID through the same allocator and saves the words, home, scope, queued state,
and an interactive escalation for refinement. It does not invent acceptance criteria or start
the agent just because the form was saved.

Later dispatch checks eligibility and the home machine, resolves prerequisites, counts capacity,
and invokes the ordinary dispatcher. If the soft limit is full, the backend returns a
confirmation response. The subsequent override is a separate personal decision; a hard limit
still refuses. After a mutation, the next feed read reflects the canonical files.

See [the JSON action example](../examples/card-action.json) and the
[public Kerdr contract](https://github.com/drewdunne/kerdr/blob/main/docs/feed.md).
