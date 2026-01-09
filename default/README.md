# Calculations

This repository provides basic math operations (addition and subtraction) with production-ready unit tests and CI/CD workflow integration.

## Usage

Import the functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 3))   # Output: 2
```

## Running Tests

Install dependencies:

```bash
pip install -r default/requirements.txt
```

Run all tests:

```bash
python -m pytest tests/ -v --tb=short
```

## CI/CD Workflow

A GitHub Actions workflow is expected at `.github/workflows/ci.yml` to run all tests on push and pull request events.

## File Structure

- `src/math_operations.py`: Business logic for math operations
- `tests/`: Pytest test cases
- `default/requirements.txt`: Python dependencies
- `default/math.json`: Metadata for workflow generation
- `.github/workflows/ci.yml`: CI workflow (to be generated)
