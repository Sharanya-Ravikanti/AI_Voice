# ui_launcher.py
import tkinter as tk
from tkinter import filedialog
import subprocess

def run_pipeline(image_path, audio_path, ppt_path):
    # You can call your main script here with args
    subprocess.run([
        "python", "main.py",
        "--image", image_path,
        "--audio", audio_path,
        "--ppt", ppt_path
    ])

def select_image():
    image_path.set(filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg")]))
    
def select_audio():
    audio_path.set(filedialog.askopenfilename(filetypes=[("Audio", "*.wav *.mp3")]))
    
def select_ppt():
    ppt_path.set(filedialog.askopenfilename(filetypes=[("PowerPoint", "*.pptx")]))

def start():
    run_pipeline(image_path.get(), audio_path.get(), ppt_path.get())

app = tk.Tk()
app.title("Bubu LipSync Generator")

image_path = tk.StringVar()
audio_path = tk.StringVar()
ppt_path = tk.StringVar()

tk.Label(app, text="Select Image:").pack()
tk.Entry(app, textvariable=image_path, width=50).pack()
tk.Button(app, text="Browse", command=select_image).pack()

tk.Label(app, text="Select Audio:").pack()
tk.Entry(app, textvariable=audio_path, width=50).pack()
tk.Button(app, text="Browse", command=select_audio).pack()

tk.Label(app, text="Select PPT:").pack()
tk.Entry(app, textvariable=ppt_path, width=50).pack()
tk.Button(app, text="Browse", command=select_ppt).pack()

tk.Button(app, text="Generate Video", command=start).pack(pady=20)

app.mainloop()
