import pandas as pd

# Criar um DataFrame de exemplo
data = {
    'nome': ['Alice', 'Bob', 'Carlos', 'Diana'],
    'idade': [30, 25, 35, 28],
    'email': ['alice@example.com', 'bob@example.com', 'carlos@example.com', 'diana@example.com']
}

df = pd.DataFrame(data)

# Iterar sobre as linhas usando iterrows()
for index, row in df.iterrows():
    nome = row['nome']
    idade = row['idade']
    email = row['email']
    print(f"Nome: {nome}, Idade: {idade}, Email: {email}")
