# PriorityQueue: 
# Não segue nenhuma das propriedades acima, FIFO ou LIFO. 
# Esta fila segue o conceito de “ordem de prioridade”. 
# Se os elementos da fila têm prioridades diferentes, então o elemento com alta prioridade é extraído primeiro.
 
import queue

fila_prioridade = queue.PriorityQueue()
fila_prioridade.put((2, "Primeiro da fila"))
fila_prioridade.put((1, "Segundo da fila"))

print(fila_prioridade.get()) 