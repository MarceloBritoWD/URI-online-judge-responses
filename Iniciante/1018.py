# -*- coding: utf-8 -*-

valor = int(input())

print(valor)
nota100_normal = 100
nota50_normal = 50
nota20_normal = 20
nota10_normal = 10
nota5_normal = 5
nota2_normal = 2
nota1_normal = 1
 
nota100 = int(valor/nota100_normal)

nota50_pre = valor % nota100_normal
nota50 = int(nota50_pre / nota50_normal)

nota20_pre = nota50_pre % nota50_normal
nota20 = int(nota20_pre/nota20_normal)

nota10_pre = nota20_pre%nota20_normal
nota10 = int(nota10_pre/nota10_normal)

nota5_pre = nota10_pre%nota10_normal
nota5 = int(nota5_pre/nota5_normal)

nota2_pre = nota5_pre%nota5_normal
nota2 = int(nota2_pre/nota2_normal)

nota1_pre = nota2_pre%nota2_normal
nota1 = int(nota1_pre/nota1_normal)

 
print(str(nota100) + " nota(s) de R$ 100,00")
print(str(nota50) + " nota(s) de R$ 50,00")
print(str(nota20) + " nota(s) de R$ 20,00")
print(str(nota10) + " nota(s) de R$ 10,00")
print(str(nota5) + " nota(s) de R$ 5,00")
print(str(nota2) + " nota(s) de R$ 2,00")
print(str(nota1) + " nota(s) de R$ 1,00")


