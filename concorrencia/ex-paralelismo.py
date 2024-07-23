from multiprocessing import Process
from time import time, sleep

print("-"*27)
print("Trabalhando com PARALELISMO")
print("-"*27)
print("")

def fazer_bolo(tipo):
    print(f'Fazendo bolo {tipo}...')
    sleep(1)
    print(f'Bolo {tipo} feito!')

inicio = time()
p1 = Process(target=fazer_bolo, args=('chocolate',))  
p2 = Process(target=fazer_bolo, args=('cenoura',))  

p1.start()
p2.start()

p1.join()
p2.join()

print("")
print("Todas as threads foram concluídas!")
print(f'Tempo total de execução foi de: {time() - inicio}')