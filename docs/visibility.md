# herdr, pinboards, and Kerdr

[Home](../README.md) · [Reading guide](README.md) · [Next: friction capture](friction.md)

**[Kerdr's public repository](https://github.com/drewdunne/kerdr)** is the best starting point for
the board itself. Its [feed contract](https://github.com/drewdunne/kerdr/blob/main/docs/feed.md)
lets it work with record systems other than ark-sdlc. This chapter explains how the audited
workflow supplies those records and keeps attention signals useful.

## Terminal structure and conversation ownership

| Object | Role in this workflow |
|---|---|
| Machine | Where processes and local runtime state live |
| herdr session | A group of workspaces; interactive capacity is counted per session |
| Workspace | One top-level piece of work and the conversation the person follows |
| Tab | A supporting agent, reviewer, or helper; or a run within a dedicated automation workspace |
| Pane | A terminal or plugin surface inside the tab |

Supporting agents are marked as helpers and kept out of the ordinary agent attention list.
Their output is still reachable in their tab. The primary worker reads the result and remains
responsible for it. Creating a second top-level workspace for a test would make one task look
like two separate conversations.

Disposable herdr sessions used for testing have names beginning `zz-`, their panes are marked
helpers, and the creator removes them after use. This convention prevents test agents from
surfacing as real work. It is backed by a repository check for scripts/tests that start
temporary sessions. It does not prove every arbitrary shell invocation in the account follows
the naming policy. [Evidence: E-RULES, E-HELPERS](sources.md#e-helpers).

## Pinboards answer the immediate question

Each workspace has a concise line on its pane borders and a drawer with a fuller note. For an
intent, `ark-pin` renders its full ID, short title, user story, request provenance, blockers,
dependencies, and latest agent message. The agent keeps the message short enough to be useful
when the person returns after a gap.

```sh
bin/ark-pin 9001 message "Export error handling is implemented. Checking missing and unwritable output folders."
bin/ark-pin 9001 status waiting "external review"
bin/ark-pin 9001 status under-way
```

The commands target the current workspace by default, with explicit workspace/session options
when needed. A pane ID copied from another herdr session is not sufficient context.

Pinboard precedence is deliberate: closed becomes Done; shelved becomes Shelved; unfinished
prerequisites show Waiting on their IDs; queued becomes Queued; a blocker becomes Blocked;
otherwise the agent-set status applies, falling back to Under way. Agent-set statuses are
dropped when a lifecycle change or blocker change contradicts them.

A blocker is an impediment such as a missing capability or broken tool. Waiting on the person
is an attention status. If an agent calls every pause a blocker, the person loses the distinction
between “please decide” and “the infrastructure is broken.”
[Evidence: E-PIN](sources.md#e-pin).

## The card adapter reads the same records

`bin/ark-cards` emits a version-1 JSON feed for Kerdr. It combines intent headers and bodies,
dated log entries, local pinboard records, workspace associations, slot counts, dependencies,
and Git-derived timestamps. It includes all open intents and selected recent closed work,
including closed work whose workspace is still open locally.

```json
{
  "kerdr_feed": 1,
  "source": "ark-sdlc",
  "machine": "example-machine",
  "generated_at": "2026-10-23T12:00:00-05:00",
  "sessions": {"default": {"used": 1, "limit": 3, "max": 5}},
  "cards": [{
    "id": "9001",
    "title": "Explain export failures clearly",
    "state": "background",
    "stage": "test",
    "lane": "background",
    "attention": "running"
  }],
  "warnings": []
}
```

This intentionally small fictional feed is not a dump of production data. A complete safe
example is in [examples/card-feed.json](../examples/card-feed.json).

Card stage and attention have derived rules. An explicit recognized `stage` wins; otherwise
lifecycle, triage, design metadata, and keywords in current status/latest history provide a
best-effort stage. For example, shipping language can imply Deploy, and checking language can
imply Test. These heuristics are display aids. They do not execute deployment or establish
that a design was approved correctly.

Attention combines local records with agent state. Waiting on prerequisites differs from
needing the person. A prompt reported by herdr can require attention even if the agent forgot
to update its message. Unknown or remote-local information is left uncertain rather than
invented. [Evidence: E-CARDS](sources.md#e-cards).

Normal feed polling reads records. There is a specific exception: the adapter participates in
the action store's locks and can recover an interrupted multi-record action before reading.
Calling the current feed absolutely read-only would conceal that recovery behavior.

## Backlog controls are optional, concrete mutations

Kerdr can use a configured action backend. The audited ark-sdlc backend is `ark-card-action`,
which accepts JSON requests and returns JSON responses. It supports creating a backlog record,
dispatching it, affirming that it is still wanted, dismissing/restoring it, and changing its
backlog order. Actions run against canonical records, not merely a cached card.

In this adapter, creating work records an interactive escalation for refinement; it does not
invent accepted criteria or immediately start an agent. Dispatch validates the home machine,
prerequisites, eligible lifecycle, and capacity, then invokes the ordinary dispatcher. A soft
limit returns a confirmation response; only a subsequent authorized override permits the higher
ceiling. A hard limit still refuses.

`created`, `refreshed_at`, and `backlog_rank` answer separate questions: when it originated,
when the person last affirmed it, and where it sits in that backlog. Ordinary agent log activity
should not make forgotten work look newly wanted. Dismissal uses a disposition field while
preserving the record; it does not erase history.
[Evidence: E-ACTIONS](sources.md#e-actions).

## Attention has limits

A green-looking card can still reflect stale, incomplete, or mistaken records. A disconnected
machine cannot provide fresh runtime truth. A process can work without accomplishing its task.
The board improves navigation; acceptance still rests on evidence and ownership.

For Kerdr's current interaction keys, installation, remote behavior, and public examples, use
its own [README](https://github.com/drewdunne/kerdr#readme). This handbook does not copy private
machine lists or operational configuration into an otherwise public explanation.
