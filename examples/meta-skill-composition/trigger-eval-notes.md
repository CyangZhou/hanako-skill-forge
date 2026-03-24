# Trigger Eval Notes

This note shows how `hanako-skill-forge` should treat trigger examples.

## Goal

Use `modules/review/18-触发评测样例集.md` as a calibration fixture:

- keep positive examples focused on skill engineering work
- keep negative examples focused on edits, bugs, browsing, and pure evaluation work
- review examples whenever `SKILL.md` description changes materially

## Important boundary

This repository stores trigger samples.

It does **not** claim to be the best place to run large-scale skill evals or benchmark experiments.
When executable evaluation is the real task, route that work into a dedicated skill-evaluation flow.
