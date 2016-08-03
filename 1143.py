valor = int(input())
cont = 1

while cont <= valor:
    
    print(cont, end=" ")
    print(cont*cont, end=" ")
    print(cont*cont*cont, end="" + "\n")

    cont += 1