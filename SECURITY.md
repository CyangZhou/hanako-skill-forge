# Security Policy

If you believe this repository contains a pattern, example, or instruction that could introduce a meaningful security risk, please report it privately.

## What to report

Relevant reports include issues such as:

- unsafe tool-use patterns
- prompt injection amplification paths
- misleading orchestration guidance
- hidden assumptions that could cause unsafe automation
- examples that encourage insecure deployment or permission handling
- data leakage or sensitive-context handling risks in skill design

## How to report

Please avoid public disclosure before maintainers have had a chance to review the issue.

If possible, include:

- affected file(s)
- a short description of the risk
- realistic impact
- reproduction or misuse path
- a safer alternative, if available

## Scope note

This repository provides reusable skill patterns, templates, and maintenance guidance.

Safe use still depends on the surrounding runtime, permission model, tool boundary, host integration, and deployment context.

Using material from this repository does **not** automatically make an agent or workflow secure.

## Supported versions

At this stage, only the latest state of the `main` branch is considered supported for security fixes and clarifications.
