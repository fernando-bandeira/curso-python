"""
CLASSE
-é um modelo de um objeto do mundo real representado computacionalmente
-pode conter atributos (características) e métodos (ações)
-a princípio, todo atributo/método é público, ou seja, pode ser acessado em qualquer parte do código
-atributos/métodos privados só devem ser acessados/utilizados dentro da própria classe em que foram declarados, e são iniciados por "__"
-um objeto é uma instância de uma classe
MÉTODOS
-são funções que representam os comportamentos/ações do objeto
-método construtor: método responsável pela construção do objeto, representado pela função __init__()
-métodos vinculados a objetos são chamados de métodos de instância
-esses métodos, incluindo o construtor, recebem um parâmetro chamado 'self' que faz referência ao objeto
-métodos vinculados à classe e não a objetos são chamados métodos de classe, e possuem 'cls' (classe) como parâmetro em vez de 'self'
-métodos de classe devem ser precedidos pela expressão @classmethod
-métodos não vinculados à classe e nem a objetos são chamados métodos estáticos, e devem ser precedidos pela expressão @staticmethod
ATRIBUTOS
-representam as características/estados do objeto
-atributo de instância: declarado dentro do método construtor, esse tipo de atributo normalmente possui um valor diferente para cada objeto criado
-atributo dinâmico: criado durante o tempo de execução, é um atributo de instância exclusivo do objeto especificado no momento de sua criação
-atributo de classe: declarado diretamente na classe, fora do método construtor, esse tipo de atributo normalmente já recebe um valor inicial que será o mesmo para todas as instâncias dessa classe, mas ele pode ser modificado, como o atributo 'contador' no exemplo abaixo
-OBS: durante a criação de um método, se o mesmo precisar fazer acesso a atributos de instância, esse método deverá ser um método de instância. se ele não precisar fazer acesso a atributos de instância, ele poderá ser um método de classe (pode fazer acesso a atributos de classe) ou um método estático (não faz acesso a nenhum atributo)
"""
class Produto: #classe é inicializada
    imposto = 1.05 #atributo de classe
    contador = 0 #atributo de classe

    @classmethod #método de classe
    def quantidade(cls):
        print(f"atualmente existem {cls.contador} produto(s) no sistema")

    @staticmethod #método estático
    def cupom():
        print("o código do seu cupom de desconto é FB99")

    def __init__(self, nome, estoque, valor): #método construtor
        #atributos de instância
        self.id = Produto.contador + 1
        self.nome = nome
        self.__estoque = estoque #atributo privado
        self.valor = valor * Produto.imposto
        Produto.contador += 1 #valor do atributo de classe é modificado e será diferente para objetos posteriores

    def __calcula(self, porcentagem): #método de instância privado
        return self.valor * ((100 - porcentagem) / 100)

    def desconto(self, porcentagem, codigo): #método de instância
        if codigo == "FB99":
            return self.__calcula(porcentagem)
        return "código inválido"

    def liquida(self): #método de instância
        if self.__estoque < 10:
            return self.__calcula(50)
        else:
            return self.valor

## para criar um objeto, deve-se convocar a classe como se fosse uma função, especificando valores para os parâmetros do método construtor (com exceção do parâmetro 'self')
tv = Produto("TV Samsung", 5, 2300) #criando objeto da classe Produto
## exibindo atributos (objeto.atributo)
#print(tv.id)
#print(tv.nome)
#print(tv.valor)
#print(tv.__estoque) #erro, pois o atributo é privado
## chamando método de instância (objeto.método(x) ou classe.método(objeto, x))
#print(tv.desconto(10, "FB99"))
#print(Produto.desconto(tv, 10, "FB99"))

pc = Produto("PC Dell", 10, 4000) #criando objeto da classe Produto
## exibindo atributos
#print(pc.id)
#print(pc.nome)
#print(pc.valor)
#print(pc.__estoque) #erro, pois o atributo é privado
## chamando método de instância
#print(pc.desconto(15, "FB99"))
#print(Produto.desconto(pc, 15, "FB99"))

## chamando método de classe/método estático (classe.método())
#Produto.quantidade()
#Produto.cupom()

pc.nome = "PC HP" #valor de atributo de instância pode ser atualizado
#print(pc.nome)
tv.ano = 2019 #atributo dinâmico exclusivo do objeto 'tv'
#print(tv.ano)
#print(pc.ano) #erro

## dicionário com os atributos de instância de um objeto e seus valores
#print(tv.__dict__)
#print(pc.__dict__)

## deleção de atributos
del tv.ano
#print(tv.__dict__)

## OBS: não é necessário criar um objeto para se obter um atributo de classe
#print(Produto.imposto)
## OBS: é possível acessar atributos/métodos privados, embora isso não deva ser feito
tv._Produto__estoque = 2
#print(tv._Produto__estoque)
#print(pc._Produto__calcula(20))
