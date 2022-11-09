import time
import pyautogui

while True:
    screenShots = [pyautogui.locateCenterOnScreen('file1.jpg'),
    pyautogui.locateCenterOnScreen('file1.jpg')]
    for i in screenShots:
        if i is not None:
            pyautogui.hotkey('ctrl', 'w')
    time.sleep(5)