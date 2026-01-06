import mss
import numpy as np
import cv2
from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionOnScreenOnly
from PIL import Image
from torchvision import transforms
import torch
from vision.get_health.classes.HealthCNN import HealthCNN

#helper
def _get_window_coords():
    windows = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)

    for w in windows:
        name = w.get("kCGWindowName", "")
        bounds = w.get("kCGWindowBounds", {})
        sharing = w.get("kCGWindowSharingState", 0)
        layer = w.get("kCGWindowLayer", -1)

        if name and name == "Hollow Knight Silksong" and sharing != 0 and layer == 0:
            top = int(bounds.get("Y", 0)) + 30 #remove top bar
            left = int(bounds.get("X", 0))
            width = int(bounds.get("Width", 0))
            height = int(bounds.get("Height", 0)) - 30

            if width > 0 and height > 0:
                return {"top": top, "left": left, "width": width, "height": height}

    return None

def _get_frame():
    if id is None:
        raise ValueError(f"Window not found")
    with mss.mss() as sct:
        while True:
            window = _get_window_coords()
            img = np.array(sct.grab(window))
            cv2.imshow("OpenCV/Numpy normal", img)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()

def _get_health_window_coords():
    window = _get_window_coords()
    window["height"] -= 615
    window["width"] -= 890
    window["left"] += 100
    window["top"] += 47
    return window

def get_health():
    with mss.mss() as sct:
        #take screenshot
        window = _get_health_window_coords()
        screenshot = np.array(sct.grab(window))
        img= cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
        img = Image.fromarray(img)

        #preprocess tensor
        img = img.convert("RGB")
        to_tensor = transforms.ToTensor()
        image = to_tensor(img).unsqueeze(0).float()  #adds batch size to tensor

        #load and pass through model
        model = HealthCNN()  
        model.load_state_dict(torch.load("vision/models/health_cnn.pth"))
        model.eval()
        with torch.no_grad():
            output = model(image)
            probs = torch.softmax(output, dim=1) 
            health = torch.argmax(probs, dim=1).item()
        return health


