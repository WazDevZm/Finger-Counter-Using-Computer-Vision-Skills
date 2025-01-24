#Finger Counter App using Computer Vision, Hand Tracking
import cv2
import time
import HandTrackingModule as htm
import os


wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set (3, wCam)
cap.set (4, hCam)


folderPath = "Images"
myList = os.listdir(folderPath )
print(myList)


#importing our images fromm the files to the project

while True:
    
    success, img = cap.read()
    cv2.imshow("Computer Vision", img)
    cv2.waitKey(1)