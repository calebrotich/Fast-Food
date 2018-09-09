from flask import jsonify, Flask, render_template
from app.data import Orders


app = Flask(__name__)
    
Orders = Orders()

@app.route('/')
def home():
    return render_template("index.html")

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

    return "Order made successfully. Send a GET request to view the added order."

@app.route('/api/v1/orders/<string:id>/<string:status>', methods = ['PUT'])
def update_order_status(id, status):
    Orders[id]["status"] = status
    return "Order " + id + " status updated to " + status