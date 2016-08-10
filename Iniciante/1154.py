verdade = True
while verdade == True:
    soma = 0
    cont = 0 
    idade = int(input())
    
    while idade >= 0:
        soma = idade + soma
        cont += 1
        idade = int(input())
    verdade = False
    
media = soma/cont
print("%.2f" %media)