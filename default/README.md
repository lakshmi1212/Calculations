# Calculations

This repository implements basic math operations (addition and subtraction) in Python and provides tests and CI workflow integration.

## Usage

```python
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 2))   # Output: 3
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

## CI Workflow

The repository includes a CI workflow file at `.github/workflows/ci.yml` for automated testing on push and pull request events.
