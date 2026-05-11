from vision.vision_service.vision_service import get_health, get_movement
import time

while "screenshotting":
    health = get_health()
    movement = get_movement()
    movementMap = {
        0:"standing",
        1:"jumping",
        2:"moving right",
        3:"falling",
        4:"moving left"}
    print("health", health)
    print("movement", movementMap[movement])

    time.sleep(2)