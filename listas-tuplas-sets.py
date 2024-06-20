# Criando Listas, Tuplas e Sets

lista []
tuplas()
sets{}

print("Calculando as notas")

nota_1 = 3
nota_2 = 5
nota_3 = 6
nota_4 = 4
nota_5 = 8

print((nota_1+nota_2+nota_3+nota_4+nota_5)/5)

print("------------------------------------")
notas = [3,5,6,4,8]
print(notas)
print("------------------------------------")

print("Adicionando o número 10 na lista")
notas.append(10)
print(notas)
print("------------------------------------")

print("Quantos ítens tem dentro da lista")
len(notas)

print("------------------------------------")

print("Qual o total das notas")
sum(notas)

print("calcular a média utilizando a lista")

sum(notas)/len(notas)

# Trabalhando com Sets

# Não pode ter valores repetidos
# Não suporta index

set_nota = {3,5,6,4,8}
print(set_nota)

print("------------------------------------")

print("Adicionar um novo valor")

set_nota.add(7)
print(set_nota)
