from time import sleep
import pyautogui
sleep(5)
x = pyautogui.position()
while True:
    if x == pyautogui.position():
        pyautogui.click(x)
        sleep(0.001)
    else:
        break
