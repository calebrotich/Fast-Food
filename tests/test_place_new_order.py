import sys
import pytest
from flask import json
from app import app
from app.data import Orders

Orders = Orders()
first_key = list(Orders.keys())[0]


""" Test POST new order """

def test_place_new_order():
    result = app.test_client()
    response = result.post('/api/v1/orders', content_type='application/json')
    assert(response.status_code == 200)