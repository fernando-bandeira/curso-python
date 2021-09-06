"""
FUNÇÕES
-uma função é um trecho de código definido que realiza uma tarefa específica, capaz de ser convocado posteriormente para que essa tarefa seja feita sem necessidade de escrever novamente os códigos responsáveis pela sua execução
-já utilizamos inúmeras funções: print(), len(), abs(), type(), max()
-o nome de funções deve obedecer às mesmas regras que o nome de variáveis:
1) deve conter apenas letras, números e "_" (sem acentuação, espaços, hífens ou outros caracteres especiais)
2) não deve começar por um número
-veja a seguir como definir suas próprias funções:
def nome_funcao():
    #comandos
"""

## função é definida
def poema():
    print("Minha terra tem palmeiras,")
    print("Onde canta o Sabiá;")
    print("As aves, que aqui gorjeiam,")
    print("Não gorjeiam como lá.")
## a função agora pode ser convocada (chamada) quantas vezes quisermos
#poema()

"""
funções com parâmetros de entrada
-parâmetros são dados recebidos pela função para serem processados pela mesma
-parâmetros são colocados dentro dos parênteses
-parâmetros opcionais devem ser declarados sempre APÓS os obrigatórios
-o valor passado chama-se argumento
def oi(nome): #'nome' é parâmetro
    print(f"oi, {nome}")
oi("fernando") #"fernando" é argumento
"""
## definindo função com um parâmetro
def quadrado(x): #o valor de 'x' será especificado na chamada da função
    resultado = x * x
    print(resultado)
## chamando a função
#quadrado(6) #o parâmetro 'x' da função quadrado() nesse caso valerá 6
#quadrado(17) #o parâmetro 'x' da função quadrado() nesse caso valerá 17

## definindo função com múltiplos parâmetros
def potencia(x, y):
    resultado = x ** y
    print(resultado)
## chamando a função
#potencia(5, 4) #os parâmetros 'x' e 'y' da função potencia(), nesse caso, valem 5 e 4, nessa ordem
## é possível chamar a função realizando atribuição dos parâmetros, o que permite ordens diferentes
#potencia(y = 5, x = 3)

## definindo função com parâmetros opcionais
def somatorio(x, y = 0, z = 0): #parâmetros 'y' e 'z' são opcionais e seus valores padrões são '0'
    resultado = x + y + z
    print(resultado)
## chamando a função
#somatorio(1, 2, 3)
#somatorio(5)

## parâmetro '*args' transforma argumentos extras em elementos de uma tupla
## útil para funções em que não se sabe a quantidade de argumentos que serão passados
def somatorio(*args):
    resultado = sum(args)
    print(resultado)
#somatorio(1, 2, 3)
#somatorio(5)
#somatorio(1, 2, 3, 4)
## utilizando o parâmetro '*args', é possível passar uma coleção como argumento de uma função e efetuar seu desempacotamento da seguinte forma:
lista = [1, 3, 5, 7]
#somatorio(*lista) #caractere '*' indica que se deseja realizar o desempacotamento

## parâmetro '**kwargs' transforma argumentos em valores de um dicionário, exigindo que se utilize atribuição de parâmetros, que serão as chaves do dicionário
def exibe_dic(**kwargs):
    print(kwargs)
#exibe_dic(nome = "bernardo", sexo = "masculino", idade = 30)
## utilizando o parâmetro '**kwargs', é possível passar um dicionário já existente como argumento de uma função:
dados = {"marca": "Honda", "ano": 2018, "modelo": "HRV"}
#exibe_dic(**dados) #caracteres '**' indicam que o argumento é um dicionário

"""
funções com retorno
"""
## repare que a função cubo1() abaixo gera e exibe o cubo de um número, porém após sua execução esse dado é perdido e não é possível utilizá-lo
def cubo(x):
    result = x ** 3
    print(result)
#cubo(4)

## para solucionar esse problema, podemos utilizar a palavra reservada 'return' para retornar um dado que pode ser recuperado simplesmente convocando a função
def cubo(x):
    result = x ** 3
    return result

