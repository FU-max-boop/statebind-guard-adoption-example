# Agent Handoff

## Task

- Goal: Demonstrate StateBind Guard adoption from a separate repository.
- Current status: Ready for CI validation.

## Active Target

- Type: test
- Handle: python -m unittest tests.test_demo.DemoTests.test_resume_selector
- Evidence: This repository uses a focused unit test as the smallest adoption proof.
- Confidence: high

## Executable Bindings

| Role | Handle | Evidence | Confidence | Risk |
|---|---|---|---|---|
| failing_test | `python -m unittest tests.test_demo.DemoTests.test_resume_selector` | Focused validation command for the demo behavior. | high | |
| next_command | `python -m unittest tests.test_demo.DemoTests.test_resume_selector` | Smallest command a resumed agent should run before broader checks. | high | |

## Next Action

1. Run the focused test selector.
2. Confirm StateBind Guard passes in GitHub Actions.
3. Use this repository as an external adoption receipt.

## Risks And Ambiguities

- This is a minimal adoption example, not a production application.

## Resume Prompt

> Verify `statebind.json`, then run the bound `next_command` before editing.

