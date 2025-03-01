'''
    boilerplate
'''

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'API is working'})

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    # Process data and create a new item (e.g., in a database)
    return jsonify({'message': 'Item created successfully', 'data': data}), 201

@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    # Retrieve item from database based on item_id
    item = {'id': item_id, 'name': 'Example Item'}
    return jsonify(item)

@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
     data = request.get_json()
    # Update item in database based on item_id and data
     return jsonify({'message': 'Item updated successfully', 'data': data})

@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    # Delete item from database based on item_id
    return jsonify({'message': 'Item deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)