# python3 -m venv ./venv && source venv/bin/activate
# pip3 install requests

import requests

informacao = '{"Idade:": 22, "Nome": "João Ricardo", "Sobrenome:": "Santana Fahham"}'

requisicao = requests.patch("https://requests-f7f13-default-rtdb.firebaseio.com/-N9IzxyYWl5jiDvFWnmg.json", data=informacao)

print(requisicao)
print(requisicao.json())

