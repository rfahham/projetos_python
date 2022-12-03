print("-"*40)
print("  Calcula a média das notas informadas")
print("-"*40)
print("")

cores = {
    'verde' : '\033[1;32m',
    'vermelho' : '\033[1;31m',
    'limpa' : '\033[m'
    }

nome = input("Insira o nome do aluno: ")
nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
nota3 = int(input("Insira a terceira nota: "))
nome = "Ricardo"

notas=[nota1, nota2, nota3]
media = sum(notas) / len(notas)
print("A média das notas do aluno {} é {}: ".format(nome, media))
print("")

if (media >= 6):
    resultado = "Aprovado"
    print("O aluno {} foi : {}{}{}".format(nome, cores['verde'], resultado, cores['limpa']))
    print("")
else:
    resultado = "Reprovado"
    print("O aluno {} foi : {}{}{}".format(nome, cores['vermelho'], resultado, cores['limpa']))
    print("")