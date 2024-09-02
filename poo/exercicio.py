class Carro:
    def __init__(self, cor, marca):
        self.cor = cor
        self.marca = marca

c1 = Carro("Cinza", "VolksWagen")
c2 = Carro("Preto", "Ford")

print("Carro 1:")
print("Cor:", c1.cor)
print("Marca:", c1.marca)
print("-"*30)
print("Carro 2:")
print("Cor:", c2.cor)
print("Marca:", c2.marca)