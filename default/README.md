# Calculations

This repository provides basic mathematical operations (addition and subtraction) with automated testing and CI integration.

## Usage

Import functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 2))   # Output: 3
```

## Testing

Run tests using pytest:

```bash
python -m pytest tests/ -v --tb=short
```

## CI/CD

Workflow file: `.github/workflows/ci.yml`

See `default/math.json` for metadata for workflow generation.
