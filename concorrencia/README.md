# CONCORRÊNCIA E PARALELISMO EM PYTHON

Concorrência e Paralelismo na programação Python e como você pode aplicá-los no cotidiano de sua carreira como programador.

## Vá Direto ao Assunto…

- Concorrência vs Paralelismo: Afinal, o que é isso?
- Threading, Multiprocessing e Asyncio
- Desempenho e Escalabilidade

## Concorrência vs Paralelismo: Afinal, o que é isso?
Tanto concorrência quanto paralelismo são técnicas usadas para fazer com que um pedaço de código, ou seja, um programa, execute tarefas de maneira mais eficiente.

Mas eles têm diferenças importantes:

Concorrência é quando dois ou mais trabalhos podem começar, correr e completar em um período de tempo sobreposto.

Em outras palavras, a concorrência acontece quando várias tarefas progridem juntas, mas não necessariamente ao mesmo tempo.

Exemplo de uso da [concorrência](./ex-threading.py):

```bash
from time import time, sleep

def fazer_bolo(tipo):
    print(f'Fazendo bolo {tipo}...')
    sleep(1)
    print(f'Bolo {tipo} feito!')

inicio = time()
fazer_bolo('chocolate')
fazer_bolo('cenoura')

print(f'Tempo total: {time() - inicio}')
```
> A saída será:

    Fazendo bolo chocolate...
    Bolo chocolate feito!
    Fazendo bolo cenoura...
    Bolo cenoura feito!
    Tempo total: 2.0023531913757324

Já paralelismo, por outro lado, é quando duas ou mais tarefas são executadas ao mesmo tempo.

Exemplo de uso do [paralelismo](./ex-paralelismo.py):

```bash
from multiprocessing import Process
from time import time, sleep

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
print(f'Tempo total: {time() - inicio}')
```
E a saída:

    Fazendo bolo cenoura...
    Fazendo bolo chocolate...
    Bolo chocolate feito!
    Bolo cenoura feito!
    Tempo total: 1.0561878681182861

Como pode ver, utilizamos duas bibliotecas diferentes para mostrar exemplos de concorrência (usa método sequencial) e paralelismo (usa multiprocessing.Process para atingir a execução simultânea).

Os benefícios de entender e aplicar esses dois conceitos passam por desempenho, escalabilidade e construção de programas mais responsivos e eficientes.

Contudo, existem desafios no seu uso, principalmente relacionados ao manuseio de recursos compartilhados e questões de segurança.

## Threading, Multiprocessing e Asyncio

- Threading permite a execução simultânea de várias threads dentro de um único processo, sendo ideal para operações I/O-bound (operações de entrada e saída, como leituras/gravações em disco, acesso a banco de dados ou acesso à uma API externa são exemplos), mas limitado pelo Global Interpreter Lock (GIL, explicação aqui embaixo).

- Multiprocessing cria múltiplos processos independentes com seu próprio espaço de memória, perfeito para operações CPU-bound (operações com grande uso de CPU, como cálculos matemáticos, multiplicação de matrizes e etc), pois cada processo pode ser executado em um núcleo diferente do processador, evitando problemas de concorrência.

- Asyncio oferece concorrência usando a sintaxe async/await em uma única thread, ideal para operações I/O-bound que envolvem muita espera, mas não adequado para tarefas que exigem paralelismo verdadeiro em operações CPU-bound.


        Obs.: O GIL (Global Interpreter Lock) é um mecanismo do Python que garante que apenas uma thread execute o código Python por vez, mesmo que o programa tenha múltiplas threads. Imagine o GIL como uma chave que apenas uma thread pode segurar por vez para acessar o interpretador Python. Isso evita que duas threads modifiquem dados ao mesmo tempo e causem problemas. No entanto, isso também significa que, mesmo em um computador com múltiplos núcleos, apenas uma thread pode executar código Python por vez, o que pode limitar a performance em programas que fazem uso intenso de threads.

## Threading, Multiprocessing e Asyncio em Python

Agora veremos esses conceitos aplicados na programação Python!

