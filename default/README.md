# Calculations

This repository provides basic math operations (addition, subtraction) in Python.

## Usage

Import functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

print(add(2, 3))       # Output: 5
print(subtract(5, 2))  # Output: 3
```

## Testing

Tests are located in the `tests/` folder. Run all tests with:

```bash
pytest tests/ -v --tb=short
```

## CI/CD

A GitHub Actions workflow is defined in `.github/workflows/ci.yml` to automate test runs on push and pull requests.
