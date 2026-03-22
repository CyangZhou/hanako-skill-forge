# Contributing

Thanks for considering a contribution to `hanako-skill-forge`.

This repository accepts improvements to:

- meta-skills and reusable skill patterns
- existing skill structure and routing rules
- templates and examples
- maintenance, extension, and recovery flows
- repository documentation and trust signals

## Before you contribute

Please make sure your change:

- has a clear purpose and scope
- makes the skill system easier to use, maintain, or verify
- keeps rules explicit instead of hidden in vague wording
- updates related documents when behavior or structure changes
- avoids adding scripts when documentation is enough

## Preferred contribution types

### 1. Improve an existing skill
Good contributions:
- clarify routing
- reduce redundant wording
- strengthen validation or maintenance paths
- improve templates or examples

### 2. Add a new reusable pattern
Good contributions:
- introduce a pattern that can be reused across multiple skills
- explain when it should and should not be used
- provide at least one minimal example

### 3. Improve repository trust and usability
Good contributions:
- improve onboarding docs
- add example flows
- improve changelog quality
- refine contribution or security guidance

## Skill contribution checklist

Before opening a pull request, verify:

- [ ] the skill or document has a clear purpose
- [ ] intended use cases are explicit
- [ ] boundaries / non-goals are documented
- [ ] inputs and outputs are described where relevant
- [ ] at least one example or concrete usage path is included when needed
- [ ] related docs are updated
- [ ] `python scripts/main.py --action audit_skill` passes when documentation changed

## Pull request guidance

A good pull request should include:

1. what changed
2. why it changed
3. affected files or modules
4. any behavior or structure impact
5. validation evidence

## What maintainers may reject

Pull requests may be rejected if they:

- add vague or decorative wording without execution value
- introduce overlapping module responsibilities
- hide behavior in scripts that should stay documented
- expand scope without a clear route, template, or validation path
- present agent behavior as guaranteed when it depends on runtime context

## Development note

This repository is documentation-first.

If a rule can be made clear with a document, template, or route, prefer that over adding code.

## Questions

If you are unsure whether an idea fits, open an issue first with:

- the problem you want to solve
- why current material is not enough
- the smallest useful change you have in mind
