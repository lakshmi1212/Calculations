# Calculations Repository

This repository provides basic math operations (addition and subtraction) implemented in Python, along with comprehensive pytest test cases and workflow instructions for CI/CD integration.

## Folder Structure
- `src/`: Contains production code.
- `tests/`: Contains test files for pytest.
- `default/requirements.txt`: Python dependencies.
- `default/README.md`: This file.
- `default/math.json`: CI/CD and test metadata.

## Usage

### Math Operations
```
from src.math_operations import add, subtract
print(add(2, 3))        # Output: 5
print(subtract(5, 3))   # Output: 2
```

### Running Tests
Install dependencies:
```
pip install -r default/requirements.txt
```
Run tests:
```
pytest tests/ -v --tb=short
```

## CI/CD Workflow
This repository is designed for easy integration with GitHub Actions using the metadata in `default/math.json`.
