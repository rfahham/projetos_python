# python3 -m venv ./venv && source venv/bin/activate
# pip3 install requests

import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

print(requisicao)
print(requisicao.json())