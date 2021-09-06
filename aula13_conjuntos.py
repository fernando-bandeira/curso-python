"""
CONJUNTOS
esse tipo de coleção faz referência ao conceito matemático de conjunto
-conjuntos podem conter dados de vários tipos
-conjuntos contabilizam elementos repetidos somente uma vez
-conjuntos não possuem ordem definida
-elementos de conjuntos não são acessíveis a partir do índice, afinal, eles não possuem índice
-os conjuntos são delimitados por chaves {}
"""
pares = {0, 2, 4, 6, 8, 4, 6, 0} #elementos repetidos não geram erro, são apenas ignorados
#print(pares)

## convertendo outros tipos em conjuntos
lista = ['b', 1, 2, 3.5, 4, 2, "a", 2, True, (1, 2)]
conjunto = set(lista)
#print(conjunto)
nome = "fernando"
conjunto = set(nome)
#print(conjunto)
tupla = (1, 2, 3, 5, 7, 11, 13, 7, 3)
conjunto = set(tupla)
#print(conjunto)
sequencia = range(1, 20, 3)
conjunto = set(sequencia)
#print(conjunto)

## adição/remoção de elementos
conjunto = {1, 2, 3}
conjunto.add('4') #adicionando string "4"
#print(conjunto)
conjunto.remove(2) #remove o elemento informado (NÃO EXISTE ÍNDICE)
#print(conjunto)
conjunto.discard(3) #outra forma de remoção, mas essa maneira não retorna erro caso o elemento a ser removido não seja encontrado
#print(conjunto)
conjunto.clear() #limpa o conjunto
#print(conjunto)

## a função sorted() (aula 11) pode retornar uma lista ordenada contendo os elementos do conjunto
conjunto = {"b", "d", "z", "a", "x"}
#print(conjunto)
ordem = sorted(conjunto)
#print(ordem)

## cópias rasa e profunda funcionam como nas listas
conjunto = {1, 2, 3}
copia = conjunto #cópia rasa
copia.add('4')
#print(conjunto)
#print(copia)

conjunto = {1, 2, 3}
copia = conjunto.copy() #cópia profunda
copia.add('4')
#print(conjunto)
#print(copia)

## interseção, união e diferença
impares = {1, 3, 5, 7, 9}
pares = {0, 2, 4, 6, 8}
primos = {2, 3, 5, 7}
#print(impares.intersection(primos)) #interseção entre 'impares' e 'primos'
#print(pares.union(primos)) #união entre 'pares' e 'primos'
#print(impares.difference(primos)) #diferença, ou seja, elementos que estão em 'impares' mas não em 'primos'
## OBS:
## a.intersection(b) sempre é igual a b.intersection(a)
## a.union(b) sempre é igual a b.union(a)
## a.difference(b) sempre é DIFERENTE de b.difference(a), a menos que 'a' e 'b' sejam conjuntos idênticos. nesse caso a diferença é um conjunto vazio

## tamanho, somatório, máximo e mínimo
conj = {4, 3, 5}
#print(len(conj))
#print(sum(conj))
#print(max(conj))
#print(min(conj))
## OBS: reveja as observações sobre as funções sum(), max() e min() na aula 10, sobre listas

## 'compreensão de conjuntos' (set comprehension) é similar à 'compreensão de listas' (list comprehension)
conjunto = {numero for numero in range(10)} #função range()
#print(conjunto)

numeros = {1, 2, 3, 4, 5, 6, 7} #conjunto
dobros = {numero * 2 for numero in numeros}
#print(dobros)

vogais = "aeiou" #string
conjunto = {vogal.upper() for vogal in vogais}
#print(conjunto)

numeros = [1, 2, 3] #lista
quadrados = {numero ** 2 for numero in numeros}
#print(quadrados)

nomes = ("maria", "joão", "pedro", "fernando") #tupla
conjunto = {nome.title() for nome in nomes}
#print(conjunto)

dic = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5} #dicionário
letras = {chave.upper() for chave in dic.keys()}
dobros = {valor * 2 for valor in dic.values()}
#print(letras)
#print(dobros)

## é possível utilizar condicionais
numeros = range(10)
pares = {n for n in numeros if n % 2 == 0}
#print(pares)
pares_dobros = {n if n % 2 == 0 else n * 2 for n in numeros}
#print(pares_dobros)

"""
#exemplo
#formulário de cadastro para passagens aéreas que registra as cidades de origem dos interessados

cidades = ['Paris', 'Berlim', 'Lisboa', 'Berlim', 'Nova York', 'Chicago', 'Nova York']
qtdpessoas = len(cidades)
qtdcidades = len(set(cidades)) #não se contabilizam cidades repetidas
print(f"{qtdpessoas} pessoas de {qtdcidades} cidades distintas se interessaram pelo programa")
"""
