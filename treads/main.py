import threading

def funcao_1():
    for i in range(5):
        print("Executando função 1")

def funcao_2():
    for i in range(5):
        print("Executando função 2")
        
thread = threading.Thread(target=funcao_1)
thread.start()

funcao_2()
