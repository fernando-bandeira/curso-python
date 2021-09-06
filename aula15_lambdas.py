"""
EXPRESSÕES LAMBDA
-são funções anônimas (sem nome)
-funcionam de forma similar às funções regulares
-sintaxe:
lambda parâmetros: retorno
"""

calc = lambda x: 3 * x + 1
#print(calc(4))

nome_comp = lambda nome, sobrenome: (nome.strip() + " " + sobrenome.strip()).title()
#print(nome_comp("joão pedro ", " ribeiro"))

bomdia = lambda: "bom dia!" #expressão lambda sem parâmetros
#print(bomdia())

autores = ["Paulo Coelho", "C. S. Lewis", "Lewis Carroll", "Arthur Conan Doyle", "George Orwell", "H. G. Wells", "J. K. Rowling", "Jane Austen", "Edgar Allan Poe", "William Shakespeare"]
## ordenação pelo sobrenome
#print(autores)
autores.sort(key = lambda nome: nome.split()[-1])
#print(autores)
## OBS: reveja o uso do método sort() e seu parâmetro opcional 'key' na aula 10, sobre listas
