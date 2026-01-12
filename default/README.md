# Calculations

This repository provides basic math operations (addition and subtraction).

## Usage

Import the functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

result_add = add(5, 3)      # Returns 8
result_sub = subtract(5, 3) # Returns 2
```

## Running Tests

Install dependencies:

```bash
pip install -r default/requirements.txt
```

Run tests using pytest:

```bash
pytest tests/ -v --tb=short
```

## CI Workflow

The CI workflow is defined in `.github/workflows/ci.yml` and runs tests on every push or pull request to `main`.
