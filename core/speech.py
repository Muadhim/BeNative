import sounddevice as sd
import soundfile as sf
import pyttsx3
import tempfile
from langdetect import detect

# --- Rekam suara ---
def record_audio(duration=5, samplerate=16000):
    tmpfile = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    print("🎙️ Recording...")
    data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write(tmpfile.name, data, samplerate)
    return tmpfile.name

# --- TTS ---
tts_engine = pyttsx3.init()

def speak_text(text: str):
    print(f"🗣️ Speaking: {text}")
    tts_engine.say(text)
    tts_engine.runAndWait()

# --- Language Detection ---
def detect_language(text: str) -> str:
    try:
        return detect(text)
    except:
        return "unknown"
