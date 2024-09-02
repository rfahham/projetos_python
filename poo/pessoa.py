class Pessoa:
    # atributos
    nome = "Ricardo"
    sobrenome = "Fahham"
    idade = 51
    nacionaldade = "Brasileira"

    def dizer_ola(self, nome):
        print("Olá!")

# pessoa1 e pessoa2 são objetos
pessoa1 = Pessoa()
pessoa2 = Pessoa()

pessoa1.dizer_ola()

