# Calculations

This repository provides basic math operations (addition and subtraction) implemented in Python.

## Usage

Import the functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

result = add(2, 3)
print(result)  # Output: 5

result = subtract(5, 2)
print(result)  # Output: 3
```

## Testing

Tests are located in the `tests/` folder. Run all tests using:

```
python -m pytest tests/ -v --tb=short
```

## CI Workflow

Continuous Integration is configured via `.github/workflows/ci.yml` to automatically run tests on push and pull request events.
