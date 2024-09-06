print("-"*50)
print("Clínica !!!")
print("-"*50)
print("")

def clinic():
    
    print("Seja Bem-Vindo!!!")
    print("Você acabou de entrar na clinica!")
    print("Você entra pela porta a esquerda (left) ou a direita (right)?")

    answer = input("Digite left (esquerda) ou right (direita) e pressione 'Enter'. ").lower()
    
    if answer == "left" or answer == "l":
        print("Esta é a sala de Abuso Verbal, seu monte de caca de papagaio!")
    elif answer == "right" or answer == "r":
        print("É claro que esta é a 'Sala das Discussões'. Eu já disse isso!")
    else:
        print("Você não escolheu esquerda ou direita. Tente de novo.")
        clinic()

clinic()