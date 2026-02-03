from pathlib import Path
import whisper

model = whisper.load_model("base")

result = model.transcribe(r"C:\Users\Arya\Documents\vscode\SpeechBot\audio\Recording.m4a")

print(result["text"])
