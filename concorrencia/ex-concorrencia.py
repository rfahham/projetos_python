from time import time, sleep

def fazer_bolo(tipo):
    print(f'Fazendo bolo {tipo}...')
    sleep(1)
    print(f'Bolo {tipo} feito!')

inicio = time()
fazer_bolo('chocolate')
fazer_bolo('cenoura')

print(f'Tempo total: {time() - inicio}')