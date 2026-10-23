# Source evidence and claim boundaries

[Home](../README.md) · [Reading guide](README.md) · [Next: publication checks](verification.md)

This handbook was checked against the existing implementation on **2026-10-23**, rather than
written from a proposed architecture. This page records how to interpret its evidence and where
the explanation has limits.

## Public references versus private audit locators

The public references are independently readable:

- [Kerdr repository](https://github.com/drewdunne/kerdr),
  [feed and action contract](https://github.com/drewdunne/kerdr/blob/main/docs/feed.md), and
  [MIT license](https://github.com/drewdunne/kerdr/blob/main/LICENSE).
- [herdr](https://herdr.dev/) and its [installation documentation](https://herdr.dev/docs/install/).
- [Open Knowledge Format specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md).

The ark-sdlc source remains private. Paths below are **audit locators**, not public hyperlinks.
They identify which files/functions were inspected without republishing those files, host
inventory, operational configurations, transcripts, or case reports. No reader is expected to
authenticate to a private server to follow the public handbook.

The [source manifest](../audit/source-manifest.json) records repository revision, SHA-256 file
digests, line counts, and symbol locations for the inspected implementation units. The digests
let an authorized maintainer compare the documented snapshot with their own checkout; they do
not make the underlying private files publicly verifiable. Prose and synthetic examples are
newly written, not source-file exports.

Evidence categories used here:

| Category | Meaning |
|---|---|
| Implementation | Read executable branches, fields, or output contracts |
| Policy | Read instructions/skills; compliance still depends on the agent |
| Operational observation | Inspected a real command response, runtime inventory, or existing work history |
| Public contract | Independently accessible upstream documentation/source |
| Planned/experimental | Explicitly distinguished from deployed capability |
| Unverified | Evidence did not establish the operational claim |

## E-RULES

**Sources:** `AGENTS.md`, `CONTEXT.md`.

**Supports:** intake obligations, intent/triage lifecycle, lane policy, capacity policy, helper
layout, dependencies, priority ownership, friction obligations, closure rules, and current
direction. These are policy unless a command entry below provides enforcement.

**Limit:** an instruction stating a rule does not prove every agent follows it. Early README
language about a judge is reconciled against the explicit current manual-triage rule and the
context's planned phase, rather than treated as evidence of an operating service.

## E-PERSONAL

**Source:** `config/agents/global-CLAUDE.md` (shared personal instructions).

**Supports:** recording unsolicited interventions, differentiating normal requests from
stepping-in cases, reporting actual publication outcomes, capture misses, attribution metadata,
positive feedback capture, interactive closure only on request, and automatic background wrap.

**Limit:** naming the shared file does not publish its contents or prove a particular front-end
loaded it. Provider/model defaults cannot substitute for missing per-occurrence attribution.

## E-INTAKE

**Sources:** `bin/ark-new-intent`, `AGENTS.md` intake rules, `bin/ark-dispatch` placement/brief.

**Supports:** outcome to claimed skeleton to manual triage to placement. Parent and priority
options are implemented; interpreting the person's desired outcome remains agent work.

## E-CLAIM

**Sources:** `bin/lib/ark-claim.sh` functions `ark_claim`, `ark_taken`, `ark_receive_pack`;
`bin/ark-new-intent`; `bin/ark-new-friction`.

**Supports:** numeric allocation, separate index, central publication, local/central locks,
concurrent-claim retry, central refusal handling, and explicitly unclaimed offline fallback.

**Limit:** a skeleton is not completed intake. An unclaimed fallback must not be treated as a
successful reserved ID. The locks described are scoped to the implementation's Git operations,
not a blanket transaction mechanism for every operation agents can run.

## E-TRIAGE

**Sources:** `AGENTS.md` intent triage rules; `CONTEXT.md` direction; current manual triage records;
`bin/ark-dispatch` lane extraction and required-file checks; `bin/ark-cards` function `triage`.

**Supports:** manual proceed/escalate/review labels, background lane decision, recorded reasoning,
future evaluation intent, and the distinction between semantic triage and dispatcher parsing.

**Limit:** the dispatcher checks files/placement; it does not implement the planned judge or
prove a review design was approved by interpreting every answer.

## E-STATE

**Source:** `bin/ark-state`, including `get`, `_set_state`, `write`, `set_waits`, `waiting`,
`set_result`, `results`, `release`, `tell`, `notify`, `priority`, and `touched`.

**Supports:** five settable lifecycle states, closed-status precedence, explicit reopen,
home/initiator/result metadata, prerequisite validation and cycles, log/notification on release,
narrow auto-commit behavior, and substantive-activity ordering.

**Limit:** `closed` does not check friction, criteria, or approvals. Dependency release does not
start the dependent intent. Notifications are best effort and have machine/home fallback rules.

## E-OKF

**Sources:** `bin/lib/okf.py` functions `parse`, `state_fields`, `move_log_header`, `add_log_entry`,
`locked`, and `problems`; `bin/lib/okf.sh`; `bin/ark-okf`; `config/okf-types.tsv`.

**Supports:** typed YAML headers read with scalar preservation, historical log-header migration,
dated log shape, common parsing, locks, and format checks.

**Limit:** conformance does not establish truth, authorization, privacy, or acceptance. External
YAML parsers can apply different implicit scalar conversions.

## E-DISPATCH

**Sources:** `bin/ark-dispatch` option parsing, lane selection, `hd`, `mark`, `need_slot`,
prerequisite refusal, `--self` handling, generated brief, placement/start/prompt path, and
background cleanup; dispatch configuration.

**Supports:** placement precedence and incompatible flags, origin home, child restriction,
workspace naming, settings for background/helpers, model configuration, startup partial failure,
best-effort notes/state, and cleanup on later background dispatch.

**Limit:** no semantic triage engine, automatic provider failover, queue-draining service, or
authorization verification of the person's override words is implemented by this command.
Configuration values in the prose are snapshot descriptions, not a full production config.

## E-SLOTS

**Sources:** `bin/ark-slots` function `slots` and count/list branches; `bin/ark-dispatch` function
`need_slot`; attention configuration.

**Supports:** live workspace counting, configured exemptions, three/five default ceilings,
session-scoped capacity locking, and background attention-limit exemption.

**Limit:** slot count measures workspace attention, not resource capacity or tenant isolation.

## E-SHELF

**Sources:** `bin/ark-shelf`, `bin/ark-shelve`, and `config/agents/herdr/shelve/SKILL.md`.

**Supports:** session grouping, queued/shelved lists, priority ordering, stale-work prompts,
recent background result window, candidate selection, prepared resume, and self-shelving.

**Limit:** the shelf displays eligibility; it is not an automatic queue scheduler. Shelving closes
a workspace after preparation, while wrap closes the worker's own pane.

## E-PIN

**Sources:** `bin/ark-pin` rendering/status branches and refresh; `config/pinboard/template.md`;
the public pinboard integration invoked by the framework.

**Supports:** story/message/blockers/status, precedence, local files, state-bound status expiry,
per-workspace update coordination, and full-ID orientation.

**Limit:** an agent must provide truthful updates. A machine-local message is not a substitute
for durable log evidence.

## E-HELPERS

**Sources:** `bin/ark-helper`; `bin/ark-dispatch` `--here` path; `bin/ark-temp-sessions`;
`AGENTS.md` helper and disposable-session rules.

**Supports:** supporting tabs, helper labeling, test-session naming convention, and the staged
repository check for inappropriate temporary session starts.

**Limit:** the convention and check are not a universal prohibition on arbitrary runtime shell
commands outside the repository.

## E-CARDS

**Sources:** `bin/ark-cards`, especially `stage`, `attention`, `card`, `triage`, `pin_status`,
`git_dates`, and the action-store guard/recovery paths; `tests/ark-cards/run`.

**Supports:** feed version and fields, stage/attention derivation, partial-data warnings,
recent-closed selection, backlog metadata, normal read behavior with interrupted-action recovery.

**Limit:** stage and attention can be heuristic; unknown data is not verification. The private
test suite is source evidence for intended coverage, not a claim that this documentation task
reran the complete framework suite.

## E-ACTIONS

**Sources:** `bin/ark-card-action` functions `create`, `dispatch`, `action`, `move`, `check_home`,
`save_records`; related store guards in `bin/ark-cards`; public Kerdr feed/action contract.

**Supports:** JSON-only request data, canonical record mutation, home validation, background-aware
capacity handling, soft-limit confirmation/hard-limit refusal, creation without startup,
backlog refresh/disposition/order, private-index publication, and interrupted action recovery.

**Limit:** a trusted configured backend is required. A timeout is not proof no mutation occurred.
Action creation's interactive escalation is a refinement placeholder, not autonomous semantic
triage. Current deployment behavior can differ from another reader's Kerdr adapter.

## E-FRICTION

**Sources:** `bin/ark-friction` functions `check`, `match_cues`, `interactive`, `log_hit`, `add_case`,
`publish_case`, `local_only`, `find_cmd`; `bin/ark-new-friction`; `friction/TEMPLATE.md`.

**Supports:** cue reminder behavior, input filtering, case IDs/deduplication, normal recurrence
reopening, past/missed options, publication outcomes, and secret-pattern screening.

**Limit:** the hook does not diagnose, create entries, or dispatch. Screening does not guarantee
privacy. Agent judgment and accurate text remain required.

## E-CUES

**Sources:** `config/agents/friction-cues`, `tests/friction-cues/run`, `tests/win-cues/run`,
personal instructions' missed-capture rule.

**Supports:** tested cue families and capture-regression practice.

**Limit:** the handbook does not publish private cue-case transcripts or claim regex matching
fully detects human intent. Existing cases and agent-behavior checks are distinct forms of
evidence.

## E-PREFLIGHT

**Source:** `friction/preflight.sh`, full executable loop (short enough to inspect as one unit).

**Supports:** every matching entry is checked, `timeout 15 bash -c`, suppressed detector output,
PASS/FAIL printed independently of metadata, aggregate nonzero only for failing open toil.

**Limit:** no automatic reopening, reconciliation, dispatch, or closure gate. Gate/remediated/
accepted FAIL rows can coexist with overall zero. This publication's baseline exited 1 from
unrelated open toil; it did not raise friction of its own.

## E-RECONCILIATION

**Sources:** friction/personal/intent rules, the commands above, and existing intent histories
showing agents creating and dispatching improvement work from friction. Local/server user-timer
inventories and available task metadata were inspected separately.

**Supports:** an existing agent-led reconciliation procedure connecting evidence, root-cause
investigation, ownership, intake, dispatch, remedies, and checked status.

**Limit:** no dedicated friction reconciler binary or versioned timer was found, and a specific
external schedule was not verified. This bounded negative observation does not prove that no
external trigger exists. The chapter is an operational synthesis, not a quoted scheduler prompt.
Private case details and inventories are deliberately omitted.

## E-WINS

**Source:** `bin/ark-win` draft, `check_draft`, allocation/publication, `find`, and list paths;
shared personal instructions and cue tests.

**Supports:** structured positive evidence, required fields, win IDs, work types, tags,
publication outcomes, and possible later mining.

**Limit:** neither a win database nor a mining intention proves an automated optimizer is running.
Private record content is not reproduced.

## E-REVIEW

**Sources:** `bin/ark-code-review`, `bin/ark-design-review`, `bin/lib/review.sh`, and review
configuration; code runner's `report`, `save`, `run_review`, and terminal-status handling.

**Supports:** other-provider selection, usage-aware effort/quota handling, inline inputs,
helper/detached execution, lock-and-ended-file waiting, preserved answers, and exit statuses.

**Limit:** review text is not execution evidence. Quota unavailable is not approval. The
publication records its own review outcome separately in [verification](verification.md).

## E-WRAP

**Sources:** `config/agents/herdr/wrap/SKILL.md`,
`config/agents/herdr/wrap/close-own-pane`, personal interactive/background closure rules.

**Supports:** closure preconditions as agent policy, owned-file saving, undertaker handoff,
result recording, same-machine home notification, own-pane close, conditional drawer cleanup.

**Limit:** the state command does not independently check those preconditions. The close script
does not validate acceptance; it must be called in the correct pane/session context.

## E-UNDERTAKER

**Sources:** `bin/ark-undertaker` discovery, `left`, `start`, `wait`, watcher marking and answer
paths; `config/agents/herdr/undertaker/SKILL.md`.

**Supports:** unfinished-agent ownership handoff, a background watcher intent, settled answers,
durable target notes, helper-only close, and unreadable-state distinctions.

**Limit:** the watcher is an agent and still needs correct interpretation, verification, and
personal escalation when required.

## E-STALLED

**Sources:** `bin/ark-stalled` functions `agent_here`, `look`, `check`, `prompt`, `tell`, `State`;
`config/stalled.env`; `config/systemd/ark-stalled.timer` and service; installer integration.

**Supports:** actual timed observation, background-only eligibility, five/five/60-minute defaults,
state-sequence tracking, recorded-before-send prompt, subsequent notification, no transcript read.

**Limit:** sample timing is approximate, the check depends on current state visibility, and it
does not solve all crashes, restart all processes, or provide quota.

## E-SYNC

**Sources:** `bin/ark-pull`, `bin/install-hooks`, `bin/install-agent-context`, and shared rules.

**Supports:** freshness reporting, protected update paths, automatic context installation after
relevant changes, staged OKF checks, narrow secret/session checks, and post-commit push attempts.

**Limit:** a hook's push attempt can fail. Shared-index ownership still matters, and a format
check is not a semantic or comprehensive privacy review.

## E-FLYWHEEL

**Sources:** the capture, reconciliation, dispatch, review, wrap, and context mechanisms above;
existing direction and operating history.

**Supports:** the described feedback pattern and its concrete carriers.

**Limit:** no single flywheel service or numerical throughput guarantee is asserted. The
distinction between mechanism, procedure, configuration, observation, and hypothesis is explicit.

## E-EXPERIMENTS

**Sources:** the historical intent 0143's intent/log/result-summary and current direction.

**Supports:** decision replay was an experiment and did not become deployed personal-decision
automation; the review judge remains planned.

**Limit:** private reports, datasets, transcripts, sensitive examples, and numerical findings
are not reproduced. No conclusion here turns experimental work into a production capability.

## How maintainers should update this evidence

Change a behavioral explanation only after inspecting the relevant implementation or observing
the deployed operation. Refresh source digests for the inspected units, note a new audit date,
and update the enforcement matrix when a policy becomes a code check or vice versa. If a
reconciliation schedule is later verified, document its trigger, execution environment, prompt
or command provenance, overlap/failure behavior, and bounded evidence. Do not fill that gap by
guessing from the existence of unrelated timers.
