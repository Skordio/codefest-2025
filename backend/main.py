'''
    boilerplate
'''

from flask import Flask, request, Request, jsonify
from flask_cors import CORS
import os
from transcribe import transcribe_audio_from_file, transcribe_audio_from_path
from llm import generateQuiz, generateFlashcards, generateStudyGuide

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'API is working'})


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def transcribe_audio_file(request:Request) -> str:
    if "file" not in request.files:
        raise ValueError("No file uploaded")

    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    transcript = transcribe_audio_from_file(file_path)
    return transcript

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    transcript = transcribe_audio_from_path(file_path)
    return jsonify({"transcript": transcript})

@app.route("/createQuiz", methods=["POST"])
def createQuiz(request:Request):
    transcript = transcribe_audio_file(request)
    return jsonify(generateQuiz(transcript))

@app.route("/createStudyGuide", methods=["POST"])
def createStudyGuide(request:Request):
    transcript = transcribe_audio_file(request)
    return jsonify(generateStudyGuide(transcript))

@app.route("/createFlashcards", methods=["POST"])
def createFlashcards(request:Request):
    transcript = transcribe_audio_file(request)
    return jsonify(generateFlashcards(transcript))

#End API stuff

if __name__ == '__main__':
    app.run(debug=True)