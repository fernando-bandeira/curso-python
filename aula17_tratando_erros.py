"""
TIPOS DE ERRO MAIS COMUNS
1. SyntaxError: erro de sintaxe, ou seja, ocorre quando é escrito algo que a linguagem não reconhece como parte de si
"""
#print "fernando"

"""
2. NameError: ocorre quando se tenta utilizar uma variável/função não definida
"""
#print(x + y)
#contagem()

"""
3. TypeError: ocorre quando uma ação (função/operação) é aplicada a um tipo indevido
"""
#print(len(100))
#print(abs("fernando"))
#print("a" / "b")

"""
4. ValueError: ocorre quando uma ação (função/operação) é aplicada a um dado que tem tipo válido, mas valor indevido
"""
#print(int("fernando"))

"""
5. IndexError: ocorre quando se tenta acessar um elemento de um iterável por um índice inválido
"""
#print("caos"[10])
#print([1, 2, 3][5])

"""
6. KeyError: ocorre quando tentamos acessar um elemento de um dicionário a partir de uma chave inexistente
"""
dic = {"a": 1, "b": 2, "c": 3}
#print(dic["d"])

"""
7. AttributeError: ocorre quando se tenta utilizar um método/atributo inválido em um tipo específico
"""
tupla = 1, 3, 2, 0
#tupla.sort()
#print([].upper())

"""
8. IndentationError: ocorre quando a indentação não é feita ou é feita de forma incorreta
"""
#while True:
#print("fernando")

"""
TRATAMENTO DE ERROS
-sintaxe
try:
    #código que o programa tentará executar
except:
    #código que o programa executará caso o código do bloco 'try' gere erro
else: #opcional
    #código que será executado caso não tenha ocorrido erro
"""
try:
    ## função não existe, portanto geraria erro do tipo NameError
    fernando(99)
except:
    #print("erro")
    pass
else:
    print("a função foi executada com sucesso")

## é possível tratar erros de tipos específicos
#entrada = "5"
try:
    n = int(entrada)
    #print(n * n)
except ValueError: #erro caso o valor da entrada do usuário seja inválido
    #print("você não digitou um número")
    pass
except NameError as err: #é possível exibir os detalhes do erro dessa forma
    #print(f"ocorreu o seguinte erro: {err}")
    pass
except:
    #print("erro de outro tipo")
    pass

"""
EXEMPLO
"""
def dividir(a, b):
    """essa função retorna a divisão entre dois números"""
    try:
        return int(a) / int(b)
    except ValueError:
        return "valor(es) inválido(s)"
    except ZeroDivisionError:
        ## erro gerado após uma tentativa de divisão por zero
        return "impossível dividir por zero"

#print(dividir(input("digite um número: "), input("digite outro número: ")))
#print(dividir(6, 2))
#print(dividir(6, "2"))
#print(dividir("a", "&"))
#print(dividir(5, 0))
