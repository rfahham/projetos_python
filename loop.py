# Agora vamos à explicação:

# {variável iteração}: é o nome da variável que vai receber os elementos do iterável a cada iteração
# {iterável}: é o container de dados sobre o qual vamos iterar, podendo ser: uma lista, uma tupla, um dicionário, entre outros.
# {código}: é o bloco de código que será executado a cada iteração (loop).

# for {nome variável} in {variável iteração}:
    # {código}

print()
print('{:-^20}'.format(''))
print('{:-^20}'.format(' Imprimindo uma lista '))
print('{:-^20}'.format(''))
print()

lista = [1, 2, 3, 4, 5]

for item in lista:
    print(item)

print("")
print("-"*55)
print("O break, para a execução de um loop.")
print("-"*55)
print("")

for item in [1, 2, 3, 4, 5]:
    if item == 3:
        break
    else:
        print(item)

print("Em uma lista com 5 objetos, só imprime a quantidade especificada.")

print("")
print("-"*55)
print("Já o continue serve para pular todo código que estiver abaixo da cláusula continue, dando sequência a próxima iteração do loop.")
print("-"*55)
print("")

for item in [1, 2, 3, 4, 5]:
    if item == 3:
        continue
    print(item)

print("Em uma lista com 5 objetos, o item selecionado 3 é pulado")

print("")
print("-"*55)
print("Loops utilizando for e else")
print("-"*55)
print("")

for item in [1, 2, 3, 4, 5]:
    if item == 6:
        print('Encontramos o 6')
        break
else:
    print('Elemento 6 não foi encontrado')

print("Como o número 6 não está presente na lista, o código em else será executado!")