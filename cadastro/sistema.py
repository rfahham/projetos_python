from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'arquivo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Listar", "Novo", "Excluir", "Sair do sistema"])
    if resposta == 1:
        # Opção de listar o conteúdo do arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastro
        cabecalho("Novo Input no Cadastro")
        nome = str(input("nome: "))
        idade = leiaInt('Idade: ')
        sexo = str(input("sexo: "))
        cadastrar(arq, nome, idade, sexo)
    elif resposta == 3:
        # Excluir um registro do sistema
        cabecalho("Excluindo o registro")
        

    elif resposta == 4:
        # Opção sair do sistema
        cabecalho("Saindo do Sistema")
        break
    else:
        # Digitou uma opção errada no sistema
        cabecalho("\033[31m Erro, digite uma opção válida \033[m")
    sleep(2)
    
