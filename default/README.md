# Calculations

## Overview
This repository provides basic math operations (addition and subtraction) implemented in Python, along with comprehensive pytest test coverage and CI/CD workflow integration.

## Usage

- Source code: `src/math_operations.py`
- Add two numbers:
  ```python
  from src.math_operations import add
  print(add(2, 3))  # Output: 5
  ```
- Subtract two numbers:
  ```python
  from src.math_operations import subtract
  print(subtract(5, 2))  # Output: 3
  ```

## Running Tests

1. Install dependencies:
   ```bash
   pip install -r default/requirements.txt
   ```
2. Run all tests:
   ```bash
   pytest tests/ -v --tb=short
   ```

## CI/CD Workflow
- Workflow file: `.github/workflows/ci.yml`
- On push or pull request to `main`, CI will run all Python tests in the `tests` folder using pytest.

## Folder Structure
- `src/`: Source code
- `tests/`: Test files (pytest)
- `default/`: Metadata, requirements, documentation

---
Maintained by Senior QA Automation and DevOps Integration Agent
