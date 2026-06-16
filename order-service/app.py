import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

PORT = int(os.environ.get("PORT", 5002))
# This URL will change depending on whether we run locally, in Docker, or Kubernetes
PRODUCT_SERVICE_URL = os.environ.get("PRODUCT_SERVICE_URL", "http://localhost:5001")

# Mock database of orders
orders = []

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)

    if not product_id:
        return jsonify({"error": "Missing product_id"}), 400

    # Communicate with the Product Service to validate the item
    try:
        response = requests.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
        if response.status_code == 404:
            return jsonify({"error": "Cannot place order. Product does not exist."}), 400
        
        product_data = response.json()
    except requests.exceptions.RequestException:
        return jsonify({"error": "Product Service is currently unreachable"}), 500

    # Create the order object if validation passes
    new_order = {
        "order_id": len(orders) + 1,
        "product_name": product_data["name"],
        "price": product_data["price"],
        "quantity": quantity,
        "total": round(product_data["price"] * quantity, 2)
    }
    orders.append(new_order)
    
    return jsonify({"message": "Order placed successfully!", "order": new_order}), 21
    return jsonify({"message": "Order placed successfully!", "order": new_order}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
