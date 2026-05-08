from vision.vision_service.vision_service import get_health
import time

while "screenshotting":
    health = get_health()

    print("health", health)

    time.sleep(5)