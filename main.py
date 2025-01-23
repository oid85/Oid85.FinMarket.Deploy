import pyautogui
import time


def do():
    while True:
        pyautogui.moveTo(1000, 500)
        pyautogui.click()
        time.sleep(10)
        pyautogui.moveTo(1500, 700)
        pyautogui.click()
        time.sleep(30)


if __name__ == '__main__':
    do()
