# StateBind Guard Adoption Example

[![StateBind Guard](https://github.com/FU-max-boop/statebind-guard-adoption-example/actions/workflows/statebind-guard.yml/badge.svg)](https://github.com/FU-max-boop/statebind-guard-adoption-example/actions/workflows/statebind-guard.yml)

This repository is a minimal third-party-style adoption example for
[StateBind Guard](https://github.com/FU-max-boop/statebind-guard).

It proves the released GitHub Action can be consumed from another repository:

```yaml
- id: statebind
  uses: FU-max-boop/statebind-guard@v0.1.38
```

## What This Repo Demonstrates

- A committed `HANDOFF.md` and `statebind.json`.
- A bug-fix policy generated from the StateBind `bugfix` preset.
- A standard `.pre-commit-config.yaml` that pins the same public release.
- A workflow that runs the released StateBind Guard action from a separate repo.
- A workflow assertion that the action outputs `passed=true`, `errors=0`,
  `warnings=0`, and `exit_code=0`.
- Uploaded JSON, SARIF, Markdown, and HTML validation reports.

## Local Check

```bash
python -m unittest discover -s tests
```

If StateBind Guard is installed locally:

```bash
statebind validate statebind.json --repo . --policy .statebind-policy.json --fail-on warning
statebind doctor --repo . --policy .statebind-policy.json
```

## Why This Exists

The main StateBind Guard repository already tests `uses: ./` locally. This repo
is the separate-repository adoption receipt: it pins a public release, runs the
published composite action, and asserts the action outputs in CI.

The adoption surface mirrors the one-command bundle produced by:

```bash
statebind init --goal "Demonstrate StateBind Guard adoption from a separate repository." \
  --next-command "python -m unittest tests.test_demo.DemoTests.test_resume_selector" \
  --policy-out .statebind-policy.json \
  --pre-commit-config .pre-commit-config.yaml
```

## StateBind Contract

The handoff binds the focused failing-test role and next-command role to the
same exact selector:

```text
failing_test -> python -m unittest tests.test_demo.DemoTests.test_resume_selector
next_command -> python -m unittest tests.test_demo.DemoTests.test_resume_selector
```
