"""
initialization of test application
"""
from starlette.testclient import TestClient

from .app import app

test_app = TestClient(app)

