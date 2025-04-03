# ✋ Rock Paper Scissors Game (Hand Gesture Recognition)

This Python project uses **OpenCV** and **MediaPipe** to implement a real-time "Rock Paper Scissors" game using hand gestures captured from your webcam.

## 🧠 How It Works

- The camera captures real-time video.
- MediaPipe detects and tracks up to 2 hands.
- Gestures are recognized as:
  - ✊ `Rock`: All fingers folded.
  - ✋ `Paper`: All fingers extended.
  - ✌️ `Scissors`: Only index and middle fingers extended.
- After a countdown, the game freezes the gestures and shows the winner.

## ▶️ How to Run

1. **Clone or download** this repository.
2. Make sure you have **Python 3.8+** installed.
3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate       # On Linux/macOS
   .venv\\Scripts\\activate        # On Windows
