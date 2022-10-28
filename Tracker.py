"""
This is a demo file that uses our created module
"""

import cv2
import mediapipe as mp
import time
import Hand_Tracking_Module as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)  # Creating out video object using cam No. 0
detector = htm.handDetector()
while True:
    success, img = cap.read()  # This gives us our frame
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (25, 200, 25), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)