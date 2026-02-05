import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import whisper



model = whisper.load_model("base")

result = model.transcribe(f"/home/local/Documents/vscode/speech-bot/SpeechBot/audio/recording26.wav")

print(result['text'])
