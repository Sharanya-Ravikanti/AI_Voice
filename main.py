import argparse
import os
from tqdm import tqdm
from ppt import extract_text
from coqui_tts import generate_voice
from lipsink import generate_lipsync_video

def main():
    parser = argparse.ArgumentParser(description="Generate lip-sync video from PPT and reference voice")
    parser.add_argument("--image", required=True, help="Path to the input image")
    parser.add_argument("--ppt", required=True, help="Path to the input PPTX file")
    parser.add_argument("--audio", required=False, help="Path to reference audio (WAV file) for voice cloning")

    args = parser.parse_args()

    image_path = args.image
    ppt_path = args.ppt
    voice_sample_path = args.audio

    # Output files
    os.makedirs("outputs", exist_ok=True)
    output_audio_path = "outputs/cloned_voice.wav"
    output_video_path = "outputs/lipsync_video.mp4"

    # Step 1: Extract text from PPT
    print("📄 Extracting text from PPT...")
    ppt_text = extract_text(ppt_path)
    print("📝 Extracted Text:", ppt_text)

    # Step 2: Generate cloned voice
    print("🔊 Generating voice from PPT text...")
    if not generate_voice(ppt_text, output_audio_path, voice_sample_path):
        print("❌ Voice generation failed. Exiting...")
        return

    # Step 3: Generate lip-sync video
    print("🎥 Generating lip-sync video...")
    generate_lipsync_video(image_path=image_path, audio_path=output_audio_path)

    print("✅ Done! Final video saved to:", output_video_path)
    print("✅ Final video should be here:", os.path.abspath("outputs/lipsync_video.mp4"))
    print("📂 Listing outputs folder:")
    print(os.listdir("outputs"))

if __name__ == "__main__":
    main()
