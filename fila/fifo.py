# FIFO (First-In-First-Out), ou em português, “Primeiro a entrar, primeiro a sair”.
# Queue: É o primeiro tipo de fila. 
# Ele segue a propriedade FIFO onde o primeiro elemento inserido é o primeiro a ser extraído.

import queue

fila_FIFO = queue.Queue()
fila_FIFO.put("Primeiro da fila")
fila_FIFO.put("Segundo da fila")

print(fila_FIFO.get()) 