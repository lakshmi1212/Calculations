# Calculations

This repository provides basic math operations (addition and subtraction) as Python functions, along with production-ready pytest test files and CI/CD workflow metadata.

## Usage

- Import functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

result = add(2, 3)
result2 = subtract(5, 3)
```

## Testing

Tests are located in the `tests/` folder:

- `tests/test_add.py`: tests for addition
- `tests/test_subtract.py`: tests for subtraction

Run all tests with:

```
python -m pytest tests/ -v --tb=short
```

## CI/CD Workflow

See `default/math.json` for workflow metadata used by automation agents.

## Requirements

- Python 3.10+
- pytest

Install dependencies:

```
pip install -r default/requirements.txt
```
