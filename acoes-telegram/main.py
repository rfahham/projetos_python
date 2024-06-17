import yfinance
import datetime
import time
import requests

ticker = "MXRF11.SA"
start = "2024-06-17"
end = "2024-06-21"
hora_inicial = datetime.time(10, 0)
hora_final = datetime.time(17, 0)
valor_desejado = 10.35

def msg_telegram(ticker: str):

    valor_atual = yfinance.Ticker(ticker).history(start=start, end=end)["Close"]
    valor_atual_atualizado = round(valor_atual.mean(), 2)

    TOKEN = ""
    CHAT_ID = ""

    if (valor_atual_atualizado <= valor_desejado):
        
        message = f"É hora de comprar MXRF11!!! \nO Valor atual é R$ {valor_atual_atualizado}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        print(requests.get(url).json())
        
        print("Fluxo finalizado, encerrando... \n")
        return True
    else:
        print("Fluxo incompleto, continuando. \n")
    return False

print(">>> Iniciando... \n")

while True:
    agora = datetime.datetime.now().time()
    if hora_inicial <= agora <= hora_final:
        msg_telegram(ticker)
        break
    time.sleep(10)