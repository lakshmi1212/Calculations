# Calculations

This repository provides basic math operations and their tests.

## Usage

The `src/math_operations.py` module includes:
- `add(a, b)`: Adds two numbers.
- `subtract(a, b)`: Subtracts second number from first.

## Running Tests

All tests are located in the `tests/` folder.
Run tests using:

```
python -m pytest tests/ -v --tb=short
```

## CI/CD

A workflow file is expected at `.github/workflows/ci.yml` for automated test runs on push and pull request events.

## Requirements

See `default/requirements.txt` for dependencies.
