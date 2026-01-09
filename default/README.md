# Calculations

This repository provides simple math operations (addition and subtraction) implemented in Python.

## Usage

Import the functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

result_add = add(2, 3)
result_subtract = subtract(5, 2)
```

## Testing

Unit tests are provided in the `tests` folder.
Run all tests with:

```sh
python -m pytest tests/ -v --tb=short
```

## CI/CD Workflow

Automated tests are run on every push and pull request to the `main` branch via GitHub Actions workflow defined in `.github/workflows/ci.yml`.

## Requirements

All dependencies are listed in `default/requirements.txt`.
