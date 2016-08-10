valor1 = int(input())
valor2 = int(input())

if valor1 < valor2:
    valor1 += 1
    
    while valor1 < valor2:
        if valor1%5==2 or valor1%5==3:
            print(valor1)
        
        valor1 += 1
    

if valor2 < valor1:
    valor2 += 1
    
    while valor2 < valor1:
        if valor2%5==2 or valor2%5==3:
            print(valor2)
        
        valor2 += 1