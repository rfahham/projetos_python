def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Digite um número inteiro válido')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu sair')
            return 0
        else:
            return n

def linha(tam = 42):
    return '_' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('Cadastro')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc =leiaInt('\033[32m Sua opção: \033[m')
    return opc