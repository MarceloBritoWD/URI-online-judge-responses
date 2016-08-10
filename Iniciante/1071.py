valor1 = int(input())
valor2 = int(input())


if valor1 < valor2:

    soma = 0
    valor2 -= 1
    
    while valor1 < valor2:
        valor1 = valor1 + 1
        
        if valor1%2 != 0:
            soma = valor1 + soma
            
    print(soma)
    
    
    
elif valor2 < valor1:
    
    soma = 0
    valor1 -= 1
    
    while valor2 < valor1:
        valor2 += 1
        
        if valor2%2 != 0:
            soma = valor2 + soma
            
    print(soma)
    

else:
    soma = 0
    print(soma)