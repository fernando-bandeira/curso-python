"""
MANIPULAÇÃO DE ARQUIVOS
-ao se trabalhar com arquivos utilizando a linguagem Python, deve-se:
1. abrir o arquivo
2. manipular o arquivo da forma que for desejada
3. fechar o arquivo
-cursor: indicador que aponta a partir de que posição do arquivo será realizada a leitura/escrita do mesmo

MODOS DE ABERTURA
-é possível abrir um arquivo de diferentes modos, dependendo do propósito
I. modo "r" (padrão): leitura. caso o arquivo não exista, ocorre erro
II. modo "w": escrita. caso o arquivo exista, seu conteúdo antigo é integralmente excluído de forma imediata, e caso não exista, ele é criado
III. modo "a": escrita. caso o arquivo exista, a escrita será realizada a partir do final de seu conteúdo, e caso não exista, ele é criado
IV. modo "x": cria o arquivo para escrita. caso o arquivo já exista, ocorre erro
V. modo "r+": leitura e escrita. caso o arquivo não exista, ocorre erro. o cursor se localiza, a princípio, no início do arquivo, mas pode ser movido. caso existam caracteres após o cursor, serão sobrescritos tantos desses caracteres quantos forem os caracteres do conteúdo a ser escrito
VI. modo "w+": similar ao modo "w" para escrita, permite leitura
VII. modo "a+": similar ao modo "a" para escrita, permite leitura

1) LEITURA DE ARQUIVOS
"""
## abrindo arquivo no modo "r" (como é o modo padrão, não precisa ser especificado)
arq = open("arquivo1.txt", encoding = "utf-8")
## abrir arquivos definindo "utf-8" como valor do parâmetro opcional 'encoding' garante que não ocorrerão problemas com acentuação e caracteres especiais presentes no arquivo

## método read() faz a leitura do arquivo, ou seja, transforma o conteúdo do arquivo em uma string
leitura = arq.read()
#print(leitura)

## após a leitura do arquivo, o cursor estará no final do arquivo, ou seja, se outra leitura for feita, nada será lido, pois não existe nada após o cursor
nova_leitura = arq.read()
#print(nova_leitura)
## é possível utilizar o método seek() para colocar o cursor em uma posição de interesse
arq.seek(28) #string 'verso' abaixo será lida a partir do caracter de índice 28
verso = arq.read(18) #é possível definir quantos caracteres serão lidos (nesse caso, 18)
#print(verso)

## o método readline() lê uma linha por vez e posiciona o cursor ao final da linha que foi lida
arq.seek(0) #cursor é posicionado no início do arquivo
#print(arq.readline(), end = "")
for i in range(3):
    #print(arq.readline(), end = "")
    pass

## o método readlines() (não confundir com readline()) cria uma lista com cada linha do arquivo como elemento
lista = arq.readlines()
#print(lista)
#print(len(lista)) #quantidade de linhas

## fechando o arquivo
arq.close()

"""
ESCRITA DE ARQUIVOS
"""
## abrindo arquivo no modo "w" (escrita)
arq = open("arquivo2.txt", "w", encoding = "utf-8")
## para realizar a escrita, utiliza-se o método write()
frase = "Até um relógio parado tem razão duas vezes ao dia"
#frase = input("digite uma frase para ser escrita: ")
arq.write(frase)
arq.close()

"""
BLOCO 'with'
-é uma estrutura que permite a manipulação de um arquivo dentro de um bloco
-após o final do bloco, o arquivo é fechado automaticamente
"""
with open("arquivo1.txt", encoding = "utf-8") as arq:
    versos = arq.readlines()
    #print("essa estrofe possui {} versos".format(len(versos)))
    #print("o primeiro verso é \"{}\"".format(versos[0].replace('\n', '')))
    #print("o último verso é \"{}\"".format(versos[-1].replace('\n', '')))
