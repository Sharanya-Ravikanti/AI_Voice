import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

class SadTalkerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SadTalker Video Generator")
        self.root.geometry("500x400")
        
        self.image_path = None
        self.ppt_path = None
        self.audio_path = None

        tk.Label(root, text="Upload Inputs", font=("Helvetica", 16)).pack(pady=10)

        tk.Button(root, text="Upload Image", command=self.upload_image).pack(pady=5)
        tk.Button(root, text="Upload PPT", command=self.upload_ppt).pack(pady=5)
        tk.Button(root, text="Upload Audio (Optional)", command=self.upload_audio).pack(pady=5)

        tk.Button(root, text="Generate Video", command=self.run_pipeline, bg="green", fg="white").pack(pady=20)

        self.status_label = tk.Label(root, text="", fg="blue")
        self.status_label.pack(pady=10)

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        self.status_label.config(text=f"Selected image: {os.path.basename(self.image_path)}")

    def upload_ppt(self):
        self.ppt_path = filedialog.askopenfilename(filetypes=[("PowerPoint Files", "*.pptx")])
        self.status_label.config(text=f"Selected PPT: {os.path.basename(self.ppt_path)}")

    def upload_audio(self):
        self.audio_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
        self.status_label.config(text=f"Selected audio: {os.path.basename(self.audio_path)}")

    def run_pipeline(self):
        if not self.image_path or not self.ppt_path:
            messagebox.showerror("Error", "Please upload both Image and PPT")
            return
        
        # Command to run main.py
        cmd = ["python", "main.py", "--image", self.image_path, "--ppt", self.ppt_path]
        if self.audio_path:
            cmd += ["--audio", self.audio_path]

        self.status_label.config(text="Processing... Please wait ⏳")
        try:
            subprocess.run(cmd, check=True)
            self.status_label.config(text="✅ Video Generated! Check 'outputs' folder.")
        except subprocess.CalledProcessError:
            self.status_label.config(text="❌ Error during generation.")
            messagebox.showerror("Error", "Something went wrong while generating video.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SadTalkerApp(root)
    root.mainloop()
