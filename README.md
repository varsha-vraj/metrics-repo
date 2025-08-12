# metrics-repo

Centralized repository for metric definitions and analyzers.

## Structure

- `metrics_repo/analyzers` - analyzer functions (e.g. churn, sales)
- `tests` - pytest unit tests

## Quickstart

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
pytest -q
