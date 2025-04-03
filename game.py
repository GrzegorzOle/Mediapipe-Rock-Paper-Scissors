import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize MediaPipe Hands with detection and tracking confidence thresholds.
hands = mp_hands.Hands(
    static_image_mode=False,            # Enables continuous detection from video stream
    max_num_hands=2,                    # Detect up to 2 hands
    min_detection_confidence=0.5,       # Minimum confidence for initial hand detection
    min_tracking_confidence=0.5         # Minimum confidence for tracking landmarks
)

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)   # Set camera resolution width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)   # Set camera resolution height

def count_fingers(hand_landmarks):
    tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky tips
    count = 0
    for tip in tips:
        # Count finger as extended if tip is above PIP joint (in y-axis)
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            count += 1
    # Check if thumb is extended (based on x-axis comparison)
    if hand_landmarks.landmark[4].x > hand_landmarks.landmark[2].x:
        count += 1
    return count

def detect_gesture(hand_landmarks, is_right):
    tips = [8, 12, 16, 20]
    fingers = []
    for tip in tips:
        extended = hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y
        fingers.append(extended)

    index, middle, ring, pinky = fingers

    # Check if thumb is extended based on handedness
    thumb = hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x if is_right else hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x

    if not any(fingers) and not thumb:
        return "Rock"
    elif all(fingers) and thumb:
        return "Paper"
    elif index and middle and not ring and not pinky:
        return "Scissors"
    else:
        return "Unknown"

def decide_winner(gesture1, gesture2):
    rules = {
        "Rock": "Scissors",
        "Scissors": "Paper",
        "Paper": "Rock"
    }
    if gesture1 == gesture2:
        return "Draw"
    elif rules.get(gesture1) == gesture2:
        return "Player 1 Wins"
    else:
        return "Player 2 Wins"

while True:
    countdown = 5
    while countdown > 0:
        ret, frame = cap.read()
        cv2.putText(frame, str(countdown), (250, 200), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 5)
        cv2.imshow("Rock Paper Scissors", frame)
        cv2.waitKey(1000)
        countdown -= 1

    gestures = ["?", "?"]
    hand_labels = ["", ""]
    outcome = "Waiting for two hands..."

    while True:
        ret, frame = cap.read()
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if results.multi_hand_landmarks and results.multi_handedness:
            for idx, (hand_landmarks, handedness) in enumerate(zip(results.multi_hand_landmarks, results.multi_handedness)):
                label = handedness.classification[0].label
                is_right = label == "Right"
                gesture = detect_gesture(hand_landmarks, is_right)
                gestures[idx] = gesture
                hand_labels[idx] = label

                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                x = int(hand_landmarks.landmark[0].x * frame.shape[1])
                y = int(hand_landmarks.landmark[0].y * frame.shape[0])
                cv2.putText(frame, f"{label} - Hand {idx+1}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

            if gestures[0] != "?" and gestures[1] != "?":
                outcome = decide_winner(gestures[0], gestures[1])

        cv2.putText(frame, f"{hand_labels[0]} Hand 1: {gestures[0]}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.putText(frame, f"{hand_labels[1]} Hand 2: {gestures[1]}", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.putText(frame, f"Result: {outcome}", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 3)

        cv2.imshow("Rock Paper Scissors", frame)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('n'):
            break
        elif key & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit()
