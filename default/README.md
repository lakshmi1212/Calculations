# Calculations

This repository provides basic math operations (addition and subtraction) with comprehensive pytest-based testing and CI integration.

## Structure
- `src/math_operations.py`: Core math functions
- `tests/test_add.py`: Tests for addition
- `tests/test_subtract.py`: Tests for subtraction
- `default/requirements.txt`: Python dependencies
- `default/math.json`: CI workflow metadata

## Usage
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
Run tests:
```bash
pytest tests/ -v --tb=short
```

## CI Workflow
The repository is ready for GitHub Actions CI using the metadata in `default/math.json`.
