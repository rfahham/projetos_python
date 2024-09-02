# Inicializar os atributos

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Ricardo", 51)

print("Nome:", p1.nome)
print("Idade:", p1.idade)

p2 = Pessoa("Alessandra", 48)

print("Nome:", p2.nome)
print("Idade:", p2.idade)