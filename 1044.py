# -*- coding: utf-8 -*-

valores = input().split()

A = int(valores[0])
B = int(valores[1])


if A > B:
    if (A % B) == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
    
elif B > A:
    if (B % A) == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
    
        
