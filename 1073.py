valor = int(input())
cont = 1

while cont <= valor:
    if cont % 2 == 0:
        cont_quadrado = cont*cont
        print(str(cont) + "^2 = " + str(cont_quadrado))
    
    cont += 1