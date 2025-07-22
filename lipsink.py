import os

def generate_lipsync_video(image_path, audio_path, output_path="outputs/lipsync_video.mp4",
                            checkpoint_dir=None):
    """
    Generates a lip-synced video from an image and audio file using SadTalker.
    """

    # Paths for SadTalker
    sad_talker_dir = "SadTalker"
    inference_script = os.path.join(sad_talker_dir, "inference.py")

    # Default checkpoint path if not passed
    if checkpoint_dir is None:
        checkpoint_dir = os.path.join(sad_talker_dir, "checkpoints")

    # Construct the command WITHOUT config_dir
    command = (
        f'python "{inference_script}" '
        f'--driven_audio "{audio_path}" '
        f'--source_image "{image_path}" '
        f'--checkpoint_dir "{checkpoint_dir}" '
        f'--result_dir "outputs" '
        f'--still --preprocess full --enhancer gfpgan'
    )

    # Run the command
    os.system(command)

    print(f"Lip-sync video saved in 'outputs/'")
    return output_path
