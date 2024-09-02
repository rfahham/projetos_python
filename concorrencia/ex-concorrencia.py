from time import time, sleep

print("-"*28)
print("Trabalhando com CONCORRÊNCIA")
print("-"*28)
print("")

def fazer_bolo(tipo):
    print(f'Fazendo bolo {tipo}...')
    sleep(1)
    print(f'Bolo {tipo} feito!')

inicio = time()
fazer_bolo('chocolate')
fazer_bolo('cenoura')

print("")
print(f'Tempo total de execução foi de: {time() - inicio}')