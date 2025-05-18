# Basic Speech-to-Text System

This project provides a simple way to convert short audio clips into text using Python. It supports two methods:

- Using the `speech_recognition` library with Google Web Speech API (requires internet)
- Using the Hugging Face `wav2vec2` pre-trained model for offline transcription

---

## Requirements

- Python 3.6 or higher
- Required Python packages:
  ```bash
  pip install SpeechRecognition
  pip install pyaudio        # Optional, for microphone input
  pip install torch torchaudio transformers

## Output

![Image](https://github.com/user-attachments/assets/15e190f8-67d5-40e0-8391-27c981d8cd3a)
