valores = input()
list = valores.split()
 
valor1 = int(list[0])
valor2 = int(list[1])
 
cont = 2
while valor2 <= 0:
    valor2 = int(list[cont])   
    cont += 1
     
cont = 1
valor1Inc = valor1 + 1
 
while cont < valor2:
    inteiro = valor1 + valor1Inc
     
    cont += 1
    if cont == valor2:
        break
    else:
        valor1Inc = valor1Inc + 1
        valor1 = inteiro
     
print(inteiro)