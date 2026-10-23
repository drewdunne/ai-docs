# Handbook reading guide

[Home](../README.md)

The chapters describe the system inspected on 2026-10-23. Commands belong to the private
ark-sdlc checkout unless explicitly identified as public Kerdr commands. They are reference
material, not a claim that installing this documentation installs the framework.

| Chapter | Questions it answers |
|---|---|
| [Overview](overview.md) | What happens after an outcome is stated? What actually runs? |
| [Intents and triage](intents.md) | What is recorded? Who decides proceed, escalate, or review? |
| [State and formats](data-model.md) | Which fields are authoritative? How do the files relate? |
| [Dispatch routing](dispatch.md) | Which workspace, session, lane, and agent receive the work? |
| [Autonomous background lane](background.md) | How does work finish, ask, recover, and hand off? |
| [herdr, pinboards, and Kerdr](visibility.md) | How does a person see what needs attention? |
| [Friction capture](friction.md) | What counts as an intervention? What do hooks really do? |
| [Friction reconciliation](reconciliation.md) | How do records turn into owned, checked improvements? |
| [Improvement flywheel](flywheel.md) | What compounds? What remains a hypothesis or experiment? |
| [Reviews and verification](reviews.md) | How are claims, changes, and completion checked? |
| [Failure and recovery](recovery.md) | What happens when dependencies, quotas, tools, or agents fail? |
| [Worked examples](examples.md) | What do complete runs look like, including unhappy paths? |
| [Command reference](commands.md) | Which commands read, mutate, publish, or close things? |
| [Policy versus code](enforcement.md) | Which guarantees are implemented, and which rely on agents? |
| [Source evidence](sources.md) | Which source units support each explanation? |
| [Publication verification](verification.md) | What was checked for this handbook, and what was not? |
| [Glossary and adaptation](glossary.md) | What do the terms mean? What can someone reuse? |

Every technical chapter links to evidence IDs in the [source map](sources.md). Private source
paths there are audit locators, written as code, not inaccessible hyperlinks masquerading as
public references. [Examples](../examples/README.md) are safe, invented records. Mermaid diagrams
describe the audited behavior; arrows representing agent actions are labeled accordingly.
