import cv2
import mediapipe as mp
import pyttsx3
import time

# Initialize mediapipe hand detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)  # Process only one hand for performance

mp_draw = mp.solutions.drawing_utils

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speech rate for smoother output
engine.setProperty('volume', 1)  # Max volume

# Camera dimensions (higher resolution)
wCam, hCam = 720, 720  # Increase webcam resolution

# Set the camera feed resolution and frame rate limit
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
cap.set(cv2.CAP_PROP_FPS, 30)  # Limit FPS to 30 for smooth performance

# Initialize variables
last_finger_count = -1  # To store the last detected finger count
last_time = time.time()  # To track the time between speech

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image from camera")
        break

    # Resize image for better performance (optional, can remove if not needed)
    # img = cv2.resize(img, (wCam // 2, hCam // 2))  # Resize to half size

    # Convert the image to RGB for mediapipe
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the image and detect hands
    results = hands.process(imgRGB)

    # Initialize finger count
    finger_count = 0

    # Check if any hands are detected
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]  # Process only the first hand
        # Draw the landmarks on the hand
        mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Count fingers (exclude the thumb)
        # Index
        if hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y:
            finger_count += 1

        # Middle
        if hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y:
            finger_count += 1

        # Ring
        if hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y:
            finger_count += 1

        # Pinky
        if hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y:
            finger_count += 1

    # Display the finger count on the frame
    cv2.putText(img, f'Fingers: {finger_count}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    # Only speak if the finger count has changed and enough time has passed
    current_time = time.time()
    if finger_count != last_finger_count and current_time - last_time >= 1:  # 1-second interval
        engine.say(f"The number of fingers is {finger_count}")
        engine.runAndWait()  # Speak the number
        last_finger_count = finger_count  # Update the last finger count
        last_time = current_time  # Update the time

    # Show the result
    cv2.imshow("Finger Counter", img)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
