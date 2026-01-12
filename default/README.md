# Calculations

This repository provides basic math operations implemented in Python.

## Usage

```
from src.math_operations import add, subtract

result = add(2, 3)
print(result)  # 5

result = subtract(5, 2)
print(result)  # 3
```

## Testing

Install dependencies:
```
pip install -r default/requirements.txt
```
Run tests:
```
pytest tests/ -v --tb=short
```

## CI Workflow

See the workflow file at `.github/workflows/ci.yml` for automated testing instructions.
