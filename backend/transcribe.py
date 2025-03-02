import os, openai

api_key = os.getenv("OPENAI_APIKEY")
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transcribe_audio_from_file(sound_file):
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=sound_file, 
        response_format="text"
    )

    return transcription

def transcribe_audio_from_path(file_path):
    sound_file = open(file_path, "rb")
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