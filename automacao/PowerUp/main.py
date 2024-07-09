
# pip install python-xlib
# python3 -m pip install pyautogui
# sudo apt-get install scrot
# sudo apt-get install python3-tk
# sudo apt-get install python3-dev

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press('win')
pyautogui.write("firefox")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

print("Executado com sucesso !!!")

pyautogui.press("WIN")