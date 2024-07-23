import multiprocessing
import time

def worker():
    print("Processo iniciado")
    time.sleep(2)
    print("Processo terminado")

# Criar processos
processes = []
for i in range(5):
    p = multiprocessing.Process(target=worker)
    processes.append(p)
    p.start()

# Aguardar todos os processos terminarem
for p in processes:
    p.join()

print("Todos os processos foram concluídos")