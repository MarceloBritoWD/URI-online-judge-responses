cont = 1
soma = 0
nota = float(input())
continua = True

while continua:
    while cont <= 2:
        
        if nota >= 0 and nota <= 10:
            cont += 1
            soma = soma + nota
            
        if nota < 0 or nota > 10:
            print("nota invalida")
            
        if cont <= 2:
            nota = float(input())
    
    media = soma / 2
    print("media = %.2f" %media)

    print("novo calculo (1-sim 2-nao)")
    entrada = int(input())
    
    while entrada < 1 or entrada > 2:
        print("novo calculo (1-sim 2-nao)")
        entrada = int(input())

    if entrada == 1:
        cont = 1
        soma = 0
        nota = float(input())
        
    elif entrada == 2:
        continua = False