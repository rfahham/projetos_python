# Filas em Python

Nativa no Python, basta importá-la com a declaração import queue. O módulo queue do Python oferece três tipos de classes: Queue, LifoQueue e PriorityQueue:

> Queue: É o primeiro tipo de fila. Ele segue a propriedade FIFO onde o primeiro elemento inserido é o primeiro a ser extraído.

> LifoQueue: Esta é a fila que segue a propriedade LIFO (Last-In-First-Out) onde o último elemento inserido é o primeiro a ser extraído.

> PriorityQueue: Não segue nenhuma das propriedades acima, FIFO ou LIFO. Esta fila segue o conceito de “ordem de prioridade”. Se os elementos da fila têm prioridades diferentes, então o elemento com alta prioridade é extraído primeiro.

Por exemplo, essa seria a sintaxe básica para cada tipo de fila:

```bash
import queue

fila_fifo = queue.Queue()
fila_lifo = queue.LifoQueue()
fila_prioridade = queue.PriorityQueue()
```

## Gerenciamento de Filas

Com a biblioteca queue, pode-se adicionar elementos na fila utilizando o método put e remover utilizando o método get.

```bash
import queue

fila = queue.Queue()
fila.put("Primeiro da fila")
fila.put("Segundo da fila")

print(fila.get())
```

E a saída será:

> Primeiro da fila

## FIFO, LIFO, Priority Queue

Como já discutimos, quando utilizamos filas, temos três abordagens principais: FIFO, LIFO e Priority Queue. Veja a diferença entre elas:

### Exemplo de FIFO

```bash
fila_FIFO = queue.Queue()
fila_FIFO.put("Primeiro da fila")
fila_FIFO.put("Segundo da fila")
print(fila_FIFO.get())  
```

Saída será: 

> Primeiro da fila

### Exemplo de LIFO

```bash
fila_LIFO = queue.LifoQueue()
fila_LIFO.put("Primeiro da fila")
fila_LIFO.put("Segundo da fila")
print(fila_LIFO.get())  
```
Saída será: 

> Segundo da fila

### Exemplo de PriorityQueue

```bash
fila_prioridade = queue.PriorityQueue()
fila_prioridade.put((2, "Primeiro da fila"))
fila_prioridade.put((1, "Segundo da fila"))
print(fila_prioridade.get())  
```

Saída será: 
> (1, 'Segundo da fila')
