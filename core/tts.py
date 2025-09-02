from TTS.api import TTS
import os

# load model sekali saja (bisa ganti sesuai kebutuhan)
# contoh: tacotron2-DDC
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

def speak_text(text: str, output_file="output.wav"):
    # generate suara
    tts.tts_to_file(text=text, file_path=output_file)
    # play pakai default system player
    os.system(f"aplay {output_file} >/dev/null 2>&1")
