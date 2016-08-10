cont = 1
soma = 0
nota = float(input())

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