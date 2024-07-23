import threading
import time

def worker():
    print("Thread iniciada")
    time.sleep(2)
    print("Thread terminada")

# Criar threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

# Aguardar todas as threads terminarem
for t in threads:
    t.join()

print("Todas as threads foram concluídas")