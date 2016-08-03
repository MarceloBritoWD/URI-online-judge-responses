valores = input().split()

valor1 = int(valores[0])
valor2 = int(valores[1])

cont = 1

while cont <= valor2:
    if cont%valor1 == 0:
        print(cont, end="" + "\n")
    
    elif cont%valor1 != 0:
        print(cont, end=" ")
    
    cont += 1