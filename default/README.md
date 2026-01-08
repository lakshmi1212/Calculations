# Calculations

This repository contains Python implementations for basic math operations: addition and subtraction, along with comprehensive pytest-based tests and CI/CD workflow integration.

## Folder Structure
- `src/`: Contains core math logic (`math_operations.py`)
- `tests/`: Contains pytest test files (`test_add.py`, `test_subtract.py`)
- `default/`: Contains configuration files (`requirements.txt`, `math.json`, `README.md`)

## Usage
1. Install dependencies:
   ```bash
   pip install -r default/requirements.txt
   ```
2. Run tests:
   ```bash
   python -m pytest tests/ -v --tb=short
   ```

## CI/CD Workflow
- Automated tests are triggered on push and pull request events to the `main` branch.
- Workflow file: `.github/workflows/ci.yml`

For workflow details, see `default/math.json`.
