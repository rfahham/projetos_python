# Compara duas strings
# Neste caso tudo que vem depois do HTTP vai dar erro

string1 = "http://www.globo.com"

string2 = "https://www.globo.com"

conjunto = enumerate(zip(string1, string2))
# print(list(conjunto))

for indice, (a, b) in conjunto:
    if a != b:
        print(f"Item errado: {indice}")

