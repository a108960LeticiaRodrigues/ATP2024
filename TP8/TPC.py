# teste de aferição

# TPC1 - Especifique as seguintes listas em compreensão:

# a) Lista formada pelos elementos que não são comuns às duas listas:

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]  
ncomuns = [...]

def criarListancomuns(lista1,lista2):
    ncomuns = []
    ncomuns1 = []
    ncomuns2 = []
    for num in lista1:
        if num not in lista2:
            ncomuns1.append(num)
    for num in lista2:
        if num not in lista1 and num not in ncomuns1:
            ncomuns2.append(num)
    ncomuns = ncomuns1 + ncomuns2
    return ncomuns

criarListancomuns(lista1,lista2)

# b) Lista formada pelas palavras do texto compostas por mais de 3 letras:

texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""

def Lista3palavras(texto):
    lista =  []
    novotexto = texto.split(" ")
    for palavra in novotexto:
        if len(palavra) > 3:
            lista.append(palavra)
    return lista

print(Lista3palavras(texto))

#c) Lista formada por pares do tipo (índice, valor) com os valores da lista dada:

lista = ['anaconda', 'burro', 'cavalo', 'macaco']

def listarLista(lista):
    listaRes = []
    for elemento in lista:
        indice = lista.index(elemento) + 1
        listaRes.append((indice,elemento))
    return listaRes
    
listarLista(lista)

# TPC2

# a) Especifique uma função que dada uma string e uma substring não vazia, calcula  o número de vezes em que a substring aparece na string, sem que haja sobreposição de substrings:

def strCount(s, subs):
    contador = 0
    i = 0
    while i <= len(s) - len(subs):
        if s[i: i + len(subs)] == subs:
            contador = contador + 1
            i = i + len(subs)
        else:
            i = i + 1
    print(contador)

strCount("catcowcat", "cat") 
strCount("catcowcat", "cow") 
strCount("catcowcat", "dog")

#b) Especifique uma função que recebe uma lista de números inteiros positivos e devolve o menor produto que for possível calcular multiplicando os 3 menores inteiros da lista:

def menorlista(lista):
    menores = []
    for i in range(3):
        menor = lista[0]
        for num in lista:
            if num < menor:
                menor = num
        menores.append(menor)
        lista.remove(menor)
    return menores
    
def produtoM3(lista):
    menoreslista = menorlista(lista)
    produto = menoreslista[0] * menoreslista[1] * menoreslista[2]
    return produto 

print(produtoM3([12,3,7,10,12,8,9]))

#c) Especifique uma função que dado um número inteiro positivo, repetidamente adiciona os seus dígitos até obter apenas um dígito que é retornado como resultado:

def reduxInt(n):
    if n < 10:
        return n 
    else: 
        total = 0
        for digito in str(n):
            total = total + int(digito)
        return reduxInt(total)

print(reduxInt(777))


#d) Especifique uma função que recebe duas strings, `string1` e `string2`, e devolve o índice da primeira ocorrência de `string2` em `string1`, caso não ocorra nenhuma vez a função deverá retornar `-1`

def myIndexOf(s1, s2):
    if s2 in s1:
        return s1.index(s2)
    else:
        return -1
    

# TPC3
# Decidi completar o dicionário para facilitar a realização dos exercicios a seguir:

MyFaceBook = [
    {
        'id': 'p1', 
        'conteudo': 'A tarefa de avaliação é talvez a mais ingrata das tarefas que um professor tem de realizar...', 
        'autor': 'jcr', 
        'dataCriacao': '2023-07-20', 
        'comentarios': [
            {
                'comentario': 'Completamente de acordo...',
                'autor': 'prh'
            },
            {
                'comentario': 'Mas há quem goste...',
                'autor': 'jj'
            }
        ]
    },
    {
        'id': 'p2',
        'conteudo': 'Aprender a programar é um desafio fascinante!',
        'autor': 'uuuu',
        'dataCriacao': '2023-07-21',
        'comentarios': [
            {
                'comentario': 'Concordo! É uma jornada incrível.',
                'autor': 'abc'
            },
            {
                'comentario': 'Sim, e muito gratificante!',
                'autor': 'def'
            }
        ]
    },
    {
        'id': 'p3',
        'conteudo': 'A leitura é fundamental para o desenvolvimento pessoal e profissional.',
        'autor': 'eee',
        'dataCriacao': '2023-07-22',
        'comentarios': []
    }
]

# Estrutura:
# myfacebook => uma lista de posts 
# cada post é um dicionário em que os comentários do post são uma lista de comentários em que cada comentário é um dicionário.

# a) `quantosPost`, que indica quantos posts estão registados:

def quantosPost(redeSocial):
    return  len(MyFaceBook)

quantosPost(MyFaceBook)

# b) `postsAutor`, que devolve a lista de posts de um determinado autor:

def postsAutor(redeSocial, autor):
    posts_do_autor = []
    for post in redeSocial:
        if post["autor"] == autor:
            posts_do_autor.append(post)
    return posts_do_autor

autor_desejado = input("Que autor deseja procurar? ")
print(postsAutor(MyFaceBook, autor_desejado))

# c)  `autores`, que devolve a lista de autores de posts ordenada alfabeticamente:

def autores(redeSocial):
    lista_autores = []
    for post in redeSocial:
        autor = post["autor"]
        lista_autores.append(autor)
    return  sorted(lista_autores)

print(autores(MyFaceBook))

#d) `insPost`, que acrescenta um novo post à rede social a partir dos parâmetros recebidos e devolve a nova rede social. 

def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    max_id = 0
    for post in redeSocial:
        post_id_num = int(post['id'][1:])
        if post_id_num > max_id:
            max_id = post_id_num
    novo_id = f"p{max_id + 1}"
    
    novo_post = {
        'id': novo_id,
        'conteudo': conteudo,
        'autor': autor,
        'dataCriacao': dataCriacao,
        'comentarios': []  
    }

    redeSocial.append(novo_post)
    return redeSocial

conteudo = input("O que queres comentar?")
autor = input("Qual é o nome do autor?")
dataCriacao = input("Quando o poste foi criado? (escreva ano - mês - dia)")
comentarios = []

print(insPost(MyFaceBook, conteudo, autor, dataCriacao, comentarios))

# e) `remPost`, que remove um post da rede, correspondente ao `id` recebido.

def remPost(redeSocial, id):
    id_post = input("Qual é o id do post que deseja retirar?")
    for post in redeSocial:
        if post["id"] == id_post:
            redeSocial.remove(post)
    return redeSocial

print(remPost(MyFaceBook, id))

# f) `postsPorAutor`, que devolve uma distribuição de posts por autor (à semelhança do que foi feito nas aulas).

def postsPorAutor(redeSocial):
    distribuicao = {}
    for post in redeSocial:
        autor = post['autor']
        if autor in distribuicao:
            distribuicao[autor] = distribuicao[autor] + 1
        else:
            distribuicao[autor] = 1
    return distribuicao 

print(postsPorAutor(MyFaceBook))

# g) `comentadoPor`, que recebe um autor e devolve a lista de posts comentados por esse autor.

def comentadoPor(redeSocial, autor):
    posts_comentados = []
    for post in redeSocial:
        for comentario in post["comentarios"]:
            if comentario["autor"] == autor:
                posts_comentados.append(post)
    return posts_comentados

autor = input("Que autor deseja procurar? ")
print(comentadoPor(MyFaceBook, autor))