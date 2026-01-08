# Calculations

This repository provides basic math operations (addition and subtraction) implemented in Python.

## Usage

Import the functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

print(add(2, 3))       # Output: 5
print(subtract(5, 2))  # Output: 3
```

## Running Tests

Ensure you have all dependencies installed:

```bash
pip install -r default/requirements.txt
```

Run all tests using pytest:

```bash
pytest tests/ -v --tb=short
```

## CI Workflow

The CI pipeline is defined in `.github/workflows/ci.yml` and runs all tests on push and pull request events to the main branch.
