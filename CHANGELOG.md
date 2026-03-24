# Changelog

All notable changes to this project will be documented in this file.

This project follows a simple human-readable changelog style inspired by Keep a Changelog.

## [0.2.0] - 2026-03-24
### Added
- Trigger-boundary guide for separating `hanako-skill-forge` from neighboring meta-skills
- Evidence and evaluation protocol for status, checkpoints, and validation traces
- Task status and checkpoint templates for long-running skill work
- Trigger sample set for should-trigger / should-not-trigger calibration
- Stronger action contract schema for script action definitions

### Changed
- Rewrote `SKILL.md` descriptor and entry discipline around routing, evidence, and boundary clarity
- Upgraded acceptance rules to include structure, behavior, and evidence layers
- Extended repository docs to mention trigger calibration and action contract alignment
- Upgraded `scripts/main.py` to enforce allowed actions and audit action-contract consistency

### Notes
- This release strengthens the repository as an engineering meta-skill, not just a documentation pattern library.
- Trigger samples are documentation fixtures first; if you want executable evals, pair this repository with a skill-evaluation flow.

## [0.1.0] - 2026-03-22
### Added
- Initial public repository structure for `hanako-skill-forge`
- Core meta-skill entry file and modular documentation
- Maintenance, extension, recovery, and review routes
- Minimal audit script for references, terms, and overall skill health
- Public-facing repository documents: README, LICENSE, CONTRIBUTING, SECURITY
- Starter examples for minimal skill use and repository maintenance flow

### Changed
- Reframed repository wording for public open-source consumption
- Clarified repository purpose, scope, and recommended GitHub About copy

### Notes
- This is the first public release of the repository.
- The repository is usable now, but conventions may continue to evolve before a stable `1.0.0`.
