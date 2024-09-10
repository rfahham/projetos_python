# Executando múltiplos testes

## Criar uma pasta para os testes `tests`

Escrever todos os testes nesta pasta

test_soma.py

<div align="center">

![Soma](../../images/soma.png)

</div>

test_subtrai.py

<div align="center">

![Subtrai](../../images/subtrai.png)

</div>

test_multiplica.py

<div align="center">

![Multiplica](../../images/multiplica.png)

</div>

test_divide.py

<div align="center">

![Divide](../../images/divide.png)

</div>

## Crie dois arquivos na pasta raiz do projeto: 

O primeiro (setup.cfg), deve instruir ao pytest apenas arquivos que comecem com o nome test_ dentro de uma pasta chamada tests e que ao fim da execução, gere um relatório html. 

setup.cfg

<div align="center">

![Divide](../../images/setup.png)

</div>

O segundo (setup.py) deve informar os requerimentos da suíte de testes.

setup.py

<div align="center">

![Divide](../../images/setup2.png)

</div>

Executar o fora da pasta onde estão os `test_`

```bash
pytest
```

Resultado do teste

<div align="center">

![Divide](../../images/multiplos-testes.png)

</div>

Página `report.html`

<div align="center">

![Divide](../../images/report-html.png)

</div>