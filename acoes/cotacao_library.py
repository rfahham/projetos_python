import pandas as pd
import yfinance as yf
from colorama import Fore

print("Lista de ações:")
print("")
print("1 - PETR4.SA")
print("2 - MXRF11.SA")
print("3 - TAEE11.SA")
print("")

opcao = int(input("Digite a Ação desejada: "))
dias = input("Digite o número de dias: ")

acao = {
        1 : "PETR4.SA",
        2 : "MXRF11.SA",
        3 : "TAEE11.SA"
}

df = yf.Ticker(acao[opcao])
hist = df.history(period = (dias+"d"))
print(Fore.CYAN + "-" * 110)
print(Fore.WHITE + acao[opcao])
print(Fore.CYAN + "-" * 110)
print(hist)
print(Fore.CYAN + "-" * 110)
print(Fore.WHITE + "")