# -*- coding: utf-8 -*-

valores = input().split()

codigo = int(valores[0])
quantidade = int(valores[1])

if codigo == 1:
    preco = 4.00

elif codigo == 2:
    preco = 4.50
    
elif codigo == 3:
    preco = 5.00
    
elif codigo == 4:
    preco = 2.00
    
elif codigo == 5:
    preco = 1.50

pagar = quantidade * preco

print("Total: R$ %.2f" %pagar )