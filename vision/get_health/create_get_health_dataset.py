import mss
import cv2
import numpy as np
import time
import os
from vision.vision_service.vision_service import get_health_window_coords

# Ensure folder exists
folder = "vision/training_data/get_health/photos"
os.makedirs(folder, exist_ok=True)

i = 38
with mss.mss() as sct:
    while True:
        time.sleep(5)
        window = get_health_window_coords()
        print(window)
        screenshot = np.array(sct.grab(window))
        img= cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
        filename = os.path.join(folder, f"frame{i}.png")
        cv2.imwrite(filename, img)
        print(f"Saved {i}")
        i += 1
