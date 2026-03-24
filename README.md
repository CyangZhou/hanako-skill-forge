# hanako-skill-forge

A minimal meta-skill repository for building, refactoring, maintaining, extending, and recovering long-lived Hanako / OpenHanako skills.

## What it is

`hanako-skill-forge` is a documentation-first meta-skill for turning loose prompts, scattered workflow notes, and half-structured skill assets into skills that are:

- easier to understand
- easier to maintain
- easier to extend
- easier to recover when they drift or break

It is designed for skill authors who want **clear routes, explicit boundaries, reusable templates, and minimal audit tooling** instead of vague prompt piles.

## Why this repository exists

Many skill repositories become hard to trust over time:

- entry files keep growing
- the real source of truth becomes unclear
- fixes are made in one place and forgotten in another
- scripts silently become the hidden brain of the system
- recovery paths are missing, so the same problems keep coming back

`hanako-skill-forge` exists to solve that.

Its core idea is simple:

> make the skill thinner, and make the maintenance path stronger.

That means:

1. define the skill’s purpose and route first
2. keep documentation as the main source of truth
3. add scripts only when audit or closure truly needs them
4. preserve formal paths for maintenance, extension, and recovery

## Who it is for

This repository is useful if you are:

- building skills for Hanako / OpenHanako
- standardizing an internal skill library
- refactoring older skills into a clearer structure
- turning prompts or workflow notes into reusable skill assets
- trying to make skill behavior easier to review and maintain

## Who it is not for

This repository is **not** intended as:

- a generic prompt dump
- a hosted agent runtime
- a guarantee of runtime safety in every environment
- a replacement for platform-specific permission or security design

## Design principles

- **Documentation first** — rules, routes, templates, and acceptance live in documents
- **Scripts second** — scripts audit, verify, and close gaps; they do not become the hidden controller
- **Single source of truth** — core rules should have one clear home
- **Minimal by default** — keep only wording that directly improves execution or maintenance
- **Explicit evolution paths** — maintenance, extension, and recovery are formal change routes, not always-on runtime behavior
- **Acceptance before completion** — if it has not been checked, it is not done

## Repository structure

```text
hanako-skill-forge/
  SKILL.md                 # skill entry: capability, route, discipline
  guides/                  # principles and design mapping
  modules/
    route/                 # intake and control routing
    research/              # benchmarking and capability injection
    build/                 # architecture and implementation rules
    maintenance/           # maintenance and health checks
    extension/             # extension rules and boundaries
    recovery/              # recovery and healing path
    review/                # acceptance and release rules
    templates/             # structured templates
  scripts/
    main.py                # minimal audit / closure helper
  schemas/
    actions_contracts.json # structured action contract
  examples/                # starter examples
```

## How it works

The main route priority is:

**recovery > maintenance > extension > new build / refactor**

In plain words:

- repair broken things first
- then close structural drift
- then extend what is missing
- only then do larger rebuild work

Typical entry order:

1. read `modules/route/02-需求卡协议.md`
2. read `modules/route/01-总控路由.md`
3. continue only into the branch that matches the task
4. read templates only when needed
5. use trigger samples when calibrating description boundaries
6. run scripts only when audit or closure is needed

## What you can do with it

### Build a new skill
Turn a vague idea or loose workflow into a structured skill.

### Refactor an old skill
Reorganize a skill whose entry, routing, and rules have drifted apart.

### Add a maintenance path
Make a skill easier to inspect, update, and keep consistent over time.

### Add an extension path
Expand capability without letting modules overlap or become ambiguous.

### Add a recovery path
Create a repeatable way to diagnose and repair drift, broken references, and documentation/script mismatch.

## Included modules

### `route`
Defines how to intake a task and route it into the correct branch.

### `research`
Maps reusable capability from existing local skills, current repository assets, and selected open-source references.

### `build`
Defines structure, layering, and when documentation is enough versus when a script is justified.

### `maintenance`
Keeps references, terminology, and module responsibilities consistent.

### `extension`
Adds new capability without breaking the current structure.

### `recovery`
Provides failure categories, recovery loops, retry discipline, and post-fix validation.

### `review`
Defines acceptance, release, evidence, and trigger calibration material.

### `templates`
Provides reusable templates for requirement cards, blueprints, maintenance checks, recovery notes, status tracking, checkpoints, and delivery summaries.

## Quick start

### Option 1 — use the meta-skill as designed
Start from `SKILL.md`, follow the route, and only read the branch you need.

### Option 2 — run the audit helper directly
From the repository root:

```bash
python scripts/main.py --action module_index
python scripts/main.py --action audit_refs
python scripts/main.py --action audit_terms
python scripts/main.py --action audit_skill
```

### What these commands do

- `module_index` — list modules and roles
- `audit_refs` — check broken Markdown references
- `audit_terms` — detect leftover terms and bad smells
- `audit_skill` — run an overall repository health check, including action contract alignment

## Examples

Starter examples are provided in:

- `examples/minimal-skill/`
- `examples/meta-skill-composition/`

These examples are intentionally small. Their job is to show how to think about skill shape and boundaries, not to act as production guarantees.

## Compatibility note

This repository focuses on **skill structure, documentation discipline, and maintenance patterns**.

Actual compatibility depends on:

- the target agent runtime
- the host platform’s tool model
- permission boundaries
- how the surrounding system injects context and tools

## Project status

**Active early-stage project.**

The repository is already usable as a meta-skill and reference asset, but wording, conventions, and examples may continue to evolve before a stable `1.0.0`.

## Trust and safety notes

Skills and meta-skills can influence agent behavior, orchestration flow, and tool usage.

Before using this repository in production or sensitive contexts, review:

- intended scope
- assumptions and non-goals
- runtime permission boundaries
- host integration behavior

Using content from this repository does **not** automatically make an agent or workflow safe.

## Open-source references

This repository absorbs useful capability from selected open-source workflow and specification projects, including ideas around:

- specification-first design
- structured change flow
- progressive skill layering
- maintenance and recovery discipline
- reusable validated patterns

The goal is not to copy their wording, but to absorb what improves structure, maintainability, and trust.

## Recommended GitHub About copy

**Description**

> A minimal meta-skill repository for building, refactoring, maintaining, extending, and recovering long-lived Hanako/OpenHanako skills.

**Suggested Topics**

- `hanako`
- `openhanako`
- `ai-agent`
- `agent-skill`
- `meta-skill`
- `prompt-engineering`
- `orchestration`
- `workflow`
- `developer-tools`
- `knowledge-management`

## Repository guide

- `README.md` — project overview and public onboarding
- `SKILL.md` — skill entry and operational route
- `schemas/actions_contracts.json` — script action contract
- `CHANGELOG.md` — notable public changes
- `CONTRIBUTING.md` — how to contribute responsibly
- `SECURITY.md` — how to report security concerns
- `LICENSE` — usage rights

## License

Released under the [MIT License](./LICENSE).