>Threading

Threading é uma forma de paralelismo que permite que várias operações ocorram simultaneamente dentro de um único processo.

Em Python, o módulo `threading` fornece uma API de alto nível para criar e gerenciar threads.

Exemplo de uso do [threading](./ex-threading.py):

```bash
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
```

No código acima:

Criamos a unidade de trabalho, que no nosso caso será a função worker
Em seguida, criamos as threads com `threading.Thread(target=worker)` e as iniciamos com `t.start()`
Por fim, aguardamos a finalização de todas com `t.join()`

> Multiprocessing

Multiprocessing envolve a criação de novos processos no Sistema Operacional, cada um com seu próprio espaço de memória.

Isso evita problemas de concorrência associados à programação multithreaded, especialmente em sistemas com CPU múltiplos.

Exemplo de uso do [multiprocessing](ex-multiprocessing.py):

```bash
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
```

O código acima é similar ao código que fizemos no exemplo de uso de `threading`.

A diferença está no container que irá executar nosso código: no primeiro, serão múltiplas Threads. No segundo, múltiplos processos serão executados.

> Asyncio

Asyncio é uma biblioteca para escrita de código concorrente usando a sintaxe `async/await` introduzida no Python 3.5.

É especialmente útil para operações de I/O que podem ser aguardadas, como chamadas de rede.

Exemplo de uso do [asyncio](./ex-asyncio.py):

```bash
import asyncio

async def worker():
    print("Tarefa iniciada")
    await asyncio.sleep(2)
    print("Tarefa terminada")

async def main():
    # Criar tarefas
    tasks = [worker() for _ in range(5)]
    
    # Aguardar todas as tarefas terminarem
    await asyncio.gather(*tasks)

# Executar o loop de eventos
asyncio.run(main())

print("Todas as tarefas foram concluídas")
```

Nesse código:

- `async def worker()`: Define uma função assíncrona chamada worker.
- `tasks = [worker() for _ in range(5)]`: Cria uma lista de 5 tarefas worker.
- `await asyncio.gather(*tasks)`: Aguarda todas as tarefas na lista tasks serem concluídas. O asyncio.gather executa todas as tarefas de forma concorrente.
- `asyncio.run(main())`: Executa a função main dentro do loop de eventos asyncio. Isto inicializa a execução assíncrona.

## Comparação entre Threading, Multiprocessing e Asyncio

Threading:

- Usa múltiplas threads dentro do mesmo processo.
- Melhor para operações I/O-bound devido ao Global Interpreter Lock (GIL).
- Menor overhead de criação e destruição de threads comparado a processos.

Multiprocessing:

- Cria processos separados com seu próprio espaço de memória.
- Ideal para operações CPU-bound porque cada processo pode ser executado em um core diferente.
- Evita problemas de concorrência, como race conditions, presentes no threading.

Asyncio:

- Usa um único thread, mas permite executar múltiplas tarefas de forma assíncrona.
- Excelente para operações I/O-bound onde muitas operações de espera são necessárias.
- Não é adequado para operações CPU-bound que necessitam de paralelismo verdadeiro.

Cada uma dessas abordagens tem seu próprio caso de uso ideal, e a escolha entre elas depende da natureza da tarefa a ser executada.

## Desempenho e Escalabilidade

Em Python, o principal fator limitante para concorrência e paralelismo é o Global Interpreter Lock (GIL).

como explicamos anteriormente, o GIL é um mecanismo que sincroniza a execução de threads para evitar conflitos de estado.

Se você começar a experimentar problemas de desempenho com threads e lock contention, pode ser a hora de começar a ver alternativas, tais como processos ou greenlets.

## Conclusão

Concorrência e Paralelismo são técnicas poderosas que, quando usadas corretamente, podem aumentar significativamente a eficiência do seu código Python.

No entanto, elas também apresentam desafios e complexidades adicionais que não devem ser subestimados.

Por isso, quando começar a explorar esses conceitos, comece com um problema pequeno e simples e gradualmente aumente a complexidade à medida que se torna mais confortável.