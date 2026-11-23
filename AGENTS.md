# AGENTS.md

## Project purpose

Expense Calculator is a small Python application that stores expenses,
calculates totals by category, and calculates the total amount of all expenses.

## Architecture

- `expense_calculator.py`: core expense logic.
- `test_expense_calculator.py`: unit tests.
- `README.md`: project documentation.

## Setup

```bash
python3 -m unittest -v
```

## Safe commands

```bash
python3 -m unittest -v
```

## Coding conventions

- Use clear function and variable names.
- Keep business logic separate from user-interface code.
- Add or update tests for changed behavior.
- Do not introduce dependencies without approval.

## Test expectations

All tests must pass before changes are accepted.

## Forbidden actions

- Do not commit secrets, API keys, passwords, or real personal or financial data.
- Do not deploy to production.
- Do not run destructive commands.
- Do not change dependencies without human review.
- Do not modify files outside the approved task scope.

## Review gates

All AI-generated changes must be reviewed by a human before merging.
