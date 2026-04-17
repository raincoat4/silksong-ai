import mss
import cv2
import numpy as np
import time
import os
import re
from vision.vision_service.vision_service import get_window_coords

# Ensure folder exists
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(BASE_DIR, "training_data", "photos")
os.makedirs(folder, exist_ok=True)
files = os.listdir(folder)
indices = []
if len(files) != 0:
    match = re.search(r"frame(\d+)", files[len(files)- 1])
    i = int(match.group(1))
else:
    i = 0   


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
