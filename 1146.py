valor = int(input())

while valor != 0:
    cont = 1
    
    while cont <= valor:
        if cont == valor:
            print(cont)
        else:
            print(cont, end=" ")
        cont += 1
    valor = int(input())