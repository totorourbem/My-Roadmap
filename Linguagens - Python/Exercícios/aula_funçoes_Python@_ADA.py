# -*- coding: utf-8 -*-
"""Aula Funçoes 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14P811HczQ9r-Bsj7RhT5QBeZmp7S72Fm

## Elementos individuais de listas

Muitas vezes, precisamos acessar elementos individuais de listas, o que é possível de ser feito a partir de sua indexação.

Sabendo disso, crie uma função retornaPenultimoEQuartoElementodeLista() que recebe uma lista e retorne o quarto e o penúltimo elemento desta lista, nesta ordem.
"""

def retornaPenultimoEQuartoElementodeLista(tuplaA):
	recorteLista = [tuplaA[3], tuplaA[-1]]
	return recorteLista

lista = [1, 2, 3 , 4, 5, 6]

retornaPenultimoEQuartoElementodeLista(lista)

"""## Indexação de listas e último elemento

Uma lista possui n elementos, sendo comum executarmos determinadas ações em um elemento de determinada posição. Por exemplo, podemos substituir o elemento da primeira posição da lista por outro valor desejado. Quando selecionamos um elemento, chamamos isto de indexação.

Sendo assim, escreva uma função ultimoElemento() em python que recebe uma lista e retorna o último elemento da lista.
"""

lista = [1, 2, 3]

def ultimoElemento(listaA):
	return listaA[-1]

ultimoElemento(lista)

"""## Ordenando listas
Em um sistema, comumente utilizamos listas para armazenamento de dados. Entretanto, existem casos em que torna-se necessário criarmos um padrão de organização dos dados. Por exemplo, podemos organizar um cadastro de clientes pela idade destes usuários. Este procedimento de organização é conhecido como ordenação.

Sabendo disso, crie uma função chamada ordena_lista() que recebe uma lista de elementos e ordene-os em ordem decrescente. A função possui como parâmetro a lista a ser ordenada e retorna a mesma lista ordenada de forma decrescente.
"""

def ordena_lista(listaA):
	listaA.sort(reverse=True)
	return listaA


lista = [1, 2, 3, 4, 5]

ordena_lista(lista)

"""## Remover elementos de listas
Considere que uma empresa desenvolveu uma aplicação que solicita ao usuário uma dada informação, como, por exemplo, o segundo nome deste usuário. O programa recebe essa informação e armazena em uma lista de strings. Entretanto, caso um usuário acidentalmente não tenha preenchido esta informação, a lista conterá elementos vazios. Por exemplo, dada uma lista com 5 nomes: listaDeNomes = ['Araújo', 'Alexandre', 'Silva', 'Flávio', ''], note que o último elemento da lista é apenas uma string vazia representada pelas aspas vazias.

Sabendo disso, faça uma função removerElementosVazios() que recebe uma lista de nomes e retorna a lista sem os elementos vazios.
"""

def removerElementosVazios(listaA):
	return [i for i in listaA if i != ""]

listaDeNomes = ['Araújo', 'Alexandre', 'Silva', 'Flávio', '']

removerElementosVazios(listaDeNomes)

"""## Slice
Apesar de utilizarmos listas para armazenar vários elementos, existem situações em que precisamos utilizar apenas parte desta lista. Por exemplo, podemos guardar em uma lista de 30 elementos com o registro do preço do dólar a cada dia nos últimos 30 dias. Posteriormente, podemos querer visualizar o custo do dólar apenas nos últimos 7 dias, para isso pegando os últimos 7 elementos da lista ao invés de 30.

Em python, quando selecionamos partes da lista, denominamos esta operação de slicing, podendo ser realizada não apenas para seleção dos últimos elementos da lista, como também elementos em qualquer posição da lista.

Sabendo disso, crie uma função particionarLista() em python que recebe uma lista e retorne apenas os elementos das posições 5 até 12.
"""

def particionarLista(listaA):
	return listaA[5:13]

precos_janeiro = [100, 102, 98, 100, 101, 99, 100, 102, 101, 100, 98, 97, 98, 100, 101, 102, 100, 99, 98, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]

particionarLista(precos_janeiro)

"""## Adicionar elementos em listas
Quando utilizamos listas, uma das vantagens é que podemos adicionar novos elementos com o passar do tempo. Podemos inserir elementos tanto ao final da lista, como também em uma posição específica.

Sabendo disso, faça uma função adicionarElemento() que recebe uma lista de números e insere o número inteiro 42 no meio da lista (isto é, em sua posição central). Note que a posição de inserção pode variar a depender da quantidade de elementos na lista original.
"""

def adicionarElemento(listaA):
  meio = len(listaA) // 2
  for item in range(len(listaA)):
    if item == meio:
      listaA.insert(item, 42)
  return (listaA)

precos_janeiro = [100, 102, 98, 100, 101, 99, 100, 102, 101, 100, 98, 97, 98, 100, 101, 102, 100, 99, 98, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]

adicionarElemento(precos_janeiro)

"""## Elemento e índice

Em python, muitas vezes é útil iterarmos tanto pelos elementos quanto pelos índices de listas. Sabendo disso, crie uma função calculaPotencia() que recebe uma lista A e retorna uma lista B, tal que os elementos desta lista sejam iguais aos elementos da lista A elevado a potência igual ao índice do respectivo elemento.

Por exemplo, dado uma lista A = [2,5,6], gere uma lista B = [2^0, 5^1, 6^2].
"""

def calculaPotencia(listaA):
    listaB = []
    for i, valor in enumerate(listaA):
      listaB.append(valor ** i)
    return listaB

A = [2,5,6]

calculaPotencia(A)

listaB = [valor ** i for i, valor in enumerate(A)]
print(listaB)

"""## Função zip
Em programação, podemos fazer uso de diferentes listas para armazenar nossos dados para, posteriormente, unir informações destas listas. Por exemplo, podemos guardar em uma lista os nomes de funcionários de uma empresa e, em outra lista, os cargos que estes funcionários ocupam.

```
funcionarios = ["Paulo", "Andrea", "Marta"]
profissao = ["cientista de dados", "engenheiro de dados", "desenvolvedor"]
```
Dado essas duas listas, podemos querer exibir as duas informações conjuntamente da seguinte forma:

`[('Paulo', 'cientista de dados'), ('Andrea', 'engenheiro de dados'), ('Marta', 'desenvolvedor')]`

Podemos fazer isto por meio da função zip que recebe as duas listas e retorna uma saída como exposta acima. Além de exibir os valores, podemos fazer uso da função zip para diversas funcionalidades. Sabendo disso, crie uma função ultimoElementoLista2D() que receba uma lista de duas dimensões (isto é, uma lista de listas, na forma de matriz) e utilize o zip para retornar o último elemento de cada sublista.

Por exemplo, se tivermos a lista abaixo:

[[192, 193, 194],
 [507, 508, 509],
 [526, 527, 528, 529],
 [560, 561],
 [635, 636, 637]]
Retorne [194, 509, 529, 561, 637].
"""

lista_de_lista = [[192, 193, 194], [507, 508, 509], [526, 527, 528, 529], [560, 561], [635, 636, 637]]

def ultimoElementoLista2D(lista):

 lista_zipada = []

 for sublista in lista:
   lista_zipada.append(sublista.pop())

 return lista_zipada

ultimoElementoLista2D(lista_de_lista)

listazipada = [sublista[-1] for sublista in lista_de_lista]

print(listazipada)