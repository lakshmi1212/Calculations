# Calculations

This repository provides basic mathematical operations (addition and subtraction) implemented in Python.

## Usage

Import the functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

result = add(2, 3)      # Returns 5
result2 = subtract(5, 2) # Returns 3
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

## Workflow

CI pipeline is configured to run tests on push or pull request to the `main` branch using `.github/workflows/ci.yml`.
