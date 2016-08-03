list = []
valor = int(input())
valor_mesmo = 0

i = 0
while len(list) <= 999:
    list.insert(valor_mesmo, i)
    print("N[" + str(len(list)-1) + "] = " + str(list.index(i)))
    
    i += 1
    if valor_mesmo < (valor-1):
        valor_mesmo += 1
    else:
        valor_mesmo = 0