# -*- coding: utf-8 -*-

valor = int(input())
valor_show = 1

while (valor_show <= valor):
    if (valor_show % 2) != 0:
        print(valor_show)
    valor_show = valor_show + 1
    