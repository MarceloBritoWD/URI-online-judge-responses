valor1 = int(input())
valor2 = int(input())

soma = 0

if valor1 < valor2:
    while valor1 <= valor2:
        if valor1%13 != 0:
            soma = soma + valor1
        
        valor1 += 1
    
    print(soma)
    
elif valor2 < valor1:
    while valor2 <= valor1:
        if valor2%13 != 0:
            soma = soma + valor2
        
        valor2 += 1
    
    print(soma)