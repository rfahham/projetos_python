import string
import random

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

senha_forte = gerar_senha() 

print("Sua senha forte é:", senha_forte)