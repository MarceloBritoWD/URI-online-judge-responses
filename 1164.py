vezes = int(input())
cont = 1

while cont <= vezes:
    valor = int(input())
    div = 1
    soma = 0
    
    while valor != div:
        if (valor%div) == 0:
            soma = soma + div
        div += 1
        
    if soma == valor:
        print(str(valor) + " eh perfeito")
    
    else:
        print(str(valor) + " nao eh perfeito")
        
    cont += 1