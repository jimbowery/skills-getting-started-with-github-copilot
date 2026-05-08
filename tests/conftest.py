import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture(autouse=True)
def reset_activities(monkeypatch):
    """Reset mutable in-memory state before each test."""
    fresh_activities = copy.deepcopy(app_module.activities)
    monkeypatch.setattr(app_module, "activities", fresh_activities)


@pytest.fixture
def client():
    return TestClient(app_module.app)
