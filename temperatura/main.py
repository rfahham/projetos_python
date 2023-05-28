import requests

key = input("Digite chave: ")
cidade = input("Digite a cidade: ")
pais = "br"
unidade = "metric"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade},{pais}&units={unidade}&lang=ptbr&APPID={key}"

# print(link)

requisicao = requests.get(link)
requisicao_dics = requisicao.json()
descricao = requisicao_dics['weather'][0]['description']
temperatura = requisicao_dics['main']['temp']
sensacao_termica = requisicao_dics['main']['feels_like']

print("-"*50)
print(f"A temperatura em {cidade} é de {temperatura} graus")
print(f"A condição do tempo é: {descricao}")
print(f"A sensação térmica é de: {sensacao_termica} graus")
print("-"*50)