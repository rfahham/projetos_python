# projetos_python

Todos os projetos feitos com python

## Instalar o env

```bash
sudo apt install python3.10-venv
```

## Isolar o ambiente:

```bash
python3 -m venv ./venv && source venv/bin/activate
```

## Salvar os requirements em um arquivo

```bash
pip3 freeze > requirements.txt
```

## Instalando os requeirementes a partir do arquivo

```bash
pip install -r requirements.txt
```
## Sair do ambiente

```bash
deactivate
```
## Atualizando todos os pacotes do requirements.txt da sua app Python

```bash
pip install upgrade-requirements
upgrade-requirements
pip freeze > requirements.txt
```