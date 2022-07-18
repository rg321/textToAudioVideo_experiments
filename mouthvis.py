import cv2
import os
import time


## Importing all the mouth images
mouths = {}
for i in os.listdir("./Mouths"):
    if i.endswith(".jpg"):
        img = cv2.imread("./Mouths" + "/" + i, 0)
        mouths["" + i] = img
        continue

## Ploting them as an animation
for key,value in mouths.items():
    ### Fast mouth showing
    cv2.imshow('window', value)
    cv2.waitKey(1)
    time.sleep(0.2)




