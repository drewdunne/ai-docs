# Command reference

[Home](../README.md) · [Reading guide](README.md) · [Next: enforcement](enforcement.md)

These are commands in the audited private ark-sdlc checkout, except explicitly named public
herdr/Kerdr interfaces. This documentation repository does not ship those executables.
`DIR` is an intent folder; `NNNN` is its allocated four-digit ID; `SESSION` is a configured
herdr session. Examples use fictional IDs. Read the command's output as well as its exit code.

## Claim and route

| Command | Effect | Important boundary |
|---|---|---|
| `bin/ark-pull` | Update from the central copy and record freshness | May refuse an unsafe/unavailable update; does not discard others' edits |
| `bin/ark-pull status` | Read last update outcome/freshness | Does not contact the central copy |
| `bin/ark-new-intent SLUG` | Allocate and publish an intent skeleton | Fill in and triage before work; an explicitly unclaimed local fallback is unresolved |
| `bin/ark-new-intent --priority high SLUG` | Claim with specified priority | Only when the person requested it |
| `bin/ark-new-intent --parent NNNN SLUG` | Claim a child skeleton | Explain why the parent needs it; dispatch with `--here` |
| `bin/ark-dispatch DIR [LABEL]` | Start according to lane, placement, and configuration | Requires intent and triage files; manual assessment is external |
| `bin/ark-dispatch --self DIR [LABEL]` | Adopt current pane, without starting another agent | Checks current ownership/capacity and updates association/name/pinboard |
| `bin/ark-dispatch --new DIR [LABEL]` | Deliberately request a new top-level placement | Does not override capacity or make a child independent |
| `bin/ark-dispatch --here DIR [LABEL]` | Supporting tab in current workspace | Helper label; no independent attention slot |
| `bin/ark-dispatch --background DIR [LABEL]` | Explicit autonomous lane | Own workspace in background; retain origin home |
| `bin/ark-dispatch --home SESSION DIR [LABEL]` | Name origin while allowing background triage | Cannot combine with `--session` |
| `bin/ark-dispatch --session SESSION DIR [LABEL]` | Explicit session placement | Suppresses automatic lane routing unless it names background |

