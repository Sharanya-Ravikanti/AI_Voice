# 🗣️ AI_Voice - Voice Cloning & Lip-sync Video Generator

AI_Voice is an end-to-end pipeline that transforms a PowerPoint presentation into a video where a static image appears to speak the presentation content in a cloned voice. It combines voice cloning, text-to-speech, and lip-sync animation using powerful AI tools.

---

## 🚀 Features

- 🎤 Clone a speaker's voice using a reference audio file
- 📄 Extract text content from PPT/PPTX presentations
- 🔊 Generate speech in the cloned voice from extracted text
- 🧑‍🎤 Create lip-synced talking head videos from a static image
- 🗂️ Clean modular structure for integration or expansion

---

## 📁 Project Structure
AI_Voice/
├── main.py # Main controller script
├── ppt.py # Extracts text from PowerPoint
├── xtts_voice.py # Voice cloning and speech generation using XTTS
├── lipsync.py # Lip-sync video generation using SadTalker
├── requirements.txt # Python dependencies
├── input/
│ ├── input.pptx # Presentation file
│ ├── input_audio.wav # Reference audio for cloning
│ └── input_image.jpg # Face image for lip-sync
├── output/
│ └── final_video.mp4 # Generated video output
└── README.md # Project documentation


---

#🔧 Setup Instructions
# 1. Clone the Repository
git clone https://github.com/yourusername/AI_Voice.git
cd AI_Voice
# 2. Create and Activate Virtual Environment
python -m venv env
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate
# 3. Install Dependencies
pip install -r requirements.txt

# 📥 Required Inputs
Place the following files in the input/ directory:
-input.pptx — PowerPoint presentation with the script/text
-input_audio.wav — Reference voice sample (~10 seconds preferred)
-input_image.jpg — A clear image of the person for animation
▶️ Run the Project
bash
Copy code
python main.py
The script will:

Extract text from the PPT

Clone the speaker's voice using XTTS

Generate audio from text in the cloned voice

Use SadTalker to create a lip-synced video from the image and audio

✅ Output will be saved to:
- output/final_video.mp4
# 🔗 Dependencies
-Python 3.8+
-Coqui TTS - XTTS
-SadTalker
-python-pptx, librosa, torch, moviepy, etc.
-ffmpeg (must be installed and added to PATH)

# 🧪 Example Use Case

input/
├── input.pptx          # Slides on AI in Education
├── input_audio.wav     # Lecturer’s voice sample
├── input_image.jpg     # Lecturer’s portrait

# After running main.py:
output/
└── final_video.mp4     # Talking lecturer video

# 📌 Future Improvements
 GUI Interface (Tkinter/Web)
 Subtitle auto-generation
 Multi-slide video stitching
 Real-time demo mode

# 📝 Acknowledgements
-💬 Voice Cloning: XTTS by Coqui
-🎥 Lip-sync Animation: SadTalker
-📊 PPT Parsing: python-pptx

# 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
