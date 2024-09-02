# LifoQueue: Esta é a fila que segue a propriedade LIFO (Last-In-First-Out) onde o último elemento inserido é o primeiro a ser extraído.

import queue

fila_LIFO = queue.LifoQueue()
fila_LIFO.put("Primeiro da fila")
fila_LIFO.put("Segundo da fila")

print(fila_LIFO.get())  