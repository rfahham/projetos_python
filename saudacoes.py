# from colorama import Fore

saudacoes = [
    "Olá !!!",
    "Seja Bem-vindo !!!",
    "Aguarde um momento...",
    "Em breve você será atendido !!!",
    " "
]

from itertools import cycle
from time import sleep

while True:
    for saudacao in cycle(saudacoes):
        # print(Fore.BLUE + saudacao)
        print(saudacao)
        sleep(1)