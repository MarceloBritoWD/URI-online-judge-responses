# -*- coding: utf-8 -*-

valores1 = input().split()
valores2 = input().split()

x1 = float(valores1[0])
y1 = float(valores1[1])

x2 = float(valores2[0])
y2 = float(valores2[1])


etapa1 = x2 - x1
etapa2 = y2 - y1

resultado1 = etapa1 * etapa1 
resultado2 = etapa2 * etapa2

import math

distancia = math.sqrt(resultado1 + resultado2)


print("%.4f" %distancia)