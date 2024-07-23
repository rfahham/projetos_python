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