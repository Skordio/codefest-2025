'''
    boilerplate
'''

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from transcribe import transcribe_audio_from_file, transcribe_audio_from_path
from llm import generateQuiz

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'API is working'})

# @app.route('/items', methods=['POST'])
# def create_item():
#     data = request.get_json()
#     # Process data and create a new item (e.g., in a database)
#     return jsonify({'message': 'Item created successfully', 'data': data}), 201

# @app.route('/items/<item_id>', methods=['GET'])
# def get_item(item_id):
#     # Retrieve item from database based on item_id
#     item = {'id': item_id, 'name': 'Example Item'}
#     return jsonify(item)

# @app.route('/items/<item_id>', methods=['PUT'])
# def update_item(item_id):
#      data = request.get_json()
#     # Update item in database based on item_id and data
#      return jsonify({'message': 'Item updated successfully', 'data': data})

# @app.route('/items/<item_id>', methods=['DELETE'])
# def delete_item(item_id):
#     # Delete item from database based on item_id
#     return jsonify({'message': 'Item deleted successfully'})

#API STUFF IDK

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route("/upload", methods=["POST"])
# def upload_file():
#     if "file" not in request.files:
#         return jsonify({"error": "No file uploaded"}), 400

#     file = request.files["file"]
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(file_path)

#     return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)


    transcript = transcribe_audio_from_path(file_path)
    os.remove(file_path)
    return jsonify({"transcript": transcript})

@app.route("/createQuiz", methods=["POST"])
def createQuiz():
    getReq = request.get_json()
    return jsonify(generateQuiz(getReq['transcription']))

#End API stuff

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)