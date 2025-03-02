import os, openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

def transcribe_audio_from_file(sound_file):
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=sound_file, 
        response_format="text"
    )

    return transcription

def transcribe_audio_from_path(file_path):
    with open(file_path, "rb") as sound_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=sound_file, 
            response_format="text"
        )

    return transcription

def main():
    file_path = os.path.join('uploads/test-file.mp3')
    transcription = transcribe_audio_from_path(file_path)
    print(transcription)

if __name__ == '__main__':
    main()