#By Wazungwa Mugala
#I'm a student at the Copperbelt Univesity Studying Computer Science!
#I love God!
#Finger Counter App using Computer Vision, Hand Tracking
#Importing all impossible 
import cv2
import time
import HandTrackingModule as htm
import os


wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set (3, wCam)
cap.set (4, hCam)

#importing our images fromm the files to the project
folderPath = "Images"
myList = os.listdir(folderPath )
print(myList)
overlayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
    
print(len(overlayList))
pTime = 0


detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]
#

while True:
    
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    
    
    if len(lmList) != 0:
       fingers = []
    
    if lmList[tipIds[0]][1] > lmList[tipIds[0]-1] [1]:
        fingers.append(1)
        
    else:
        fingers.append(0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    cv2.imshow("Computer Vision", img)
    cv2.waitKey(1)