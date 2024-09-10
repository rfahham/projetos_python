# Python

Gustavo Guanabara diz que este é o primeiro teste...

print("Olá mundo !!!")



## Tipos

- Inteiros (int)
    
    Os inteiros em Python são números inteiros sem parte decimal. 
    Eles podem ser positivos ou negativos. 
    Por exemplo, 10, -5, 0 são exemplos de inteiros em Python.

- Números de ponto flutuante (float)
    
    Os números de ponto flutuante em Python são números com parte decimal. 
    Eles podem representar números reais, como 3.14, -2.5, 0.0.

- Strings (str)
    
    As strings em Python são utilizadas para representar sequências de caracteres. 
    Elas são definidas entre aspas simples ou duplas. 
    Por exemplo, “Olá, mundo!” é uma string em Python.

- Listas (list)
    
    As listas em Python são utilizadas para armazenar uma coleção ordenada de elementos. 
    Elas podem conter diferentes tipos de dados e podem ser modificadas. 
    Por exemplo, [1, 2, 3] é uma lista em Python.

- Tuplas (tuple)

    As tuplas em Python são semelhantes às listas, mas são imutáveis, ou seja, não podem ser modificadas após a sua criação. 
    Elas também podem conter diferentes tipos de dados. 
    Por exemplo, (1, 2, 3) é uma tupla em Python.

- Dicionários (dict)
    
    Os dicionários em Python são utilizados para armazenar dados em pares chave-valor. 
    Cada elemento em um dicionário é acessado por sua chave única. 
    Por exemplo, {“nome”: “João”, “idade”: 30} é um dicionário em Python.

Esses são apenas alguns exemplos dos diferentes tipos de variáveis disponíveis em Python. 
Cada tipo possui suas próprias propriedades e métodos que podem ser utilizados para manipular os dados. 
É importante escolher o tipo de variável adequado para cada situação em seus programas, levando em consideração as necessidades específicas do projeto.

print("Olá mundo !!!")

print(5)
print(5+5)
print(55-5)
print(5*5)
print(5/5)

print("khamsa")

nome = "ricardo"
sobrenome = "fahham"

print(nome, sobrenome)

nota1 = 5
nota2 = 7
nota3 = 9
nota4 = 8

media = (nota1+nota2+nota3+nota4)/4

print(media)

print(nome, sobrenome, "sua nota final foi:", media, "parabéns você passou de ano!!!",)


## Lista

frutas = ["laranja", "banana", "caju"]

print(frutas)

print(frutas[2])

## Adicionar um item na lista

frutas.append("mamão")
print(frutas)

## remover um item da lista

frutas.remove("banana")
print(frutas)

print(nota3 > nota1)

print(nota3 < nota1)

ano = input("digite o ano que vc nasceu: ")
print(ano)
print(type(ano) is int)
print(type(ano) is str)

ano = int(input("digite o ano que vc nasceu: "))

# idade = (2024 - ano)

# print(idade)