list = []
valor = float(input())
list.append(valor)

cont = 0
i = 0
meio = list[i]
while cont <= 99:

    print("N[" + str(cont) + "] = " + "%.4f" %meio)
    
    meio = meio/2
    cont += 1