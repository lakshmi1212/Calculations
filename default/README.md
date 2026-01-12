# Calculations

## Overview
This repository provides basic math operations (addition and subtraction) and associated unit tests. All source code is in `src/`, and tests are in `tests/`. CI/CD integration is configured via `.github/workflows/ci.yml`.

## Usage

### Math Operations
Import and use functions from `src/math_operations.py`:
```python
from src.math_operations import add, subtract
print(add(2, 3))       # Output: 5
print(subtract(5, 2))  # Output: 3
```

### Running Tests
Install dependencies and run tests:
```sh
pip install -r default/requirements.txt
pytest tests/ -v --tb=short
```

## CI/CD
- Workflow file: `.github/workflows/ci.yml`
- Runs on push and pull request events to `main`
- Uses Python 3.10

## Folder Structure
- `src/`: Source code
- `tests/`: Pytest test cases
- `default/`: Metadata, requirements, and documentation
