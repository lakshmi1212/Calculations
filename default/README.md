# Calculations

This repository provides basic math operations (addition and subtraction) with comprehensive automated tests and CI/CD integration.

## Usage

```
from src.math_operations import add, subtract

result_add = add(2, 3)
result_subtract = subtract(5, 2)
```

## Running Tests

Install dependencies:
```
pip install -r default/requirements.txt
```

Run all tests:
```
pytest tests/ -v --tb=short
```

## CI/CD

Automated workflows are configured in `.github/workflows/ci.yml` to run tests on every push and pull request to `main`.

## File Structure
- src/math_operations.py: Business logic for math operations
- tests/test_add.py: Unit tests for addition
- tests/test_subtract.py: Unit tests for subtraction
- default/requirements.txt: Python dependencies
- default/math.json: CI/CD metadata
