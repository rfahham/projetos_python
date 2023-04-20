print("-"*34)
print("Olá, bem-vindo, escolha uma opção:")
print("-"*34)

from datetime import datetime

def validar_data(data_hora):
    try:
        datetime.strptime(data_hora, "%d/%m/%Y  %H:%M")
        return True
    except:
        return False

def adicionar_tarefa(nome, descricao, data, hora, lista):
    lista.append(nome + ";" + descricao + ";" + data + ";" + hora)

def listar_tarefas(lista):
    for i, tarefa in enumerate(lista):
        informacoes = tarefa.split(";")
        print(f"Tarefa número: {i+1}")
        print("-"*30)
        print(f"Nome: {informacoes[0]}")
        print(f"Descrição: {informacoes[1]}")
        print(f"Data: {informacoes[2]}")
        print(f"Hora: {informacoes[3]}")
        print("\n")

def remover_tarefa(indice, lista):
    lista.pop(indice - 1)
    

def editar_tarefa(listas):
    item = int(input("Digite o item a ser editado: "))
    print(item)

lista = []

while True:
    
    print("\n1. Adicionar uma tarefa")
    print("2. Listar tarefas")
    print("3. Remover uma tarefa")
    print("4. Editar uma tarefa")
    print("5. Sair")

    try:
        escolha = int(input("\nEscolha: "))
    except ValueError: 
        print("Opção inválida, escolha um inteiro")
        continue
    
    if(escolha == 1):
        print("-"*22)
        print("Adicionando uma tarefa")
        print("-"*22)
        nome_tarefa = input("Digite o nome da tarefa: ")
        descricao_tarefa = input("Digite a descrição da tarefa: ")
        data_tarefa = input("Digite a data em formato dd/mm/aaaa: ")
        hora_tarefa = input("Digite a hora da tarefa no formato hh:mm: ")

        data_hora = data_tarefa + " " + hora_tarefa

        if(validar_data(data_hora)):

            adicionar_tarefa(nome_tarefa, descricao_tarefa, data_tarefa, hora_tarefa, lista)
            # print(lista)
        else:
            print("Erro, data e hora inválida !!!")
    
    elif(escolha == 2):
        print("-"*39)
        print("A opção escolhida foi listar as tarefas")
        print("-"*39)
        listar_tarefas(lista)
        print("-"*39)
    
    elif(escolha == 3):
        print("-"*40)
        print("A opção escolhida foi remover uma tarefa")
        print("-"*40)
        listar_tarefas(lista)
        try:
            num_tarefa = int(input("Digite o item a ser removido: "))
            remover_tarefa(num_tarefa, lista)
        except ValueError:
            input("Digite o item a ser removido: ")
    
    elif(escolha == 4):
        print("-"*39)
        print("A opção escolhida foi editar uma tarefa")
        print("-"*39)
        editar_tarefa(lista)

    if(escolha == 5):
        print("-"*38)
        print("A opção escolhida foi sair do programa")
        print("-"*38)
        break