# Backend Tests

This directory contains backend API tests for the FastAPI app.

## Test Files

- `test_root.py`: verifies `GET /` redirects to `/static/index.html`.
- `test_activities.py`: verifies `GET /activities` returns expected activity data.
- `test_signup.py`: verifies signup success and 404 behavior for unknown activities.
- `conftest.py`: shared pytest fixtures, including in-memory state reset between tests.

## Run Tests

From the repository root:

```bash
python -m pytest tests -v
```

If you are using this repo's virtual environment explicitly:

```bash
/workspaces/skills-getting-started-with-github-copilot/.venv/bin/python -m pytest tests -v
```
