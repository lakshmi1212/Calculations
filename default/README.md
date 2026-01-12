# Calculations

This repository provides basic math operations (addition and subtraction) implemented in Python, along with comprehensive pytest-based test coverage and CI/CD workflow integration.

## Usage

```python
from src.math_operations import add, subtract

result_add = add(2, 3)
result_subtract = subtract(5, 2)
```

## Running Tests

Install dependencies:

```bash
pip install -r default/requirements.txt
```

Run all tests:

```bash
pytest tests/ -v --tb=short
```

## CI/CD Workflow

The repository includes a GitHub Actions workflow file at `.github/workflows/ci.yml` to automate testing on each push or pull request to the `main` branch.
