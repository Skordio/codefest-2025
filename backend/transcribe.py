import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_APIKEY")
client = OpenAI(api_key=api_key)

def transcribe_audio(file_path):
    sound_file = open(file_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=sound_file, 
        response_format="text"
    )

    return transcription

def main():
    file_path = os.path.join('uploads/test-file.mp3')
    transcription = transcribe_audio(file_path)
    print(transcription)

if __name__ == '__main__':
    main()