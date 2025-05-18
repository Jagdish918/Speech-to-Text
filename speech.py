import speech_recognition as sr

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError:
        return "Could not request results from the speech recognition service."

# Example usage
if __name__ == "__main__":
    audio_file = "audio.wav"
    print("Transcription:", transcribe_audio(audio_file))
