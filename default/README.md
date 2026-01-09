# Calculations

## Overview
This repository provides basic math operations (addition and subtraction) with production-ready test automation integrated for CI/CD workflows.

## Usage

### Math Operations
Import and use the functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

result_add = add(2, 3)
result_subtract = subtract(5, 2)
```

### Running Tests
Install dependencies from `default/requirements.txt` and run tests:

```bash
pip install -r default/requirements.txt
python -m pytest tests/ -v --tb=short
```

## CI/CD Workflow
GitHub Actions workflow file is located at `.github/workflows/ci.yml`.

## Structure
- `src/math_operations.py`: Business logic
- `tests/`: Pytest test cases
- `default/README.md`: This file
- `default/requirements.txt`: Python dependencies
- `default/math.json`: Metadata for CI workflow

## Maintainers
QA Automation & DevOps Integration Agent
