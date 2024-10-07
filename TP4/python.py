def menu():

    print("---------------MENU-----------------")
    print("(1) Criar Lista ")
    print("(2) Ler Lista ")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) estaOrdenada por ordem crescente ")
    print("(8) estaOrdenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")

from random import randint

cond = True
lista = []

while cond:
    menu()
    Opção = int(input("Qual opção deseja escolher? (Introduza o número correspondente)"))
    

    if Opção == 1:
        def criarLista(N):
            lista.clear()
            for num in range(N):
                num = randint(1,100)
                lista.append(num)
            return lista
        N = int(input("Quantos números a sua lista vai ter?"))
        lista = criarLista(N)
        print(f"Lista atual: {lista}")
        

    elif Opção == 2:
        def lerLista(N):
            lista.clear()
            for num in range(N):
                n = int(input(f"Introduza o número {num + 1} de {N}"))
                lista.append(n)
            return lista 

        N = int(input("Quantos números a lista vai ter? "))
        lista = lerLista(N)
        print(f"Lista atual: {lista}")

    elif Opção == 3:
        if lista != []:
            def somalista(list):
                soma = 0
                for num in list:
                    soma = soma + num
                return soma

            SOMA = somalista(lista)
            print(f"A soma dos elementos dá {SOMA}")
        else:
            print("A lista está vazia, use primeiro a opção 1 ou 2.")

    elif Opção == 4:
        if lista != []:
            def medialista(list):
                soma = 0
                for num in list:
                    soma = soma + num
                return soma / len(list)
        
            MEDIA = medialista(lista)
            print(f"A média dos elementos é {MEDIA}")
        else:
            print("A lista está vazia, use primeiro a opção 1 ou 2.")

    elif Opção == 5:
        if lista != []:
            def maiorlista(list):
                maior = list[0]
                for num in list[1:]:
                    if num > maior:
                        maior = num
                return maior
        
            MAIOR = maiorlista(lista)
            print(F"O maior dos elementos da lista é {MAIOR}")
        else: 
            print("A lista está vazia, use primeiro a opção 1 ou 2.")

    elif Opção == 6:
        if lista != []:
            def menorlista(list):
                menor = list[0]
                for num in list[1:]:
                    if menor > num:
                        menor = num
                return menor

            MENOR = menorlista(lista)
            print(f"O menor elemento da lista é {MENOR}")
        else:
            print("A lista está vazia, use primeiro a opção 1 ou 2.")

    elif Opção == 7:
        if lista != []:
            def estaOrdenadacrescente(list):
                i = 0
                condição = True
                while i < len(list) - 1 and condição != False:
                    if list[i] < list[i + 1]:
                        i = i + 1
                    else:
                        condição = False

                if condição == True:
                    print("Sim")
                else:
                    print("Não")

            estaOrdenadacrescente(lista)
        else:
            print("A lista está vazia, use primeiro a opção 1 ou 2.")

    elif Opção == 8:
        if lista != []:
            def estaOrdenadadecrescente(list):
                i = 0
                condi = True
                while i < len(list) - 1 and condi != False:
                    if list[i] > list[i + 1]:
                        i = i + 1
                    else:
                        condi = False

                if condi == True:
                    print("Sim")
                else:
                    print("Não")

            estaOrdenadadecrescente(lista)
        else:
            print("A lista está vazia, use primeiro a opção 1 ou 2.")

    elif Opção == 9:
        if lista != []:
            def encontrarelem(list,elem):
                i = 0
                while i < len(list):
                    if list[i] == elem:
                        print(f"O elemento {elem} fui encontrado na posição {i}")
                        i = i + 1
                    else:
                        i = i + 1
                if elem not in list:
                    print("-1")

            elem = int(input("Qual número deseja procurar"))
            encontrarelem(lista,elem)
        else:
            print("A lista está vazia, use primeiro a opção 1 ou 2.")
            

    elif Opção == 0:
        cond = False 
        print(f"Lista guardada no momento: {lista}")
        print("Obrigada,Volte sempre!")
        lista.clear()
