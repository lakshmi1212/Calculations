# Calculations

This repository provides basic math operations (addition and subtraction) implemented in Python. It includes production code and comprehensive pytest-based test coverage.

## Usage

- Production code is in `src/math_operations.py`.
- Run tests using pytest:
  ```bash
  python -m pytest tests/ -v --tb=short
  ```

## CI/CD Workflow

- Workflow file: `.github/workflows/ci.yml`
- Tests are executed automatically on push and pull request events to the `main` branch.

## File Structure

- `src/`: Source code files
- `tests/`: Pytest test files
- `default/`: Metadata, README, and requirements

## Requirements

See `default/requirements.txt` for dependencies.
