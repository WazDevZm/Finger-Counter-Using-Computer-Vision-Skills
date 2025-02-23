# By Wazungwa Mugala
# I'm a student at the Copperbelt University Studying Computer Science!
# I love God!
# Finger Counter App using Computer Vision, Hand Tracking

import cv2
import HandTrackingModule as htm
import os
import time

# Camera dimensions
wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Import images from folder
folderPath = "Images"
myList = os.listdir(folderPath)
print("Images Found:", myList)

overlayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    
    # Resize image to fit (200x200)
    image = cv2.resize(image, (200, 200))
    
    overlayList.append(image)

print("Total Overlays Loaded:", len(overlayList))
PTime = 0

while True:
    success, img = cap.read()
    
    if not success:
        print("Failed to capture image from camera")
        break

    # Check if overlay list is not empty
    if len(overlayList) > 0:
        h,w,c = overlayList[0].shape
        img[0:200, 0:200] = overlayList[3]  # Place resized overlay on frame
        cTime = time.time()
        fps = 1/(cTime - PTime)
        cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)
    cv2.imshow("Computer Vision", img)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
