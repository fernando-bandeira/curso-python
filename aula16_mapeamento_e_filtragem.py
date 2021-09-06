"""
MAPEAMENTO, ZIPAGEM E FILTRAGEM DE DADOS
1. MAPEAMENTO DE DADOS (função map())
-essa função recebe como parâmetros uma outra função e um iterável
-sintaxe:
map(função, iterável)
-a função passada como parâmetro atua sobre cada item do iterável e adiciona seus retornos a um objeto também iterável, que será retornado pela função map() e pode ser convertido em uma coleção de interesse
"""
def area_circ(r):
    """função que calcula a área aproximada de um círculo a partir de seu raio"""
    return 3.14 * r ** 2

raios = [2, 3, 5, 7, 11] #lista de raios de círculos cujas áreas serão calculadas
areas = [] #lista de áreas correspondentes

areas = map(area_circ, raios)

## é possível passar expressões lambda como primeiro parâmetro da função map()
calc_area = lambda r: 3.14 * r ** 2
areas = map(calc_area, raios)
#print(tuple(areas))

"""
2. ZIPAGEM DE DADOS (função zip())
-essa função recebe como parâmetros dois ou mais iteráveis
-sintaxe:
zip(iterável, iterável)
-essa função une itens de uma mesma posição desses iteráveis em tuplas, e retorna um objeto iterável contendo essas tuplas, que também pode ser convertido em uma coleção de interesse
"""
areas = map(calc_area, raios)
raios_areas = zip(raios, areas) #isso gera um objeto com tuplas que seguem o padrão (raio 'y', área do círculo de raio 'y')
#print(list(raios_areas))

## se os iteráveis não tiverem a mesma quantidade de itens, será considerada apenas a quantidade de itens do menor iterável
idades = (2, 12, 20, 18, 23, 15) #6 itens
sexos = ("feminino", "masculino", "masculino", "feminino") #4 itens
nomes = ["amanda", "marcelo", "fernando", "maria", "joão"] #5 itens
#print(list(zip(idades, sexos, nomes)))

"""
3. FILTRAGEM DE DADOS (função filter())
-assim como a função map(), a função filter() recebe como parâmetros uma função e um iterável
-sintaxe:
filter(função, iterável)
-a função passada como parâmetro recebe cada item do iterável como parâmetro, e caso ela retorne 'True', esse item é adicionado a um objeto iterável, que será retornado pela função filter() e também pode ser convertido em uma coleção de interesse
"""
idades = 11, 20, 15, 38, 9, 22, 13, 4, 12, 17, 18, 35
media = sum(idades) / len(idades)

def acima_media(x):
    """essa função retorna True, caso um dado seja maior do que a média, ou False, caso o dado seja menor do que a média"""
    return x > media

maiores_media = filter(acima_media, idades)
#print(set(maiores_media))

## é possível passar expressões lambda como primeiro parâmetro da função filter()
checa_media = lambda x: x > media
maiores_media = filter(checa_media, idades)
#print(list(maiores_media))

## se colocarmos 'None' (tipo nulo) como parâmetro de filter() no lugar de uma função, podemos remover dados vazios
nomes = ["", "julio", "fernando", "", "roberto", "", []]
nomes = list(filter(None, nomes))
#print(nomes)

"""
OBSERVAÇÕES
a. após a primeira utilização das funções map(), zip() e filter(), os objetos retornados por elas são esvaziados, não sendo mais possível utilizá-los
"""
## map()
numeros = (0, 1, 2, 3, 4, 5)
dobros = map(lambda x: x * 2, numeros)
## print(list(dobros)) #primeira utilização
## print(tuple(dobros)) #coleção vazia

## zip()
dobros = map(lambda x: x * 2, numeros)
numeros_dobros = zip(numeros, dobros)
## print(set(numeros_dobros)) #primeira utilização
## print(list(numeros_dobros)) #coleção vazia

## filter()
pares = filter(lambda x: x % 2 == 0, numeros)
## print(tuple(pares)) #primeira utilização
## print(set(pares)) #coleção vazia

"""
b. entretanto, se a conversão for realizada no momento em que a função é chamada, os dados não são perdidos
"""
## map()
numeros = (0, 1, 2, 3, 4, 5)
dobros = list(map(lambda x: x * 2, numeros))
#print(set(dobros))
#print(tuple(dobros))

## zip()
dobros = map(lambda x: x * 2, numeros)
numeros_dobros = tuple(zip(numeros, dobros))
#print(list(numeros_dobros))
#print(set(numeros_dobros))

## filter()
pares = set(filter(lambda x: x % 2 == 0, numeros))
#print(tuple(pares))
#print(list(pares))

"""
OUTRAS FORMAS DE REALIZAR MAPEAMENTO, ZIPAGEM E FILTRAGEM
I. laço de repetição 'for'
"""
## mapeamento
areas = []
for r in raios:
    areas.append(area_circ(r))
#print(areas)

## zipagem
raios_areas = []
for n in range(len(raios)):
    raios_areas.append((raios[n], areas[n]))
#print(raios_areas)
## OBS: o iterável passado como parâmetro da função len() precisa ser o menor iterável que participará do processo

## filtragem
maiores_media = []
for idade in idades:
    if idade > media:
        maiores_media.append(idade)
#print(maiores_media)

"""
II. compreensão de coleções (comprehensions)
"""
## mapeamento
areas = [area_circ(r) for r in raios]
#print(areas)

## zipagem
raios_areas = [(raios[i], areas[i]) for i in range(len(raios))]
#print(raios_areas)
## OBS: o iterável passado como parâmetro da função len() precisa ser o menor iterável que participará do processo

## filtragem
maiores_media = [idade for idade in idades if idade > media]
#print(maiores_media)
