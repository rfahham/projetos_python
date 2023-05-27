import requests

key = "9c67f7fd97e570204447648b096f437b"
cidade = "Petropolis"
pais = "br"
unidade = "metric"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade},{pais}&unit={unidade}&lang=ptbr&APPID={key}"

requisicao = requests.get(link)
requisicao_dics = requisicao.json()
descricao = requisicao_dics['weather'][0]['description']
temperatura = requisicao_dics['main']['temp']
sensacao_termica = requisicao_dics['main']['feels_like']

print(f"A temperatura em {cidade} é de {temperatura}")
print(f"A condição do tempo é: {descricao}")
print(f"A sensação térmica é de: {sensacao_termica}")