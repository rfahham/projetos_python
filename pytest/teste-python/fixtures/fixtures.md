# fixtures

Uma das grandes funcionalidades do PyTest são as fixtures, que representam tudo o que o teste precisa para fazer o seu trabalho. Ou seja, são funções que você define para moldar uma configuração de testes personalizada. Em um nível bem simples, as funções de teste solicitam fixtures declarando como argumentos, o que torna possível utilizar diversos modelos de entrada de dados em uma função de teste, por exemplo.

Criamos um arquivo `arquivo.py` com uma Classe chamada Fruit

<div align="center">

![Funções](../docs/images/arquivo.png)

</div>

Criamos um arquivo com o teste, sempre começando com `test_`, `teste_arquivo.py`. 

<div align="center">

![](../docs/images/test_arquivo-old.png)

</div>

Podemos observar que as fixtures estão no mesmo arquivo de teste, o que pode ser um problema quando elas ou outros testes existem em grande quantidade. Para resolver isso, podemos utilizar o plugin conftest, que vem junto com o framework que estamos utilizando.

Este plugin nos permite criar um arquivo de configuração para os testes, o que permite concentrarmos tudo que os testes precisam em um único arquivo e tornar os módulos de teste mais limpos e práticos, conforme exemplo abaixo:

As fixtures ficarão separadas da função de teste

<div align="center">

![](../docs/images/conftest.png)

</div>

O arquivo `test_arquivo.py` agora fica só com a função que será testada.

<div align="center">

![](../docs/images/test_arquivo.png)

</div>


Executando o teste

<div align="center">

![Executando o teste](../docs/images/exec-pytest.png)

</div>

Para que você consiga gerar os relatórios de cobertura, realize o comando dentro do diretório de testes, resultando no relatório exemplificado abaixo:

```bash
pytest
```
