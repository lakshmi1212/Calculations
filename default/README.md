# Calculations

This repository provides basic math operations with Python functions for addition and subtraction.

## Usage

- Source code is in `src/math_operations.py`
- Tests are in `tests/` folder and can be run using pytest

## Running Tests

Install dependencies:

```bash
pip install -r default/requirements.txt
```

Run tests:

```bash
pytest tests/ -v --tb=short
```

## CI/CD Workflow

The CI workflow runs all tests in the `tests/` directory using GitHub Actions. See `.github/workflows/ci.yml` for details.