cubo(3) #note que apenas chamar a função não exibe nada na tela
#print(cubo(3)) #para exibir, utilizamos a função print()
#print(cubo(7) + 10)
## o uso de 'return' interrompe de imediato a execução da função

"""
variáveis locais e globais
"""
## uma variável só é reconhecida dentro do bloco de função em que ela foi declarada, a menos que ela seja uma variável global, explicada abaixo
x = 1 #'x' é uma variável global, pois é declarada fora de qualquer bloco de função, e, portanto, é reconhecida em qualquer trecho do código
def zero():
    y = 0 #por ser declarada dentro de uma função, a variável 'y' só é reconhecida dentro dessa função, ou seja, é uma variável local
    return y
#print(y) #variável 'y' não é reconhecida, retornando erro, mesmo que a função zero() tivesse sido chamada anteriormente

## variáveis globais não podem ser modificadas dentro de funções de forma convencional
nome = 'fernando' #variável global
def altera_nome():
    nome = 'roberta' #isso não altera a variável global!
altera_nome() #função altera_nome() é chamada
#print(nome) #apesar de a função altera_nome() ter sido chamada, a variável 'nome' ainda possui valor 'fernando'

## dentro de uma função, caso possuam mesmo nome, a variável local tem preferência sobre a variável global
def altera_nome():
    nome = 'roberta' #variável local
    print(nome) #apesar de a variável global permanecer inalterada, a variável exibida será a local, pois possui prioridade sobre a global
#altera_nome()

## para modificar uma variável global dentro de uma função, é necessário escrevê-la após a palavra reservada 'global'
def altera_nome():
    global nome
    nome = 'roberta' #variável global é alterada
altera_nome() #função altera_nome() é chamada
#print(nome) #agora a variável global 'nome' tem valor 'roberta'
## dessa forma, além de poder modificar variáveis globais já existentes, é possível criar novas variáveis globais, que poderão ser reconhecidas em todo o código
def define_idade():
    global idade
    idade = 20
define_idade()
#print(idade)

## apesar de não ser possível alterar variáveis globais dentro de funções de forma convencional, é possível trabalhar com elas de outras formas normalmente
saldo = 2
def analisa_saldo():
    if saldo > 0 :
        print(f"houve lucro de {saldo}")
    elif saldo < 0:
        print(f"houve prejuízo de {saldo}")
    else:
        print("não houve lucro nem prejuízo")
#analisa_saldo()

## OBS: cuidado com esse erro comum:
contador = 1
def incrementa():
    contador += 1 #esse operador modifica a variável, portanto 'contador' é considerado uma variável local, e como ela não foi declarada, retorna um erro
    return contador
#print(incrementa())

"""
EXEMPLOS
"""
## recomenda-se documentar as funções criadas com docstrings, isto é, informar na primeira linha da função, entre triplas aspas duplas, que tarefa a função executa
def soma_algs(x):
    """essa função soma os algarismos de um número e faz o mesmo com o resultado até que reste um único algarismo, que é retornado"""
    x = str(x)
    while len(x) > 1:
        soma = 0
        for i in range(len(x)):
            soma += int(x[i])
        x = str(soma)
    return x
#print(soma_algs(2356))

def fibonacci(x):
    """essa função retorna o número informado de termos da sequência de fibonacci"""
    lista = []
    if x == 0:
        return lista
    lista.append(1)
    if x == 1:
        return lista
    lista.append(1)
    for i in range(2, x):
        lista.append(lista[i - 1] + lista[i - 2])
    return lista
#print(fibonacci(8))

def fatorial(x):
    """essa função retorna o fatorial do número informado"""
    fatorial = 1
    for i in range(1, x + 1):
        fatorial *= i
    return fatorial
#print(fatorial(8))

"""
recursividade
-convocar uma função dentro da própria função
"""
def fatorial(x):
    """essa função retorna o fatorial do número informado"""
    if x == 0:
        return 1
    return x * fatorial(x - 1) #esse processo é repetido até que o parâmetro da função tenha valor 0
#print(fatorial(5))
