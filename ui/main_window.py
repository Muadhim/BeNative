import sys
import queue
import tempfile
import sounddevice as sd
import soundfile as sf
import numpy as np
import whisper
import pyttsx3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel

# Buffer audio untuk rekaman
q = queue.Queue()

# Load model whisper
model = whisper.load_model("base")  # bisa "small", "medium", "large"

# Engine TTS
engine = pyttsx3.init()

def callback(indata, frames, time, status):
    """Callback untuk sounddevice"""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

class SpeechApp(QWidget):
    text_input = ''
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Whisper Demo")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Klik tombol untuk bicara...")

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)

        self.btn_record = QPushButton("🎤 Rekam dan Transkrip")
        self.btn_record.clicked.connect(self.record_and_transcribe)

        self.btn_play = QPushButton("🔊 Play Text")
        self.btn_play.clicked.connect(self.play_text)

        self.btn_check_voice = QPushButton("Check voice")
        self.btn_check_voice.clicked.connect(self.check_voice)

        layout.addWidget(self.label)
        layout.addWidget(self.text_area)
        layout.addWidget(self.btn_record)
        layout.addWidget(self.btn_play)
        layout.addWidget(self.btn_check_voice)

        self.setLayout(layout)

    def record_and_transcribe(self):
        duration = 5  # detik
        samplerate = 16000
        self.text_area.append("⏺️ Merekam audio...")
        recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype="float32")
        sd.wait()

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
            sf.write(tmpfile.name, recording, samplerate)
            result = model.transcribe(tmpfile.name, fp16=False)
            text = result["text"]

        self.text_area.append(f"📝 Hasil: {text}")
        self.text_input = text
        print("Transcribed:", text)

    def play_text(self):
        text = self.text_input
        if not text:
            self.text_input.append("⚠️ Tidak ada teks untuk dibacakan")
            return
        self.text_area.append("🔊 Membacakan teks...")
        engine.say(text)
        engine.runAndWait()
    
    def check_voice(self):
        voices = engine.getProperty("voices")
        for voice in voices:
            self.text_area.append(f"voice: {voice} voice_id: {voice.id}")
            engine.say("Hello World")
            engine.runAndWait()
            engine.stop()