Additional dispatch options include `--tab-in LABEL`, `--tab-label TEXT`, `--brief-extra FILE`,
`--env KEY=VALUE`, `--agent-settings FILE`, `--permission-mode MODE`, and `--effort LEVEL`.
Placement flags have compatibility constraints; [routing precedence](dispatch.md#routing-precedence)
is more reliable than treating them as independent toggles.

`--override` means the person authorized exceeding the soft interactive limit, up to the
configured maximum. `--no-wait` on **dispatch** means the person authorized starting before
prerequisites closed. Neither flag proves that authorization by itself.

Dispatch exit **3** means work was deferred/refused by an expected routing constraint such as
capacity or prerequisites. Startup errors generally exit nonzero and may leave an already
created placement; inspect before retrying.

## Lifecycle, priority, results, and dependencies

| Command | Output or mutation |
|---|---|
| `bin/ark-state get NNNN` | Tab-separated state and home |
| `bin/ark-state set NNNN STATE [--home H] [--by N]` | Set lifecycle/home/initiator; explicit nonclosed state reopens |
| `bin/ark-state list [--home H] [--state S] [--priority P] [--by-priority]` | Tab-separated number, state, home, priority, title |
| `bin/ark-state home [SESSION]` | This machine's `machine/session` identity |
| `bin/ark-state priority NNNN [LEVEL]` | Read priority or set the person's specified choice |
| `bin/ark-state touched NNNN` | Last substantive Git activity time, excluding recognized bookkeeping |
| `bin/ark-state result NNNN [LINE]` | Read result, or save one line plus today's completion date |
| `bin/ark-state results [--home H] [--days N]` | Recorded background results, newest first |
| `bin/ark-state waits-on NNNN [--all]` | Unfinished prerequisites, or all with `--all` |
| `bin/ark-state waits-on NNNN OTHER...` | Validate and save prerequisites; refuse missing IDs and cycles |
| `bin/ark-state waits-on NNNN none` | Remove prerequisites |

Allowed set states are `active`, `queued`, `shelved`, `background`, and `closed`. State commands
write narrow records and auto-commit when the target had no pre-existing edits; otherwise they
leave the edit for its owner and say so. `ARK_STATE_NO_COMMIT=1` disables their automatic commit
path. `closed` does not mechanically enforce the acceptance/friction invariant.
[Evidence: E-STATE](sources.md#e-state).

## Capacity and shelf

| Command | Purpose |
|---|---|
| `bin/ark-slots [--session SESSION] list` | Live slot holders: workspace, label, associated intent |
| `bin/ark-slots [--session SESSION] count [--except WORKSPACE]` | Current interactive slot count |
| `bin/ark-slots limits` | Configured default and maximum |
| `bin/ark-shelf [SESSION]` | Workspaces, queued/shelved work, background runs, recent results |
| `bin/ark-shelve pick` | Candidate other intent, lowest priority first, then least recent substantive commit |
| `bin/ark-shelve ask WHICH [--note TEXT] [--wait [SECONDS]]` | Ask the other intent's own agent to shelve; optionally wait |
| `bin/ark-shelve [NNNN]` | Own final shelving step after prepared/committed resume record |

Shelving policy requires finished work saved and a useful `resume.md`. The own-shelving command
records conversation recovery information when available, marks shelved, notifies, and closes
its own workspace after a delay. It is broader than wrap's own-pane close, so apply the correct
skill to the correct intent. No tool should close someone else's workspace merely to free space.

## Pinboard and history

```sh
bin/ark-pin NNNN story "As a user I want an actionable error so that I can recover."
bin/ark-pin NNNN message "The fix is implemented. Verification is running."
bin/ark-pin NNNN block "The required service is unavailable."
bin/ark-pin NNNN unblock all
bin/ark-pin NNNN status under-way
bin/ark-pin NNNN status waiting Andrew
bin/ark-pin NNNN status waiting "external review"
bin/ark-pin NNNN show
bin/ark-pin NNNN render /tmp/example-note.md
bin/ark-pin refresh-all NNNN
bin/ark-okf log intents/NNNN-slug/log.md "What changed and how it was checked."
```

`ark-pin --session NAME --workspace ID ...` explicitly targets another location. Status has
lifecycle/blocker/dependency precedence; do not try to manually set Done or Queued. `ark-okf log`
adds history but does not itself establish remote publication. [Evidence: E-PIN, E-OKF](sources.md#e-pin).

## Friction and wins

| Command | Purpose and boundary |
|---|---|
| `friction/preflight.sh` | Run every detector under timeout 15; nonzero only for failing open toil |
| `bin/ark-friction find WORDS...` | Search related entries, favoring open matches |
| `bin/ark-new-friction SLUG` | Allocate/publish skeleton; agent fills the evidence |
| `bin/ark-friction case F-NNNN [OPTIONS] TEXT` | Append/publish a case, reopening remediated entries on ordinary recurrence |
| `bin/ark-friction check` | Hook JSON on stdin; emit cue-based reminder context, not a case or dispatch |
| `bin/ark-win draft` | Print a structured draft |
| `bin/ark-win record SLUG FILE` | Validate, allocate, publish a win; `-` reads stdin |
| `bin/ark-win find WORDS...` | Search positive evidence |
| `bin/ark-win list [--json]` | List records, with headers in JSON for analysis |

Case options are `--missed`, `--past`, `--intent NNNN`, and `--id ID`. The command prints its
publication outcome. A local-only case result exits 3. Capture commands have secret-pattern
screening, not a general privacy guarantee. The agent remains responsible for safe wording.
[Evidence: E-FRICTION, E-WINS](sources.md#e-friction).

## Independent review

```sh
bin/ark-code-review DIR [FILES...] --repo CODE-REPO --diff CHANGE --no-wait
bin/ark-code-review status RUN-ID
bin/ark-code-review wait --timeout 60 RUN-ID
bin/ark-design-review DIR [DESIGN-FILE] [EXTRA-FILES...]
```

Code review accepts multiple `--diff` selections, `--diff-file FILE`, `--what TEXT`, and review
configuration options. `CHANGE` can be a commit, range, or `worktree`. Name untracked new files
explicitly. `--no-wait` on **review** starts/returns without a long wait and refuses to wait for
a quota reset; it is unrelated to dispatch's dependency bypass.

Review exits are 0 completed, 1 runner error, 2 failed, 3 quota, 4 could not review, 5 still
running. Use its own wait protocol. [Review details](reviews.md).

## Recovery and handoff

| Command | Role |
|---|---|
| `bin/ark-stalled list` | Observe eligible background agents and predicted action without prompting |
| `bin/ark-stalled check` | Perform recovery prompt/notification according to recorded state |
| `bin/ark-stalled status` | Check observer freshness, with environment-specific no-manager/no-herdr handling |
| `bin/ark-stalled install`, `setup`, `off`, `on` | Manage the machine's observer timer |
| `bin/ark-undertaker left NNNN` | List started/child/helper work the wrapping intent leaves |
| `bin/ark-undertaker start NNNN` | Establish a watcher when needed; otherwise report nothing remains |
| `bin/ark-undertaker wait --timeout S [TARGET...]` | Watch until a target changes/stops or timeout; timeout exits 3 |
| `bin/ark-undertaker hold`, `release` | Maintain watched-pane ownership marks |
| `bin/ark-undertaker read TARGET [LINES]` | Read target output |
| `bin/ark-undertaker answer TARGET TEXT` | Prompt with settled information and log the answer |
| `bin/ark-undertaker close TARGET` | Close a finished helper; not an intent's own agent |

The undertaker skill controls how these tools are used. Completion of the parent does not
license abandoning a child. Its watcher remains responsible until delivery or a genuine
personal decision. [Evidence: E-UNDERTAKER, E-STALLED](sources.md#e-undertaker).

## Boards, prompts, and finishing

`bin/ark-cards --pretty` emits the feed. `bin/ark-card-action` reads one JSON action from stdin
and returns a JSON response. They are the private adapter; public Kerdr usage and the contract
are documented [in Kerdr](https://github.com/drewdunne/kerdr/blob/main/docs/feed.md).

The public `kerdr report` command writes workspace status tokens; it does not by itself create
an intent. `herdr agent prompt PANE TEXT` sends a message through the agent interface instead of
typing into whatever focused terminal happens to exist. Important cross-agent notes also go
in the receiving intent's durable log.

Wrap is a skill, not just `ark-state set closed`. Its last command is
`config/agents/herdr/wrap/close-own-pane TITLE LINE`, after checks, handoff, result, log, and
owned-file publication. Background work notifies its home and closes automatically; interactive
work waits for the person's wrap request. [Completion protocol](background.md#completion-is-an-explicit-protocol).
