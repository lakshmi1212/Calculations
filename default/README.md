# Calculations

This repository provides basic math operations (addition and subtraction) with automated testing and CI workflow integration.

## Usage

Import and use the functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

result_add = add(3, 5)
result_subtract = subtract(10, 4)
```

## Testing

All tests are located in the `tests` folder. Run tests using:

```
python -m pytest tests/ -v --tb=short
```

## CI Workflow

The workflow is defined in `.github/workflows/ci.yml` and runs on push and pull requests.

## Requirements

See `default/requirements.txt` for dependencies.
