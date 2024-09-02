# Declarando a classe Carro
class Carro:
    # atributos
    cor = "Cinza"
    fabricante = "Volkswagen"
    modelo = "Fox"
    ano = 2003
    placa = "frxbr11"

    #método
    def ligar(self):
        print("ligando...")
    
    def parar(self):
        print("parando...")

        

# Instanciando
carro1 = Carro() # Carro1 é um objeto da classe carro
print("Cor do carro:", carro1.cor)
print("Fabricante do carro:", carro1.fabricante)
print("O carro está:")
carro1.ligar()

print("*-"*20)

carro2 = Carro() # Carro2 é um objeto da classe carro

print("Ano do carro:", carro2.ano)
print("A placa do carro:", carro2.placa)
carro2.parar()

