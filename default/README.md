# Calculations

This repository provides basic math operations (addition and subtraction) and includes comprehensive pytest test cases.

## Usage

```
from src.math_operations import add, subtract

result_add = add(2, 3)        # 5
result_subtract = subtract(5, 2)  # 3
```

## Running Tests

Install dependencies:

```
pip install -r default/requirements.txt
```

Run all tests:

```
python -m pytest tests/ -v --tb=short
```

## CI Workflow

All commits to `main` branch trigger the CI pipeline defined in `.github/workflows/ci.yml`.
