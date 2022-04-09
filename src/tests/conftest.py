import pytest


@pytest.fixture
def app():
    from src.server import app
    return app
