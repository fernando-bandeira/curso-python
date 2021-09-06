"""
MÓDULOS PYTHON
-módulos são arquivos escritos em linguagem Python que podem ser importados em um programa para realização de ações específicas por meio de seus métodos (funções) e atributos (variáveis que guardam um valor)
-exemplos: módulo 'random' e módulo 'math'
-é recomendado realizar a importação de módulos na(s) primeira(s) linha(s) de um programa
1. PRIMEIRA MANEIRA DE IMPORTAÇÃO DE UM MÓDULO
-importar um módulo dessa maneira faz com que todos os métodos e atributos (inclusive os que não serão utilizados) desse módulo sejam carregados
sintaxe:
-para realizar a importação: import MÓDULO
-para convocar um método/atributo do módulo: módulo.método/atributo
"""
## MÓDULO 'random' (para realização de ações que envolvam aleatoriedade)
import random
## método randint()
#print(random.randint(0, 100)) #gera um número inteiro aleatório dentro de um intervalo (de 0 a 100, nesse caso)
## método uniform()
#print(random.uniform(0, 10)) #gera um número flutuante aleatório dentro de um intervalo (de 0 a 10, nesse caso)
## método shuffle()
lista = [1, 2, 3, 4, 5, 6]
random.shuffle(lista) #"embaralha" uma lista, colocando seus elementos em posições aleatórias
#print(lista)
## método choice()
#print(random.choice(lista)) #escolhe um item aleatório dentro de um iterável
## método random()
#print(random.random()) #gera um número flutuante aleatório entre 0 e 1

## MÓDULO 'math' (para realização de operações matemáticas mais avançadas)
import math

## métodos sqrt() e pow() (raiz quadrada e potência, respectivamente. essas operações podem ser realizadas através do operador aritmético ** (aula 3))
#print(math.sqrt(4))
#print(math.pow(2, 5)) #2 elevado à quinta potência
## atributo 'pi' (razão entre o perímetro de uma circunferência e seu diâmetro)
pi = math.pi
#print(pi)
## método radians() e degrees() (converte graus em radianos e radianos em graus, respectivamente)
#print(math.radians(30))
#print(math.degrees(pi / 180))
## métodos sin(), cos() e tan() (retornam seno, cosseno e tangente, respectivamente. argumentos devem estar em radianos)
#print(math.sin(math.radians(30)))
#print(math.cos(math.radians(60)))
#print(math.tan(math.radians(45)))
## atributo 'e' (constante "e", número neperiano)
#print(math.e)
## método log() (retorna logaritmo. valor padrão da base é a constante "e")
#print(math.log(32, 2)) #logaritmo de 32 na base 2
#print(math.log(47)) #logaritmo natural de 47 (base "e")
## método factorial()
#print(math.factorial(6)) #retorna o fatorial de um número

## OBS: é possível utilizar um "apelido", chamado de alias, ao se importar um módulo
import random as rd
#print(rd.randint(0, 10)) #o alias deve ser utilizado toda vez que um método/atributo do módulo for convocado

"""
2. SEGUNDA MANEIRA DE IMPORTAÇÃO DE UM MÓDULO (mais recomendada)
-importar um módulo dessa maneira faz com que apenas alguns métodos/atributos específicos sejam carregados
sintaxe:
-para realizar a importação: from MÓDULO import métodos/atributos
-para convocar um método/atributo do módulo: método/atributo
"""
## MÓDULO 'random'
from random import randint
x = randint(1, 10)
#print(x)

## MÓDULO 'math'
from math import pi, degrees, factorial
#print(factorial(degrees(pi) / 30))

## OBS: é possível, dessa maneira, importar o módulo inteiro utilizando o caracter '*'
from random import *
## a diferença entre fazer isso e realizar a primeira maneira de importação mostrada é que dessa forma não é necessário escrever o nome do módulo ao convocar um método/atributo seu
#print(randint(0, 10))

## OBS: também é possível utilizar alias para métodos/atributos específicos
from random import randint as sortint
#print(sortint(0, 10))

from math import sin as seno, radians as rad
#print(seno(rad(30)))

##OBS: a função dir() é capaz de retornar todos os métodos de um módulo
#print(dir(random))
#print(dir(math))

"""
MÓDULOS CUSTOMIZADOS
-tendo em vista que um módulo é um arquivo escrito em linguagem Python, é possível importar arquivos que você criou nessa linguagem como módulos
-variáveis e funções presentes nesses arquivos serão atributos e métodos, respectivamente
-o nome utilizado para a importação é o nome do arquivo, sem extensão
OBS: para um arquivo poder ser aceito como módulo, seu nome deve obedecer às mesmas regras que o nome de variáveis e funções:
1) deve conter apenas letras, números e "_" (sem acentuação, espaços, hífens ou outros caracteres especiais)
2) não deve começar por um número
"""
import aula01_variaveis as aula
#print(aula.nome)

from aula14_funcoes import fibonacci as fib
#print(fib(10))
