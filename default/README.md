# Calculations

This repository provides basic math operations (addition, subtraction) in Python, along with comprehensive tests and CI/CD workflow integration.

## Structure
- `src/math_operations.py`: Core math functions
- `tests/`: Pytest-based unit tests for all operations
- `default/requirements.txt`: Python dependencies
- `default/math.json`: CI/CD workflow metadata (for other agents)

## Usage

```
from src.math_operations import add, subtract
print(add(2, 3))       # Output: 5
print(subtract(5, 2))  # Output: 3
```

## Running Tests

Install dependencies:
```
pip install -r default/requirements.txt
```
Run tests:
```
pytest tests/ -v --tb=short
```

## Workflow
- CI runs on push/pull_request to `main` branch
- Workflow file: `.github/workflows/ci.yml`
- Test command: `pytest tests/ -v --tb=short`

## Requirements
See `default/requirements.txt` for Python dependencies.
