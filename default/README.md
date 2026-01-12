# Calculations

This repository provides basic math operations (addition and subtraction) with comprehensive unit tests and CI workflow integration.

## Usage

- Source code is located in `src/math_operations.py`
- Unit tests are in the `tests/` folder

### Example
```python
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 3))   # Output: 2
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

## CI Workflow

Workflow file: `.github/workflows/ci.yml`
- Runs tests automatically on push and pull requests to `main`

## Project Structure
```
src/
  math_operations.py

tests/
  test_add.py
  test_subtract.py

default/
  README.md
  requirements.txt
  math.json
```
