import pyautogui

pyautogui.hotkey('ctrl', 'shift', 't')

pyautogui.hotkey('ctrl', 'n')

with pyautogui.hold('ctrl'):
        pyautogui.press(['alt', 't'])

pyautogui.click(x=626, y=626)