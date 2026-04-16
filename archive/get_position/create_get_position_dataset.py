import mss
import cv2
import numpy as np
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vision_service import get_window_coords
#ensure folder exists
folder = "vision/get_position/testing_data/photos"
os.makedirs(folder, exist_ok=True)

i = 1
with mss.mss() as sct:
    while True:
        time.sleep(5)
        window = get_window_coords()
        screenshot = np.array(sct.grab(window))
        img= cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
        filename = os.path.join(folder, f"frame{i}.png")
        cv2.imwrite(filename, img)
        print(f"Saved {i}")
        i += 1
