# -*- coding: utf-8 -*-

valores = input().split()

valor1 = int(valores[0])
valor2 = int(valores[1])
valor3 = int(valores[2])

if valor1 > valor2 and valor1 > valor3:
    print(str(valor1) + " eh o maior")
    
elif valor2 > valor1 and valor2 > valor3:
    print(str(valor2) + " eh o maior")

else:
    print(str(valor3) + " eh o maior")