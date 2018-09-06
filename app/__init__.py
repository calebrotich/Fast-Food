from flask import jsonify, Flask
from app.data import Orders


app = Flask(__name__)
    
Orders = Orders()

@app.route('/api/v1/orders', methods = ['GET'])
def fetch_all_orders():
    return jsonify(Orders)