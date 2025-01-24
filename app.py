#Finger Counter App using Computer Vision, Hand Tracking
import cv2
import time
import HandTrackingModule as htm


wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set (3, wCam)
cap.set (4, hCam)
