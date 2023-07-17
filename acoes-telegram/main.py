from request import get
import yfinance as yf
import datetime
import time

nome_ativo = "MXRF11"
valor_desejado = 10.69

hora_inicial = datetime.time(10, 0)
hora_fial = datetime.time(17, 0)

def msg_telegram(nome_ativo: str):
    CHAVE_API = ""
    BOT_CHAT_API = "chat_id_tiktok"

    valor_atual = yf.Ticker(f"{nome_ativo}.SA").history(per)
    valor_atual_atualizado = valor_atual['Close'][-1]

    if (valor_atual_atualizado <= valor_desejado):
        mensagem = f"Hora de comprar MXRF11 !!! {str{nome_ativo.upper()}}CAIU\n Valor atual: {valor valor_atual}"
        url_mensagem = f"https://api.telegram.org/bot{CHAVE_API}/sendMessage?chat_id-{BOT_CHAT_API}&parse_mode-Markdown"

        print(f"{mensagem}\n")
        get(url_mensagem)
        print("Fluxo finalizado, encerrando. \n")
        return True
    else:
        print("Fluxo incompleto, continuando. \n")
    return False

print(">>> Iniciando...")

while True:
    agora = datetime.datetime.now().time()
    if hora_inicial <= agora <= hora_final:
        if msg_telegram(nome_ativo):
            break
    time.sleep(300)

