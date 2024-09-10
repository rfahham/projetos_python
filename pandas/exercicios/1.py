# Se você precisar aplicar uma função a cada linha, pode usar apply() com o parâmetro axis=1. Isso é útil para operações que exigem manipulação ou transformação de dados.

import pandas as pd

# Criar um DataFrame de exemplo
data = {
    'nome': ['Alice', 'Bob', 'Carlos', 'Diana'],
    'idade': [30, 25, 35, 28],
    'email': ['alice@example.com', 'bob@example.com', 'carlos@example.com', 'diana@example.com']
}

df = pd.DataFrame(data)

# Definir uma função para aplicar a cada linha
def processar_linha(linha):
    nome = linha['nome']
    idade = linha['idade']
    email = linha['email']
    print(f"Nome: {nome}, Idade: {idade}, Email: {email}")

# Aplicar a função a cada linha
df.apply(processar_linha, axis=1)
