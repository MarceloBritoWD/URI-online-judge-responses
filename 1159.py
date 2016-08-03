valor = int(input())

while valor != 0:
    cont = 1
    soma = 0
    
    while cont <= 5:
        if valor%2==0:
            soma = valor + soma
            cont += 1
        valor += 1
        
    print(soma)
    valor = int(input())