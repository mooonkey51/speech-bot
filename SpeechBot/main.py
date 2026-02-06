import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import whisper
import json
from llama_cpp import Llama

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

        self.transcription = model.transcribe(f"/home/local/Documents/vscode/speech-bot/SpeechBot/audio/recording{self.speechno}.wav", language="en")
        
        self.gui.speechDisplay(self.transcription['text'])
        print('Transcription finished')
        
        
        
    def analyseSpeech(self):
        print("Analysis of the speech started!")
        llm = Llama(
            #model_path="/home/youruser/models/llama-2-7b-chat.Q4_K_M.gguf",
            #model_path = "~/models/llama-2-7b-chat.Q4_K_M.bin",
            model_path= "/home/local/Documents/vscode/llama-env/models/llama-2-7b.Q4_K_M.gguf",
            #n_ctx=4096,
            n_ctx=2048,
            n_threads=8   
        )

        prompt = f"""
            Analyze the following speech:
            1. Grammar mistakes
            2. Fluency and articulation
            3. Content quality
            4. Suggestions for improvement

            Speech:
            {self.transcription["text"]}
            """

        response = llm(prompt, max_tokens=500)
        print(response["choices"][0]["text"])
        self.gui.analysisDisplay(response["choices"][0]["text"])

