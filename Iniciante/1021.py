# -*- coding: utf-8 -*-

valor = float(input())

nota100_normal = 100
nota50_normal = 50
nota20_normal = 20
nota10_normal = 10
nota5_normal = 5
nota2_normal = 2

moeda1_normal = 1
moeda50_normal = 0.50
moeda25_normal = 0.25
moeda10_normal = 0.10
moeda5_normal = 0.05
moeda1c_normal = 0.01

nota100 = int(valor/nota100_normal)

nota50_pre = valor%nota100_normal
nota50 = int(nota50_pre/nota50_normal)

nota20_pre = nota50_pre%nota50_normal
nota20 = int(nota20_pre/nota20_normal)

nota10_pre = nota20_pre%nota20_normal
nota10 = int(nota10_pre/nota10_normal)

nota5_pre = nota10_pre%nota10_normal
nota5 = int(nota5_pre/nota5_normal)

nota2_pre = nota5_pre%nota5_normal
nota2 = int(nota2_pre/nota2_normal)

moeda1_pre = nota2_pre%nota2_normal
moeda1 = int(moeda1_pre/moeda1_normal)

moeda50_pre = moeda1_pre%moeda1_normal
moeda50 = int(moeda50_pre/moeda50_normal)

moeda25_pre = moeda50_pre%moeda50_normal
moeda25 = int(moeda25_pre/moeda25_normal)

moeda10_pre = moeda25_pre%moeda25_normal
moeda10 = int(moeda10_pre/moeda10_normal)

moeda5_pre = moeda10_pre%moeda10_normal
moeda5 = int(moeda5_pre/moeda5_normal)

moeda1c_pre = moeda5_pre%moeda5_normal
moeda1c = int(moeda1c_pre/moeda1c_normal)


print("NOTAS:")
print(str(nota100) + " nota(s) de R$ 100.00")
print(str(nota50) + " nota(s) de R$ 50.00")
print(str(nota20) + " nota(s) de R$ 20.00")
print(str(nota10) + " nota(s) de R$ 10.00")
print(str(nota5) + " nota(s) de R$ 5.00")
print(str(nota2) + " nota(s) de R$ 2.00")


print("MOEDAS:")
print(str(moeda1) + " moeda(s) de R$ 1.00")
print(str(moeda50) + " moeda(s) de R$ 0.50")
print(str(moeda25) + " moeda(s) de R$ 0.25")
print(str(moeda10) + " moeda(s) de R$ 0.10")
print(str(moeda5) + " moeda(s) de R$ 0.05")
print(str(moeda1c) + " moeda(s) de R$ 0.01")


