# Policy versus code: what is actually enforced

[Home](../README.md) · [Reading guide](README.md) · [Next: source evidence](sources.md)

The workflow deliberately mixes instructions, skills, commands, and human decisions. Calling all
of it “automation” obscures important boundaries. This table distinguishes what code checks
from what an agent must do correctly.

| Rule or behavior | Concrete mechanism | Remaining policy/judgment boundary | Evidence |
|---|---|---|---|
| Start work with an intent | Allocator claims IDs and publishes skeletons | Agent must recognize requests, fill criteria, and not begin without a valid claim | [E-CLAIM](sources.md#e-claim) |
| Triage before work | Dispatcher requires a triage file and consults lane | Agent manually answers questions and respects proceed/escalate/review; no deployed judge | [E-TRIAGE](sources.md#e-triage) |
| Preserve user priority | State reader/writer supports three levels and lists sort accordingly | Only the person decides the priority; the CLI cannot prove who asked | [E-STATE](sources.md#e-state) |
| Do not start before prerequisites | Dependency validation and dispatcher refusal | `--no-wait` is authorized by the person, not justified by the flag existing | [E-DISPATCH](sources.md#e-dispatch) |
| Keep interactive work bounded | Session lock, live slot count, soft/hard ceilings | Person authorizes override; agents choose the correct lane instead of evading limits | [E-SLOTS](sources.md#e-slots) |
| One top-level conversation per workspace | Placement checks, `--self`, child `--here` restriction | Agent understands whether work is independent or supporting | [E-DISPATCH](sources.md#e-dispatch) |
| Do autonomous work out of the attention queue | Background session, origin home, dispatch brief/settings | Agent must correctly assess ongoing interaction needs and finish | [E-DISPATCH](sources.md#e-dispatch) |
| Keep progress visible | Pinboard renderer, status precedence, feed | Agent supplies accurate, current messages | [E-PIN](sources.md#e-pin) |
| Capture unsolicited interventions | Cue hook, search/case/claim commands | Agent decides whether it was stepping in and actually records it | [E-FRICTION](sources.md#e-friction) |
| Attribute friction accurately | Cases accept supplied text; personal rule specifies metadata | Agent must record known provider/app/model/effort and avoid guessing | [E-PERSONAL](sources.md#e-personal) |
| Reopen a failed remedy | Normal case append reopens remediated entries | Agent identifies genuine recurrence; does not misuse `--past` | [E-FRICTION](sources.md#e-friction) |
| Check friction detectors | Preflight runs every detector under timeout and prints rows | Agent interprets relevance and detector quality | [E-PREFLIGHT](sources.md#e-preflight) |
| Keep closure free of unresolved toil | Wrap skill's explicit precondition | `ark-state closed` does not check friction or acceptance | [E-WRAP](sources.md#e-wrap) |
| Get another perspective | Review runner, quota checks, preserved result | Agent chooses appropriate scope, reads the result, and fixes valid findings | [E-REVIEW](sources.md#e-review) |
| Complete background work automatically | Result fields, wrap skill, close script, home notification | Agent must invoke the finishing protocol after actual completion | [E-WRAP](sources.md#e-wrap) |
| Continue watching unfinished agents | Undertaker discovery, records, watcher marks, wait tool | Watcher agent must interpret questions and verify delivery | [E-UNDERTAKER](sources.md#e-undertaker) |
| Recover certain stopped turns | Versioned stalled-agent timer and state logic | Narrow eligibility, no universal process restart or quota repair | [E-STALLED](sources.md#e-stalled) |
| Turn friction into improvements | Existing agent-led procedure using normal intake and dispatch | No dedicated reconciler/schedule established; judgment and ownership remain essential | [E-RECONCILIATION](sources.md#e-reconciliation) |
| Keep records well formed | Shared YAML reader and staged OKF check | Well-formed text can still be wrong | [E-OKF](sources.md#e-okf) |
| Keep public explanations private-data-free | Deliberate source selection and publication checks | Pattern scanning is incomplete; an agent must understand what is sensitive | [Publication checks](verification.md) |

## Three misleading shortcuts

**“The intent is closed, therefore all its friction is fixed.”** Code does not establish that
implication. The agent should check the closure invariant before setting the state. The board
will still display a record closed incorrectly.

**“Preflight passed, therefore every detector passed.”** Its aggregate exit ignores failing
gates and failing remediated/accepted entries. Read the rows. Conversely, unrelated open toil
can make the shared suite exit nonzero without blocking a particular publication.

**“The diagram has an arrow from friction to dispatch, therefore a daemon schedules it.”** That
arrow represents agent-led reconciliation and ordinary dispatch. A specific trigger/cadence
needs separate evidence. The actual stalled-agent timer performs a different job.

## Authority is not supplied by configuration alone

A permissive agent runtime makes commands possible. It does not settle whether a public post,
deployment, destructive change, password operation, or personal decision was authorized. The
task, established instructions, and explicit decisions supply that boundary. The public handbook
does not publish live credentials or production configuration and does not grant readers access
to the private system.

This separation makes failure analysis more productive. If a lock is missing, repair code. If
the person never authorized a bypass, a stronger lock on the bypass flag would not explain the
agent's decision. If instructions are ignored, asserting that the words exist in a file is not
evidence of behavioral reliability.
