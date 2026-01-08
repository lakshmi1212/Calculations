# Calculations

This repository provides basic math operations (addition and subtraction) with automated tests and CI integration.

## Usage

Import the `add` and `subtract` functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

result1 = add(2, 3)        # 5
result2 = subtract(5, 2)   # 3
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

## CI/CD

This project is designed for GitHub Actions CI. The workflow file is located at `.github/workflows/ci.yml`.

