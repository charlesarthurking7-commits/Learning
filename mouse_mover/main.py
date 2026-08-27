import pyautogui 
import random

pyautogui.PAUSE = 1

try:   
    while True:
        screenWidth, screenHeight = pyautogui.position()
        x = screenWidth - 1
        y = screenHeight - 1
        pyautogui.moveTo(x, y)
        pyautogui.moveTo(screenWidth, screenHeight)
except KeyboardInterrupt:
    print("end")