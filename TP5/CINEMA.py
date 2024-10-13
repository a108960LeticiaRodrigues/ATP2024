sala1 = ("Sala1", 150, [], "Twilight")
sala2 = ("Sala2", 200, [], "Hannibal")
cinema = [sala1,sala2]

def listar(cinema):
    print("---------- FILMES ------------") 
    for sala in cinema:
        print(f"{sala[0]} -> Filme: {sala[3]}  Lotação: {sala[1]}  Vendidos: {len(sala[2])}")

def vendebilhete(cinema, filme, lugar):
    for sala in cinema:
        nome, nlugares, Vendidos, nomef = sala
        if  nomef == filme and lugar <= nlugares:
            if lugar not in Vendidos:
                Vendidos.append(lugar)
                print(f"O seu bilhete fui comprado com sucesso! Corresponde ao lugar {lugar} na {nome}.")
            else:
                print(f"Esse lugar já está ocupado.")

def disponivel(cinema,filme,lugar):
    cond = True
    for sala in cinema:
        nome, nlugares, Vendidos, nomef = sala
        if  nomef == filme and lugar <= nlugares:
            if lugar in Vendidos:
                print("O lugar que escolheu não está disponivel.")
                cond = False

            elif cond == True:
                print("O lugar que escolheu está disponivel.")
                DECISÃO = input("Deseja comprar este lugar? (S/N)")
                if DECISÃO == "S":
                    vendebilhete(cinema, filme, lugar)
                else:
                    print("Compra cancelada")         
    return cond

def listardisponibilidade(cinema):
    print("--------------- LOTAÇÃO ----------------")
    for sala in cinema:
        lugares_disponiveis = sala[1] - len(sala[2])
        print(f"Filme: {sala[3]} ------> (Lugares disponiveis : {lugares_disponiveis})")

def existeSala (cinema,sala):
    cond = False
    for sala in cinema:
        if sala[0] == sala:
            cond = True
        return cond

def inserirSala(cinema, nome_sala, lugares, filme):
    if not existeSala(cinema, nome_sala):
        nova_sala = [nome_sala, lugares, [], filme] 
        cinema.append(nova_sala)
        print("Sala inserida com sucesso!")
    else:
        print("A sala já existe no cinema.")
    return listar(cinema)

def menu():
    print("------------MENU------------------")
    print("- (1) Listar filmes em exibição")
    print("- (2) Verificar disponibilidade de lugar")
    print("- (3) Vender bilhete")
    print("- (4) Listar disponibilidades nas salas")
    print("- (5) Verificar existência da sala")
    print("- (6) Inserir nova sala")
    print("- (7) Sair")
        

condição = True
print("Bem vindo ao nosso cinema!")
while condição:
    menu()
    opção = int(input(" Escolha uma opção: (Escreva o número correspondente) "))

    if opção == 1:
        listar(cinema)

    elif opção == 2:
        listar(cinema)
        FILME2 = input("Que filme deseja ver? ")
        LUGAR2 = int(input("Qual lugar deseja ver se está disponivel?"))
        disponivel(cinema,FILME2,LUGAR2)


    elif opção == 3:
        listar(cinema)
        FILME1 = input("Que filme deseja ver? ")
        LUGAR1 = int(input("Qual lugar prefere ?"))
        vendebilhete(cinema,FILME1,LUGAR1)
    

    elif opção == 4:
        listardisponibilidade(cinema)

    elif opção == 5:
        SALA = input("Qual é o nome da sala que deseja inserir no nosso cinema?")
        print(existeSala (cinema,SALA))

    elif opção == 6:
        SALA = input("Qual é o nome da sala que deseja inserir no nosso cinema? ")
        LUGARES = int(input("Quantos lugares vai ter essa sala? "))
        FILME = input("Qual vai ser o filme que vai passar nessa sala? ")

        inserirSala(cinema, SALA, LUGARES, FILME)

    elif opção == 7:
        condição = False
        print("Obrigada por visitar o nosso cinema, volte sempre!")
    
