# sudo apt-get install python3-tk python3-dev
# touch ~/.Xauthority
# xauth add ${HOST}:0 . $(xxd -l 16 -p /dev/urandom)
# xauth list
# DESKTOP-059018K.:0  MIT-MAGIC-COOKIE-1  fc5ac2ca5f1262c0751b120446e11dfa
# pip install pyautogui

import pyautogui

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

