from pynput.keyboard import Key, Controller
import pyautogui
import time
keyboard = Controller()
while True:
    pyautogui.keyDown('z')
    time.sleep(0.05)
    pyautogui.keyDown('down')
    pyautogui.press('x')
    pyautogui.keyUp('down')
    pyautogui.keyUp("z")
    time.sleep(0.5)