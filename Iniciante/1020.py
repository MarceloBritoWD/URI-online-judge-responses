# -*- coding: utf-8 -*-

idade = int(input())
ano_normal = 365
mes_normal = 30

Anos = int(idade/ano_normal)
Meses = int((idade % ano_normal) / mes_normal)
Dias = int((idade % ano_normal) % mes_normal)

print(str(Anos) + " ano(s)")
print(str(Meses) + " mes(es)")
print(str(Dias) + " dia(s)")