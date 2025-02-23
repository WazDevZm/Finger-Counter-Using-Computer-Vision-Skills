import cv2
import mediapipe as mp

# Initialize mediapipe hand detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_draw = mp.solutions.drawing_utils

# Camera dimensions
wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

while True:
    success, img = cap.read()

    if not success:
        print("Failed to capture image from camera")
        break

    # Convert the image to RGB for mediapipe
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the image and detect hands
    results = hands.process(imgRGB)

    # Check if any hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw the landmarks on the hand
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Count fingers
            finger_count = 0

            # Thumb (tip is landmark 4, base is landmark 1)
            if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x > hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x:
                finger_count += 1

            # Index (tip is landmark 8, base is landmark 5)
            if hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y:
                finger_count += 1

            # Middle (tip is landmark 12, base is landmark 9)
            if hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y:
                finger_count += 1

            # Ring (tip is landmark 16, base is landmark 13)
            if hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y:
                finger_count += 1

            # Pinky (tip is landmark 20, base is landmark 17)
            if hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y:
                finger_count += 1

            # Display the finger count on the frame
            cv2.putText(img, f'Fingers: {finger_count}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    # Show the result
    cv2.imshow("Finger Counter", img)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
