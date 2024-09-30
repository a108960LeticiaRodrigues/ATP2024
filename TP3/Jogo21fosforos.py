
def menu():

    print("---------------MENU-----------------")
    print("Bem vindo ao jogo dos 21 fósforos! ")
    print("No início do jogo, há 21 fósforos.")
    print("Cada jogador (computador ou utilizador), pode tirar 1, 2, 3 ou 4 fósforos quando for a sua vez de jogar")
    print("Os jogadores jogam alternadamente e quem tirar o último fósforo perde!")
    print("O jogo tem dois modos:")
    print("Modo 1: O jogador joga em primeiro lugar ")
    print("Modo 2: o computador começa primeiro ")
    print("Se deseja sair, responda com 3.")


from  random import randint

cond = True
while cond:
    menu()
    Modo = int(input("Qual modo pretende jogar? (responda com 1, 2 ou 3)"))
    
    while Modo != 3:
        if Modo == 1:
            caixa = ["fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo",]
            quantidade = len(caixa)

            while quantidade > 0:
                N_utilizador = int(input("É a sua vez! Quantos fósforos deseja retirar? (responda com 1,2,3 ou 4)"))
                i = 0
                while i < N_utilizador:
                    caixa.remove("fósforo")
                    i = i + 1
                    quantidade = len(caixa)
                print(f"Fósforos restantes: {quantidade} ")

                VEZ = input("É a vez do computador! (clique enter)")
                if quantidade <= 4:
                    N_computador = quantidade
                    i = 0
                    while i < N_computador:
                        caixa.remove("fósforo")
                        i = i + 1
                    quantidade = len(caixa)
                else:
                    N_computador = randint(1,4)
                    i = 0
                    while i < N_computador:
                        caixa.remove("fósforo")
                        i = i + 1
                    quantidade = len(caixa)
                print(f"Fósforos restantes: {quantidade} ")
        
            if quantidade == 0:
                print("O jogador venceu! O computador tirou  o ultimo fósforo!")
                Modo = int(input("Deseja voltar a jogar, jogar o modo 2 ou sair? (responda com 1,2 ou 3)"))

        if Modo == 2:
            caixa = ["fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo","fósforo",]
            quantidade = len(caixa)

            while quantidade > 0:
                VEZ = input("É a vez do computador! (clique enter)")
                if quantidade <= 5 and quantidade != 1:
                    caixa = ["fósforo"]
                    quantidade = len(caixa)
                    print(f"Fósforos restantes: {quantidade} ")
                elif quantidade > 5:
                    N_computador = randint(1,4) 
                    i = 0
                    while i < N_computador:
                        caixa.remove("fósforo")
                        i = i + 1
                        quantidade = len(caixa)
                    print(f"Fósforos restantes: {quantidade} ")
                
                elif quantidade == 1:
                    N_computador = 1
                    caixa.remove("fósforo")
                    quantidade = len(caixa)
                    print(f"Fósforos restantes: {quantidade} ")
                    print("O jogador venceu! O computador tirou  o ultimo fósforo!")
                    Modo = int(input("Deseja voltar a jogar, jogar o modo 2 ou sair? (responda com 1,2 ou 3)"))
                    quantidade = -1

                if quantidade != -1:   
                    N_utilizador = int(input("É a sua vez! Quantos fósforos deseja retirar? (responda com 1,2,3 ou 4)..."))
                    i = 0
                    while i < N_utilizador:
                        caixa.remove("fósforo")
                        i = i + 1
                        quantidade = len(caixa)
                    print(f"Fósforos restantes: {quantidade} ")
                else:
                    pass

            if quantidade == 0:
                print("O computador venceu! O jogador tirou  o ultimo fósforo!")
                Modo = int(input("Deseja voltar a jogar, jogar o modo 2 ou sair? (responda com 1,2 ou 3)"))
            

    if Modo == 3:
        cond = False
        print("Obrigada, volte sempre!")
