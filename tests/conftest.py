from copy import deepcopy
from importlib import import_module

import pytest
from fastapi.testclient import TestClient

app_module = import_module("src.app")


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(app_module, "activities", deepcopy(app_module.activities))

    with TestClient(app_module.app) as test_client:
        yield test_client