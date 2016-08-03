# -*- coding: utf-8 -*-

Vendedor = input()
Salario = float(input())
Vendas = float(input())

Recebe = Salario + (Vendas * 15/100)

print("TOTAL = R$ %.2f" % Recebe)
