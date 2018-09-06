import pytest
from flask import json
from app import app

""" Test GET all orders """

def test_fetch_all_orders():
    result = app.test_client()
    response = result.get('/api/v1/orders', content_type='application/json')
    assert(response.status_code == 200)