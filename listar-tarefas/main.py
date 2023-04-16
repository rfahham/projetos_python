print("-"*15)
print("Olá, bem-vindo, escolha uma opção:")
print("-"*15)

while True:
    print("\nMenu:")
    print("1. Adicionar uma tarefa")
    print("2. Listar tarefas")
    print("3. Remover uma tarefa")
    print("4. Editar uma tarefa")
    print("5. Sair")

    try:
        escolha = int(input("Escolha: "))
    except ValueError: 
        print("Opção inválida, escolha um inteiro")
        continue