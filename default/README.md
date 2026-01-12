# Calculations

This repository provides basic math operations (addition and subtraction) with automated tests and CI workflow integration.

## Usage

Import from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

print(add(2, 3))       # 5
print(subtract(5, 2))  # 3
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

See `.github/workflows/ci.yml` for automated test execution.
