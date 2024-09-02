import pandas as pd
import yfinance as yf
from colorama import Fore

print("Lista de ações:")
print("")
print("0 - PETR4.SA")
print("1 - MXRF11.SA")
print("2 - VGIR11.SA")
print("3 - MCHF11.SA")
print("4 - VGIR11.SA")

print("")

opcao = int(input("Digite a Ação desejada: "))
dias = input("Digite o número de dias: ")
acao = ["PETR4.SA", "MXRF11.SA", "VGIR11.SA", "MCHF11.SA", "VGIR11.SA"]
df = yf.Ticker(acao[opcao])
hist = df.history(period = (dias+"d"))
print(Fore.CYAN + "-" * 110)
print(Fore.WHITE + acao[opcao])
print(Fore.CYAN + "-" * 110)
print(hist)
print(Fore.CYAN + "-" * 110)
print(Fore.WHITE + "")