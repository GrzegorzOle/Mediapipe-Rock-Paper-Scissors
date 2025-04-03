# ✋ Rock Paper Scissors Game – Hand Gesture Recognition

This Python project uses your webcam and [MediaPipe](https://google.github.io/mediapipe/) + OpenCV to recognize hand gestures and play a real-time Rock-Paper-Scissors game.

---

## 📦 Requirements

Python 3.8+ and the following libraries:

```bash
pip install opencv-python mediapipe
```

Optional (recommended): create a virtual environment:

```bash
python -m venv .venv

# Activate it:
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```

---

## ▶️ How to Run the Game

After downloading this project and installing dependencies:

```bash
python game.py
```

Make sure your **webcam is connected and not in use** by other apps.

---

## 🎮 Game Controls

- Press `n` → Start **new round**
- Press `q` → **Quit** the game

---

## ✋ Gestures Detected

- ✊ **Rock** – All fingers folded
- ✋ **Paper** – All fingers extended
- ✌️ **Scissors** – Only index + middle fingers extended

---

## 🧠 How It Works

- Uses MediaPipe Hands for hand detection and classification
- Uses OpenCV to show video and draw hand landmarks
- 5-second countdown before gesture evaluation
- Detects both hands and shows gesture + game result

[![Video on YouTube](https://img.youtube.com/vi/90BWIiX7B3s/hqdefault.jpg)](https://youtu.be/90BWIiX7B3s)
---

## 📸 Tips for Better Detection

- Keep both hands **clearly in frame**
- Ensure **good lighting** and camera focus
- Don’t move hands during the countdown
- Avoid overlap between hands

---

## 🔄 Reinstall or Repair

If gesture detection fails or GUI doesn’t display, try:

```bash
pip uninstall opencv-python mediapipe
pip install opencv-python mediapipe
```

---

## 📄 License

MIT License © 2025  
Rock Paper Scissors using OpenCV + MediaPipe
