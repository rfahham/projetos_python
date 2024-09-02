import pyautogui
pyautogui.PAUSE=1 # dá uma pausa de 1 segundo entre os procedimentos seguintes, é importante na medida em que o computador pode demorar algum tempo a abrir as páginas
pyautogui.press('win') # clica na tecla win
pyautogui.write('firefox') #na barra de pesquisa escreve firefox, se tiver o firefox instalado e for o chrome troque por chrome
pyautogui.press('enter') # prime a tecla enter
pyautogui.press('backspace') # este é um promenor para abrir a pagina do browser
pyautogui.press('shift') # seleciona a barra de pesquisa do browser
pyautogui.write('google.com') # escreve na barra de pesquisa google.com
pyautogui.press("enter") # prime a tecla enter
pyautogui.write("pyautogui") #escreve na barra de pesquisa do ggogle a palavra pyautogui
pyautogui.press("enter") # prime a tecla enter
pyautogui.click(x=319, y=329) #clica no primeiro link que aparece da pesquisa que é a documentação do pyautogui