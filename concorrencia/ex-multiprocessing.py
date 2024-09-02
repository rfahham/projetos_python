import multiprocessing
import time

print("-"*36)
print("Trabalhando com MULTIPROCESSAMENTO")
print("-"*36)
print("")

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

print("")
print("Todos os processos foram concluídos!")