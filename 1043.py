# -*- coding: utf-8 -*-

valores = input().split()

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])


if A < (B + C) and B < (A + C) and C < (A + B):
    perimetro = A + B + C
    print("Perimetro = %.1f" %perimetro)

else:
    area = (A + B)* C / 2
    print("Area = %.1f" %area)
