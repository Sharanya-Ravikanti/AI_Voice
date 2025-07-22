import os
import torch
from tqdm import tqdm
from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig

# Fix for PyTorch 2.6+ deserialization issues
# Allow the XTTS config class
#torch.serialization.add_safe_globals({XttsConfig.__name__: XttsConfig})

# Patch torch.load to always use weights_only=False (trust this ONLY if model is safe)
original_torch_load = torch.load

def safe_load(*args, **kwargs):
    kwargs["weights_only"] = False  # Force full object loading
    return original_torch_load(*args, **kwargs)

torch.load = safe_load  # Apply patch

def generate_voice(text, output_path, voice_sample_path=None):
    progress_bar = None
    try:
        print("🔊 Loading XTTS voice cloning model...")
        tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True, gpu=False)

        progress_bar = tqdm(total=3, desc="Voice Cloning", position=0, leave=True)

        if voice_sample_path and os.path.exists(voice_sample_path):
            print(f"🎤 Cloning voice from: {voice_sample_path}")
            tts.tts_to_file(
                text=text,
                file_path=output_path,
                speaker_wav=voice_sample_path,
                language="en"
            )
        else:
            print("⚠️ No voice sample provided. Using default voice.")
            tts.tts_to_file(
                text=text,
                file_path=output_path,
                language="en"
            )

        progress_bar.update(1)
        progress_bar.set_description("Voice Cloning Done")
        print("✅ Voice generated and saved to:", output_path)
        return True

    except Exception as e:
        print("❌ Voice generation failed:", e)
        return False

    finally:
        if progress_bar:
            progress_bar.close()

# Optional: restore original torch.load after use
# torch.load = original_torch_load
