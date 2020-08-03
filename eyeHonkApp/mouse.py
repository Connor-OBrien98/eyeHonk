import pyautogui
from sms import water

def select_top_left():
    pyautogui.moveTo(707, 518)
    pyautogui.click()

    pyautogui.moveTo(360, 337, duration=0.5)
    pyautogui.click()

def select_top_right():
    pyautogui.moveTo(707, 518)
    pyautogui.click()

    pyautogui.moveTo(1077, 335, duration=1)
    pyautogui.click()

def select_bottom_left():
    pyautogui.moveTo(707, 518)
    pyautogui.click()

    pyautogui.moveTo(360, 700, duration=1)
    pyautogui.click()

    water()

def select_bottom_right():
    pyautogui.moveTo(707, 518)
    pyautogui.click()

    pyautogui.moveTo(1077, 700, duration=1)
    pyautogui.click()



# select_top_left()
# select_top_right()
select_bottom_left()
# select_bottom_right()