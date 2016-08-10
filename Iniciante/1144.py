valor = int(input())
cont = 1

while cont <= valor:
    
    print(cont, end=" ")
    print(cont*cont, end=" ")
    print(cont*cont*cont, end="" + "\n")
    
    print(cont, end=" ")
    print(cont*cont+1, end=" ")
    print(cont*cont*cont+1, end="" + "\n")

    cont += 1