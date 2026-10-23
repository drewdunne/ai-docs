# How I work with coding agents

I state an outcome. An agent records it as an **intent**, decides how much of my attention it
needs, carries out the work, and checks the result. When I have to step in, that becomes
**friction**: evidence for improving the tools and instructions that run the next job.

**[Kerdr](https://github.com/drewdunne/kerdr)** is the public kanban cockpit over
[herdr](https://herdr.dev/) that makes this work visible across agent sessions.
[Get Kerdr](https://github.com/drewdunne/kerdr#install) ·
[Kerdr's MIT license](https://github.com/drewdunne/kerdr/blob/main/LICENSE)

This repository is a retrospective handbook of my existing **ark-sdlc** workflow, audited on
**2026-10-23**. It contains newly written documentation and fictional examples, rather than the
private framework or its operational records. The handbook is [MIT licensed](LICENSE).

## Read it in layers

- **Five minutes:** [the system at a glance](docs/overview.md).
- **Understand the machinery:** [intents and triage](docs/intents.md),
  [state and file formats](docs/data-model.md), [dispatch](docs/dispatch.md), and
  [the autonomous lane](docs/background.md).
- **Understand the improvement loop:** [friction capture](docs/friction.md),
  [reconciliation](docs/reconciliation.md), and [the flywheel](docs/flywheel.md).
- **Operate and inspect it:** [herdr and Kerdr](docs/visibility.md),
  [reviews and verification](docs/reviews.md), [recovery](docs/recovery.md),
  [worked examples](docs/examples.md), and [command reference](docs/commands.md).
- **Check the boundaries:** [policy versus code](docs/enforcement.md),
  [source evidence](docs/sources.md), [publication checks](docs/verification.md), and
  [glossary and adaptation](docs/glossary.md).

Manual triage is operating today. The review judge is planned. A historical decision-replay
experiment did **not** become deployed decision automation. Friction reconciliation is agent-led;
its scheduling cadence was not independently established. These distinctions recur throughout
the handbook because they affect what the system can actually promise.

[Full reading guide](docs/README.md)
