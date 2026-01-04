import pyautogui
import time

def jump(self):
    pyautogui.keyDown("z")
    time.sleep(0.5)
    pyautogui.keyUp("z")
    pass

def jump_left(self):
    pyautogui.keyDown("z")
    pyautogui.keyDown("left")
    time.sleep(0.5)
    pyautogui.keyUp("z")
    pyautogui.keyUp("left")
    pass

def jump_right(self):
    pyautogui.keyDown("z")
    pyautogui.keyDown("right")
    time.sleep(0.5)
    pyautogui.keyUp("z")
    pyautogui.keyUp("right")
    pass

def move_left(self):
    pyautogui.keyDown("left")
    time.sleep(0.5)
    pyautogui.keyUp("left")
    pass

def move_right(self):
    pyautogui.keyDown("right")
    time.sleep(0.5)
    pyautogui.keyUp("right")
    pass