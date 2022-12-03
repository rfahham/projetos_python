from pathlib import Path

f = Path(input('Nome do arquivo a ser pesquisado: '))
d = Path(input('Diretório a ser pesquisado: '))

for i in d.rglob('*'):
    if i.name.lower() == f.name.lower():
        if i.is_file():
            print(i)
            