valor1 = int(input())
valor2 = int(input())

while valor2 <= valor1:
    valor2 = int(input())

cont = 1
continua = True
valorInc = valor1 + 1

while continua:

    passou = valor1 + valorInc
    if passou > valor2:
        continua = False

    else:
        valorInc = valorInc + 1
        valor1 = passou

    cont += 1

print(cont)
