# Calculations

## Overview
This repository provides basic math operations (addition and subtraction) with automated tests and CI/CD workflow integration.

## Usage
- Source code: `src/math_operations.py`
- Functions: `add(a, b)`, `subtract(a, b)`

## Running Tests
Install dependencies:
```bash
pip install -r default/requirements.txt
```
Run all tests:
```bash
pytest tests/ -v --tb=short
```

## CI/CD Workflow
- Workflow file: `.github/workflows/ci.yml`
- Trigger: On push and pull request to `main`
- Runs: Python 3.10, installs dependencies, runs tests

## Repository Structure
```
src/
  math_operations.py

tests/
  test_add.py
  test_subtract.py

default/
  requirements.txt
  README.md
  math.json
```
