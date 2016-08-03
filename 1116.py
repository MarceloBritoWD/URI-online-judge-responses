vezes = int(input())
 
cont = 1
 
while cont <= vezes:
    valores = input().split()
    X = int(valores[0])
    Y = int(valores[1])
     
    if X < 0 and Y == 0:
        print("divisao impossivel")
        
    elif X == 0 and Y < 0:
        print("divisao impossivel")
        
    elif X > 0 and Y == 0:
        print("divisao impossivel")
     
    else:
        divisao = X/Y
        print("%.1f" %divisao)
     
    cont += 1