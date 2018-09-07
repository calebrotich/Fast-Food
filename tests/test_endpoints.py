from app.app import app
import pytest
from flask import json
from app.data import Orders


Orders = Orders()
first_key = list(Orders.keys())[0]

""" Test GET all orders """

def test_fetch_all_orders():
    result = app.test_client()
    response = result.get('/api/v1/orders', content_type='application/json')
    assert(response.status_code == 200)


""" Test POST new order """

def test_place_new_order():
    result = app.test_client()
    response = result.post('/api/v1/orders', content_type='application/json')
    assert(response.status_code == 200)


""" Test UPDATE specific order """

def test_update_specific_order():
    result = app.test_client()
    response = result.put('/api/v1/orders/'+first_key+'/new_status', content_type='application/json')
    assert(response.status_code == 200)


""" Test GET specific order """
def test_fetch_specific_order():
    result = app.test_client()
    response = result.get('/api/v1/orders/'+first_key+'/', content_type='application/json')
    assert(response.status_code == 200)