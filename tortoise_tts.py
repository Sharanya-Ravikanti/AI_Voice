# tortoise_tts.py

from TTS.api import TTS

# Load model only once
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

def clone_voice(input_audio, text, output_audio="outputs/cloned_voice.wav"):
    """
    This now uses a faster TTS model from Coqui TTS.
    It doesn't clone voice exactly but synthesizes in a standard voice.
    """
    print("[INFO] Synthesizing speech with Coqui TTS...")
    tts.tts_to_file(text=text, file_path=output_audio)
    return output_audio
