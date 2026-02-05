import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import whisper
import json
import time

class Back:
    def __init__(self,gui):
        self.gui = gui
        with open('/home/local/Documents/vscode/speech-bot/SpeechBot/person.json', 'r') as file:
            self.data = json.load(file)
        self.speechno = self.data['speechno']
        

    def voiceRecording(self):
        
        freq = 44100

        duration = 5

        recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

        sd.wait()
        self.speechno+=1
        self.data = {
            "speechno": self.speechno
        }
        with open('/home/local/Documents/vscode/speech-bot/SpeechBot/person.json', 'w') as file:
            json.dump(self.data, file, indent=4)
        wv.write(f"/home/local/Documents/vscode/speech-bot/SpeechBot/audio/recording{self.speechno}.wav", recording, freq, sampwidth=2)
        
        
    def transcribe(self):
        print("Transcription started")
        model = whisper.load_model("base")

        result = model.transcribe(f"/home/local/Documents/vscode/speech-bot/SpeechBot/audio/recording{self.speechno}.wav", language="en")

        self.gui.speechDisplay(result['text'])
        print('Transcription finished')
