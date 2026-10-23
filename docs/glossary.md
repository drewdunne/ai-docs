# Glossary and adapting the pattern

[Home](../README.md) · [Reading guide](README.md)

| Term | Meaning in this handbook |
|---|---|
| Acceptance criteria | Observable conditions that define delivery for an intent |
| Agent | The worker interpreting the request and using tools within its authority |
| ark-sdlc | The private file/command/instruction workflow described here |
| Background lane | A herdr session for work that can finish without ongoing personal involvement |
| Case | One occurrence appended to a recurring friction entry |
| Child intent | Supporting work explicitly related to a parent; runs in a helper tab |
| Dependency | An intent that must close before another starts; represented by `waits_on` |
| Dispatch | Placement/startup of work after intake and manual triage |
| Epic win | Structured evidence that a result worked especially well for the person |
| Flywheel | Repeated evidence-to-improvement-to-better-work feedback pattern |
| Friction | A recorded intervention or manual checkpoint, classified as toil or gate |
| Gate | An intentional human checkpoint to retain and make inexpensive |
| Helper | A supporting agent/pane, distinct from the top-level conversation |
| herdr | The terminal environment hosting sessions, workspaces, tabs, panes, and agents |
| Home | The machine/session an intent belongs to and reports back to |
| Intent | Durable desired work with scope, criteria, lifecycle, and history |
| Kerdr | The public board/cockpit combining records and herdr workspace state |
| Lane | Triage's assessment of whether work can finish autonomously or needs interaction |
| OKF | Open Knowledge Format; conventions for typed Markdown knowledge records |
| Pinboard | Concise workspace orientation and a fuller note, kept current by the worker |
| Preflight | Detector execution before work; its aggregate exit has specific open-toil semantics |
| Reconciliation | Agent investigation connecting friction evidence to ownership and checked remedies |
| Review judge | Planned triage automation; manual triage currently operates |
| Shelf | Session-oriented view of active, queued, shelved, background, and recently finished work |
| Shelve | Save work and a resume record, mark it set aside, and free its workspace |
| Stage | A board column such as Build or Test, separate from lifecycle |
| State | The intent's recorded operational lifecycle such as queued/background/closed |
| Toil | Avoidable manual work the system should remove |
| Undertaker | An agent that owns watching unfinished agents when their initiating worker wraps |
| Wrap | Verify and save completion, hand off ownership, notify, and close the own pane last |

## What another person can reuse

Start with the smallest complete loop: an outcome record, manual triage, a worker, evidence of
delivery, and a way to record interventions. Make those records easy to find before increasing
the number of concurrent agents. The distinction between work that needs attention and work
that can finish alone is useful even without this exact terminal setup.

The public [Kerdr project](https://github.com/drewdunne/kerdr) can consume a different tracker
through a JSON feed and optional action backend. This handbook's [examples](../examples/README.md)
illustrate the records but do not implement the private allocator, dispatcher, or recovery tools.
Readers should not expect to clone `ai-docs` and obtain a complete running ark-sdlc installation.

Useful adaptations preserve the boundaries rather than merely the vocabulary:

- Separate lifecycle, stage, attention, and process state.
- Distinguish intentional decisions from avoidable manual work.
- Make repeated mechanics commands with explicit failure outputs where practical.
- Preserve ownership when a primary worker ends before its supporting agents.
- Test a remedy against the old failure and let recurrence challenge remediation.
- Record unavailable evidence instead of promoting plans or experiments to deployed behavior.

Those are descriptions of transferable lessons, not a proposal to replace the audited system.
The [MIT license](../LICENSE) permits reuse of the newly written handbook and examples. It does
not grant rights to private source, operational records, or other projects; public companion
projects carry their own licenses.
