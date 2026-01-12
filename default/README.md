# Calculations

A simple Python project for basic math operations (addition and subtraction) with automated tests and CI workflow.

## Usage

- Source code: `src/math_operations.py`
- Add: `add(a, b)`
- Subtract: `subtract(a, b)`

## Running Tests

```bash
python -m pytest tests/ -v --tb=short
```

## Continuous Integration

The CI workflow is defined at `.github/workflows/ci.yml` and runs tests on every push and pull request to `main`.

## Requirements

- Python 3.10
- pytest

## Folder Structure

- `src/` : source code
- `tests/` : test files
- `default/` : meta files and documentation
