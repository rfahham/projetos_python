# PROGRESS BAR

## Instalar as dependências

```bash
pip install requirements
```

Executa requisição GET para um site e mostra a barra de progresso em tempo real.

    from tqdm import tqdm
    import time

    # forma mais simples
    for i in tqdm(range(10)):
        time.sleep(1)


Uma segunda forma

    with tqdm(total=100) as barra_progresso:

        for i in range(10):

            time.sleep(1)
            
            barra_progresso.update(10)