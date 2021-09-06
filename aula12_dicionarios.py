"""
DICIONÁRIOS
-dicionários são coleções de dados em que cada elemento possui uma chave e um valor, que podem ser de vários tipos. os elementos também são separados por vírgula, e o dicionário é delimitado por chaves {}
-a sintaxe de um dicionário é {chave1: valor, chave2: valor, chave3: valor}
-NÃO É POSSÍVEL existirem duas chaves iguais em um dicionário
"""
paises = {"br": "Brasil", "eua": "Estados Unidos", "arg": "Argentina"}
#print(type(paises))
## outra forma (menos comum)
paises = dict(br = "Brasil", eua = "Estados Unidos", arg = "Argentina")
#print(type(paises))

## é possível acessar os elementos de um dicionário através das chaves, utilizando COLCHETES
## se a chave não existir no dicionário, ocorrerá erro
lugar = paises["arg"]
#print(lugar)
## a forma mais recomendada é utilizar o método get()
## se a chave não existir, não ocorrerá erro, mas o método retornará None (tipo nulo)
lugar = paises.get("br")
#print(lugar)
lugar = paises.get("ing", "país não encontrado") #valor caso chave não exista
#print(lugar)

## é possível verificar se uma chave existe em um dicionário
if "br" in paises:
    #print("existe")
    pass
if "Brasil" in paises: #não é possível buscar valores dessa forma, apenas chaves
    print("existe")
else:
    #print("não existe")
    pass

## é possível adicionar ou atualizar elementos de um dicionário simplesmente atribuindo um valor a uma nova chave
receita = {"jan": 300, "fev": 250, "mar": 450}
receita["abr"] = 500 #adicionando
#print(receita)
receita["jan"] = 200 #atualizando
#print(receita)

## o método update() insere elementos de um dicionário em outro. se uma das chaves daquele não existir nesse, o elemento é adicionado. caso contrário, o elemento que possui essa chave tem seu valor atualizado
novo = {"mai": 350} #dicionário com um elemento
receita.update(novo) #acrescentando esse elemento no dicionário 'receita' (chave "mai" não existe no mesmo)
#print(receita)
receita.update({"fev": 200}) #atualizando um elemento do dicionário 'receita' (chave "fev" já existe no mesmo)
#print(receita)
novos = {"jun": 550, "jul": 500}
receita.update(novos) #acrescentando múltiplos elementos
#print(receita)
## ao adicionar um elemento, certifique-se de que a chave a ser utilizada não existe, caso contrário o valor dessa chave será atualizado, e nenhum elemento será adicionado, já que não podem existir chaves iguais em um dicionário

## é possível remover elementos de um dicionário utilizando o método pop() e especificando a chave
receita = {"jan": 300, "fev": 250, "mar": 450, "abr": 500}
receita.pop("abr")
#print(receita)
## outra forma
del receita["mar"]
#print(receita)
## é possível ainda limpar um dicionário utilizando o método clear()
receita.clear()
#print(receita)

## assim como nas listas, nos dicionários existem as cópias rasa e profunda
d = dict(a = 1, b = 2, c = 3)
copia = d #cópia rasa
copia.pop("c") #qualquer alteração na cópia altera o original
#print(d)
#print(copia)

d = dict(a = 1, b = 2, c = 3)
copia = d.copy() #cópia profunda
copia.pop("c") #alteração na cópia não altera o original
#print(d)
#print(copia)

"""
iterando sobre um dicionário utilizando o loop 'for'
"""
paises = {"br": "Brasil", "eua": "Estados Unidos", "arg": "Argentina"}
for chave in paises:
    #print(chave) #exibindo a chave
    #print(paises[chave]) #exibindo o valor
    pass
## os métodos keys() e values() retornam objetos iteráveis contendo as chaves e os valores, respectivamente
for chave in paises.keys(): #forma mais recomendada de iterar sobre as chaves de um dicionário
    #print(chave)
    pass
for valor in paises.values():
    #print(valor)
    pass

## é possível, a partir dos objetos gerados pelos métodos keys() e values(), obter o somatório, máximo e mínimo das chaves ou dos valores
dicionario = {"a": 100, "b": 400, "c": 900}
#print(sum(dicionario.values()))
#print(max(dicionario.values()))
#print(min(dicionario.keys()))
#print(len(dicionario)) #tamanho do dicionário
## OBS: reveja as observações sobre as funções sum(), max() e min() na aula 10, sobre listas

## é possível criar uma lista com apenas as chaves ou apenas os valores de um dicionário convertendo os objetos em listas através da função list()
#print(list(paises.keys()))
#print(list(paises.values()))

"""
desempacotamento de dicionários
"""
#print(paises.items()) #gera um objeto iterável contendo tuplas, em que cada tupla possui como elementos uma chave e seu respectivo valor
## iterando sobre o objeto realizando desempacotamento das tuplas
for chave, valor in paises.items():
    #print(f"chave: {chave} | valor: {valor}")
    pass

"""
'compreensão de dicionário' (dictionary comprehension)
-permite criar um dicionário a partir de uma iteração dinâmica
"""
numeros = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5} #dicionário
triplos = {chave: valor * 3 for chave, valor in numeros.items()}
#print(triplos)

impares = [1, 3, 5, 7, 9] #lista
dobros = {numero: numero * 2 for numero in impares}
#print(dobros)

letras = "abcde" #string
numeros = (1, 2, 3, 4, 5) #tupla
dic = {letras[i]: numeros[i] for i in range(len(letras))}
#print(dic)

numeros = {4, 7, 3, 2, 9, 0, 1, 5, 6, 8} #conjunto (aula 13)
classif = {n: ("par" if n % 2 == 0 else "impar") for n in numeros}
#print(classif)

"""
#exemplo
#sistema de carrinho de compras virtual

## códigos dos produtos: ps4, pc, tv, cel
ps4 = {"nome": "PS4", "qtd": 1, "preco": 3000, "cod": "ps4"}
laptop = {"nome": "Laptop", "qtd": 1, "preco": 4000, "cod": "pc"}
tv = {"nome": "TV", "qtd": 1, "preco": 1500, "cod": "tv"}
celular = {"nome": "Smartphone", "qtd": 1, "preco": 3500, "cod": "cel"}
produtos = [ps4, laptop, tv, celular]

carrinho = []
comando = ""
while comando != "f":
    comando = input("digite o código de um produto ou digite 'f' para finalizar\n").strip().lower()
    if comando == "f":
        break
    else:
        for i in range(len(produtos)):
            produto = produtos[i]
            if comando == produto["cod"]:
                print("produto adicionado")
                if produto in carrinho:
                    carrinho[carrinho.index(produto)]["qtd"] += 1
                else:
                    carrinho.append(produto)
                break
            elif i == len(produtos) - 1:
                print("produto não encontrado")
total = 0
for d in carrinho:
    preco_total = d["qtd"] * d["preco"]
    print(f"-{d['nome']} ({d['qtd']} unidade(s))")
    print(f"Preço Unit.: R${d['preco']} / Preço total: R${preco_total}")
    total += preco_total
print(f"Total: R${total}")
"""
