import mss
import numpy as np
import cv2
from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionOnScreenOnly


def get_window_coords():
    windows = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)

    for w in windows:
        name = w.get("kCGWindowName", "")
        bounds = w.get("kCGWindowBounds", {})
        sharing = w.get("kCGWindowSharingState", 0)
        layer = w.get("kCGWindowLayer", -1)

        if name and name == "Hollow Knight Silksong" and sharing != 0 and layer == 0:
            top = int(bounds.get("Y", 0)) + 25 #remove top bar
            left = int(bounds.get("X", 0))
            width = int(bounds.get("Width", 0))
            height = int(bounds.get("Height", 0)) - 25

            if width > 0 and height > 0:
                return {"top": top, "left": left, "width": width, "height": height}

    return None

def get_frame():
    if id is None:
        raise ValueError(f"Window not found")
    with mss.mss() as sct:
        while True:
            window = get_window_coords()
            img = np.array(sct.grab(window))
            cv2.imshow("OpenCV/Numpy normal", img)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
    

get_frame()