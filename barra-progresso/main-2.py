import time
from tqdm import tqdm

with tqdm(total=100) as barra_progresso:

    for i in range(10):

        time.sleep(1)
            
        barra_progresso.update(10)