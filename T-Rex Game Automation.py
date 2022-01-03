import numpy as np
import cv2
from mss import mss
from pynput.keyboard import Key, Controller

keyboard = Controller()

bounding_box = {'top': 460, 'left': 255, 'width': 3, 'height': 3}

sct = mss()
color = (83,83,83,255)
hex = "#535353"

day = np.array([[255, 255, 255],
       [255, 255, 255],
       [255, 255, 255]])

night =np.array([[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]])

while True:
    sct_img = sct.grab(bounding_box)
    colored = cv2.cvtColor(np.array(sct_img), cv2.COLOR_RGB2BGR)

    cv2.imshow('screen', colored)
    rgb = np.array(colored)
    rgb = np.array(rgb[0])
    # print(rgb)

    if  (rgb != day).all():
        print("Arrow")
        keyboard.press(Key.up)
        keyboard.release(Key.up)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
