

tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

def medias(tabMeteo):
    res = []
    for dia in tabMeteo:
        data, min, max, perc = dia
        media = (max + min)/2
        res.append(media)
    return res


def guardaTabMeteo(t, fnome):
    file = open(fnome,"w")
    for data, min, max, perc in t:
         ano, mes, dia = data
         registo = f"{ano}-{mes}-{dia}&{max}&{min}&{perc}\n"
         file.write(registo)
    file.close()


def carregaTabMeteo(fnome):
    res = []
    file = open(fnome,"r")

    for linha in file:
        linha = linha.strip() 
        campos = linha.split("&")
        data, min, max, prec = campos
        ano,mes, dia = data.split("-")
        dia = (int(ano),int(mes), int(dia), float(min), float(max), float(prec))
        res.append(dia)
    file.close()
    return res


def minMin(tabMeteo):
    minimo = tabMeteo[0][1]
    for data,min,*_ in tabMeteo[1:]:
        if min < minimo:
            minimo = min
        return minimo


def amplTerm(tabMeteo):
    res = []
    for data,min,max,prec in tabMeteo:
        amplTerm = max - min
        res.append((data,amplTerm))
    return res 


def maxChuva(tabMeteo):
    max_prec = tabMeteo[0][3]
    for dia in tabMeteo[1:]:
        data,min,max,prec = dia
        if prec > max_prec:
            max_prec = prec
            max_data = data
    return (max_data, max_prec)


def diasChuvosos(tabMeteo, p):
    res = []
    for dia in tabMeteo:
        if dia[3] > p:
            res.append((dia[0],dia[3]))
    return res


def maxPeriodoCalor(tabMeteo, p):
    consec_local = 0
    consec_max = 0

    for data,min,max,prec in tabMeteo:
        if prec < p:
            consec_local += 1
           
        else:
            if consec_local > consec_max:
                consec_max = consec_local
            consec_local = 0

    if consec_local > consec_max:
        consec_max = consec_local 

    return consec_max 

import matplotlib.pyplot as plt

tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

def grafTabMeteo(t):
    datas = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]
    temps_min = [min for _, min, *_ in t]
    temps_max = [max for _, _, max, _ in t]
    precs = [prec for _, _, _, prec in t]
    plt.plot(datas,temps_min, label = "Temp Mínima")
    plt.plot(datas,temps_max, label = "Temp Máxima")
    plt.xlabel("Data")
    plt.ylabel("Temperatura ºC")
    plt.title("Temperatura Mínima e Máxima")
    plt.legend()
    plt.grid(True) #para por grelha
    plt.show()

    # Precipitação
    plt.bar(datas,precs)
    plt.xlabel("Data")
    plt.ylabel("Precipitação mm")
    plt.title("Precipitação")
    plt.show()

    return


def menu():
    print("-----------Menu-----------------")
    print(" (1) - Temperatura média de cada dia")
    print(" (2) - Guardar uma tabela meteorológica num ficheiro de texto")
    print(" (3) - Carregar uma tabela meteorológica de um ficheiro de texto")
    print(" (4) - Temperatura mínima mais baixa registada na tabela")
    print(" (5) - Amplitude térmica de cada dia")
    print(" (6) - Dia em que a precipitação registada teve o seu valor máximo")
    print(" (7) - Dias em que a precipitação foi superior ao limite escolhido (p)")
    print(" (8) - Maior número consecutivo de dias com precipitação abaixo do limite escolhido")
    print(" (9) - Desenho dos gráficos da temperatura mínima, máxima e de pluviosidade")
    print(" (0) - Sair da aplicação")


menu()

op = int(input("Introduza uma das opções: "))

while op != 0:
    if op == 1:
        print(medias(tabMeteo1))
    
    elif op == 2:
        ficheiro = input("Qual vai ser o nome do ficheiro?")
        guardaTabMeteo(tabMeteo1, ficheiro)
        print("Ficheiro criado com sucesso")

    elif op == 3:
        print(carregaTabMeteo(ficheiro))

    elif op == 4:
        print(minMin(tabMeteo1))
    
    elif op == 5:
        print(amplTerm(tabMeteo1))

    elif op == 6:
        print(maxChuva(tabMeteo1))

    elif op == 7:
        p = int(input("Qual vai ser o limite escohido?"))
        print(diasChuvosos(tabMeteo1, p))

    elif op == 8:
        p = int(input("Qual vai ser o limite escohido?"))
        print(maxPeriodoCalor(tabMeteo1,p))

    elif op == 9: 
        grafTabMeteo(tabMeteo1)

    menu()
    op = int(input("Introduza uma das opções: "))

if op == 0:
    print("Obrigada, Volte sempre!")
