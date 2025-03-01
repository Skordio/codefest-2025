import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_APIKEY")
client = OpenAI(api_key=api_key)

def transcribe_audio(file_path):
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=file_path, 
        response_format="text"
    )

    return transcription
