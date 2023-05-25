# Convertendo conteudo de arquivo com letrás minúsculas para letras maiúsculas

with open('arquivo.txt', 'r') as input, open('arquivo2.txt', 'w') as output:
    text = input.readlines()
    uppercase = [t.upper() for t in text]
    output.writelines(uppercase)