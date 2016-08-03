# -*- coding: utf-8 -*-

valores = input().split()

A = float(valores[0])
B = float(valores[1])

if A == 0 and B == 0:
    print("Origem")

elif A > 0 and B > 0:
    print("Q1")
    
elif A < 0 and B < 0:
    print("Q3")
    
elif A > 0 and B < 0:
    print("Q4")
    
elif A < 0 and B > 0:
    print("Q2")
    
elif A == 0:
    print("Eixo Y")
    
elif B == 0:
    print("Eixo X")