# import pandas as pd
# import yfinance as yf
# from colorama import Fore

acao = "MXRF11.SA"

# df = yf.Ticker(acao)
# hist = df.history(period = ("1"+"d"))
# print(Fore.CYAN + "-" * 110)
# print(Fore.WHITE + acao)
# print(Fore.CYAN + "-" * 110)
# print(hist)
# print(Fore.CYAN + "-" * 110)
# print(Fore.WHITE + "")



from chave import key

import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={acao}&apikey={key}'
r = requests.get(url)
data = r.json()

# print(data)
print(data["Weekly Adjusted Time Series"])
