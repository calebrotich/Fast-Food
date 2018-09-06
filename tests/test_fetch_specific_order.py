import sys
sys.path.append('C:\\Andela\\Fast-Food')
import pytest
from flask import json
from app import app
from app.data import Orders

Orders = Orders()
first_key = list(Orders.keys())[0]


""" Test GET specific order """

def test_fetch_specific_order():
    result = app.test_client()
    response = result.get('/api/v1/orders/'+first_key+'/', content_type='application/json')
    assert(response.status_code == 200)