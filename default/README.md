# Calculations

This repository provides basic math operations (addition and subtraction) and comprehensive pytest-based test coverage.

## Usage

Import functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract
print(add(2, 3))      # Output: 5
print(subtract(5, 3)) # Output: 2
```

## Run Tests

Install dependencies:
```bash
pip install -r default/requirements.txt
```

Run all tests:
```bash
pytest tests/ -v --tb=short
```

## CI Workflow

See `.github/workflows/ci.yml` for automated test execution on push and pull request to `main`.
