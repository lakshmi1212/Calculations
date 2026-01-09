# Calculations

This repository provides basic math operations (addition and subtraction) with tested Python functions and CI/CD integration.

## Usage

Import `add` and `subtract` from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

result_add = add(2, 3)
result_subtract = subtract(5, 2)
```

## Testing

Run tests using pytest:

```bash
pytest tests/
```

## Workflow

CI is configured to run tests automatically on push and pull request events using `.github/workflows/ci.yml`.
