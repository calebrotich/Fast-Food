from flask import jsonify, Flask
from app.data import Orders


app = Flask(__name__)
    
Orders = Orders()

@app.route('/api/v1/orders', methods = ['GET'])
def fetch_all_orders():
    return jsonify(Orders)

@app.route('/api/v1/orders/<string:id>/', methods = ['GET'])
def fetch_specific_order(id):
    order = Orders[id]
    return jsonify(order)

@app.route('/api/v1/orders', methods = ['POST'])
def place_new_order():
    Orders['3'] = {
        "order_id" : 3,
        "food_ordered": "Juice",
        "quantity" : 1,
        "date_ordered" : "06/09/2018",
        "status" : "Pending"
    }
    return "Order made successfully"