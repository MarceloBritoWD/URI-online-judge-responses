vezes = int(input())
cont = 1
 
while cont <= vezes:
    valor = int(input())
    
    quantidade = 0
    div = 1
    while div <= valor:
        
        if valor%div == 0:
            quantidade = quantidade + 1
        div = div + 1
        
    if quantidade == 2:
        print(str(valor) + " eh primo")
    else:
        print(str(valor) + " nao eh primo")
        
    cont += 1