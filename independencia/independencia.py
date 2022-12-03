from time import sleep

verde = "\033[1;32m"
amarelo = "\033[1;33m"
azul = "\033[1;96m"
reset = "\033[0;0m"

with open("independencia.txt", "r",) as arquivo:
    hino = arquivo.readlines()

    print()
    print(amarelo,'{:-^40}'.format(''), reset)
    print(verde,'{:-^40}'.format(' Hino da Independência do Brasil '), reset)
    print(amarelo,'{:-^40}'.format(''),reset)
    print()

    for linha in hino:
        print(azul, linha, reset)
        sleep(2)
    print()

