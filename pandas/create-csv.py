import pandas as pd

# Dados para o DataFrame

dados = {
    'nome': ['João Ricardo', 'João Victor', 'Andreza'],
    '1 Trimestre': [8, 8, 6],
    '2 Trimestre': [9, 7, 8],
    '3 Trimestre': [9, 9, 9],
    '4 Trimestre': [7, 8, 8]
}

# dados = {
#     'nome': ['Alice', 'Bob', 'Carlos', 'Diana'],
#     'idade': [30, 25, 35, 28],
#     'email': ['alice@example.com', 'bob@example.com', 'carlos@example.com', 'diana@example.com']
# }

# Criar o DataFrame
df = pd.DataFrame(dados)

# Salvar o DataFrame como arquivo CSV
df.to_csv('dados.csv', index=False)