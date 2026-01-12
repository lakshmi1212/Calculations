# Calculations

This repository implements basic math operations (`add` and `subtract`) with production-ready pytest test cases and CI/CD workflow integration.

## Usage

- Add: `add(a, b)` returns the sum of `a` and `b`
- Subtract: `subtract(a, b)` returns the difference of `a` and `b`

## Testing

All tests are located in the `tests/` folder and can be run using:

```bash
python -m pytest tests/ -v --tb=short
```

## Workflow

CI/CD workflow file: `.github/workflows/ci.yml`

## Requirements

See `default/requirements.txt` for dependencies.
