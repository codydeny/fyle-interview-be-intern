from flask import jsonify
import json

from core import app
from core.libs import helpers


def test_hello():
    with app.test_client() as c:
        expected_response = c.get('/')
        expected_response = json.loads(expected_response.data)
        assert expected_response["status"] == "ready"
