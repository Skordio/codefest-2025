'''
    boilerplate
'''

from flask import Flask, request, Request, jsonify
from flask_cors import CORS
import os, ffmpeg
from transcribe import transcribe_audio_from_path
from llm import generateQuiz, generateFlashcards, generateStudyGuide

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'API is working'})


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Helper functions

def compress_audio(input_file_path:str, target_size_mb=25) -> str:
    # Get the original file size
    original_size = os.path.getsize(input_file_path) / (1024 * 1024)  # Convert to MB
    
    if original_size <= target_size_mb:
        print(f"File is already below {target_size_mb}MB.")
        return input_file_path

    # Estimate bitrate needed to fit the target size (assuming duration remains the same)
    probe = ffmpeg.probe(input_file_path)
    duration = float(probe['format']['duration'])  # Duration in seconds
    target_bitrate = (target_size_mb * 8 * 1024 * 1024) / duration  # in bps
    
    # Convert bitrate to kbps and apply reasonable limits
    target_bitrate_kbps = max(64, min(target_bitrate / 1000, 320))  # Between 64kbps and 320kbps

    print(f"Original size: {original_size:.2f}MB, Target bitrate: {target_bitrate_kbps:.0f}kbps")

    output_file_path = input_file_path.replace(".mp3", "_compressed.mp3")

    # Run ffmpeg to compress the audio
    (
        ffmpeg
        .input(input_file_path)
        .output(output_file_path, audio_bitrate=f'{int(target_bitrate_kbps)}k', format='mp3')
        .run(overwrite_output=True)
    )

    # Check the final file size
    final_size = os.path.getsize(output_file_path) / (1024 * 1024)
    print(f"Compressed file size: {final_size:.2f}MB")

    os.remove(input_file_path)

    return output_file_path

def transcribe_audio_file(request:Request) -> str:
    if "file" not in request.files:
        raise ValueError("No file uploaded")

    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Compress the audio file if it's too large
    compressed_file_path = compress_audio(file_path)

    transcript = transcribe_audio_from_path(compressed_file_path)
    return transcript

# Endpoints

@app.route("/transcribe", methods=["POST"])
def transcribe():
    transcript = transcribe_audio_file(request)
    return jsonify({"transcript": transcript})

@app.route("/create", methods=["POST"])
def create():
    quiz = True if request.args.get("quiz") == "true" else False
    studyGuide = True if request.args.get("study_guide") == "true" else False
    flashcards = True if request.args.get("flashcards") == "true" else False

    transcript = transcribe_audio_file(request)

    if quiz:
        quiz = generateQuiz(transcript)
    else:
        quiz = {}

    if studyGuide:
        studyGuide = generateStudyGuide(transcript)
    else:
        studyGuide = {}

    if flashcards:
        flashcards = generateFlashcards(transcript)
    else:
        flashcards = {}

    return jsonify({"quiz": quiz, "studyGuide": studyGuide, "flashcards": flashcards})


if __name__ == '__main__':
    app.run(debug=True)