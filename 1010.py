# -*- coding: utf-8 -*-

peca1 = input().split()
peca2 = input().split()

peca1_codigo = int(peca1[0])
peca1_numero = int(peca1[1])
peca1_valor = float(peca1[2])

peca2_codigo = int(peca2[0])
peca2_numero = int(peca2[1])
peca2_valor = float(peca2[2])

valor_total = (peca1_numero*peca1_valor) + (peca2_numero*peca2_valor)

print("VALOR A PAGAR: R$ %.2f" % valor_total)