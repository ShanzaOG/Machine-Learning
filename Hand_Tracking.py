"""
This is a hand tracking project with cv2; media pipe.

"""

import cv2
import mediapipe as mp
import time

# Creating out video object using cam No. 0
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()  # This gives us our frame
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converting our image to RGB
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)

                cv2.circle(img,  # Image
                           (cx, cy),  # Centre
                           15,  # Radius
                           (255, 50, 255),  # Color
                           cv2.FILLED
                           )

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)


