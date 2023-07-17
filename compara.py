# Compara duas strings

string1 = "Orquestração de containers com Kubernetes"

string2 = "Orquestração de containers sem Kubernetes"

conjunto = enumerate(zip(string1, string2))
print(list(conjunto))

for indice, (a, b) in conjunto:
    if a != b:
        print(f"Item errado: {indice}")

