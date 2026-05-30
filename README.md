# StateBind Guard Adoption Example

[![StateBind Guard](https://github.com/FU-max-boop/statebind-guard-adoption-example/actions/workflows/statebind-guard.yml/badge.svg)](https://github.com/FU-max-boop/statebind-guard-adoption-example/actions/workflows/statebind-guard.yml)

This repository is a minimal third-party-style adoption example for
[StateBind Guard](https://github.com/FU-max-boop/statebind-guard).

It proves the released GitHub Action can be consumed from another repository:

```yaml
- id: statebind
  uses: FU-max-boop/statebind-guard@v0.1.13
```

## What This Repo Demonstrates

- A committed `HANDOFF.md` and `statebind.json`.
- A bug-fix policy generated from the StateBind `bugfix` preset.
- A workflow that runs the released StateBind Guard action from a separate repo.
- A workflow assertion that the action outputs `passed=true`, `errors=0`,
  `warnings=0`, and `exit_code=0`.
- Uploaded JSON, SARIF, Markdown, and HTML validation reports.

## Local Check

```bash
python -m unittest discover -s tests
```

## Why This Exists

The main StateBind Guard repository already tests `uses: ./` locally. This repo
is the separate-repository adoption receipt: it pins a public release, runs the
published composite action, and asserts the action outputs in CI.

## StateBind Contract

The handoff binds the focused failing-test role and next-command role to the
same exact selector:

```text
failing_test -> python -m unittest tests.test_demo.DemoTests.test_resume_selector
next_command -> python -m unittest tests.test_demo.DemoTests.test_resume_selector
```
