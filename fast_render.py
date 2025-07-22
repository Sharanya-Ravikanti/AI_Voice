import os
import subprocess
from datetime import datetime

# Paths
timestamp = datetime.now().strftime("%Y_%m_%d_%H.%M.%S")
base_output_dir = f"outputs/{timestamp}"
first_frame_dir = "outputs/2025_04_17_18.12.41/first_frame_dir"
audio_path = "outputs/cloned_voice.wav"
mat_path = "outputs/2025_04_17_18.12.41/shar##cloned_voice.mat"  # Not used here anymore, as per new changes
image_path = os.path.join(first_frame_dir, "shar.png")

# Make sure output folder exists
os.makedirs(base_output_dir, exist_ok=True)

# Run only rendering (skipping full pipeline)
cmd = [
    "python", "SadTalker/inference.py",  # Changed from demo.py to inference.py
    "--driven_audio", audio_path,
    "--source_image", image_path,
    "--result_dir", base_output_dir,
    "--still",
    "--size", "256",
    "--preprocess", "full",
    "--pose_style", "0",
    "--batch_size", "2",
    "--input_yaw", "0",
    "--input_pitch", "0",
    "--input_roll", "0",
    "--expression_scale", "1.0",
]


print("🚀 Rendering directly from precomputed files...")
subprocess.run(cmd)
print(f"✅ Done! Check your output at: {base_output_dir}")
