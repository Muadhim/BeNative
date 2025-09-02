import whisper
from core.speech import record_audio, detect_language
from core.ai import ask_ollama
from core.tts import speak_text

# Load whisper sekali
whisper_model = whisper.load_model("base")

def transcribe_audio(audio_file):
    result = whisper_model.transcribe(audio_file, fp16=False)
    return result["text"].strip()

def conversation_loop(stop_event):
    while not stop_event.is_set():
        # 1. Rekam
        audio_file = record_audio(duration=5)
        
        # 2. Transkrip
        text = transcribe_audio(audio_file)
        print("👤 User:", text)

        if not text:
            continue

        # 3. Cek bahasa
        lang = detect_language(text)
        if lang != "en":
            feedback = "Please practice in English."
            print("⚠️", feedback)
            speak_text(feedback)
            continue

        # 4. Kirim ke Ollama
        response = ask_ollama(text)
        print("🤖 Ollama:", response)

        # 5. Balas dengan suara
        speak_text(response)
