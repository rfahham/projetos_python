# python3 -m venv ./venv && source venv/bin/activate
# pip3 install requests

import requests

informacao = '{"Idade:": "xx", "Nome": "apagar", "Sobrenome:": "apagado"}'

requisicao = requests.post("https://requests-f7f13-default-rtdb.firebaseio.com/.json", data=informacao)

print(requisicao)
print(requisicao.json())

