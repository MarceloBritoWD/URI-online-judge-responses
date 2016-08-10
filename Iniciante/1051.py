# -*- coding: utf-8 -*-

renda = float(input())

if renda >= 0 and renda <= 2000.00:
    print("Isento")
    
elif renda >= 2000.01 and renda <= 3000.00:
    imposto = (8/100) * (renda - 2000.01)
    print("R$ %.2f" %imposto)
    
elif renda >= 3000.01 and renda <= 4500.00:
    imposto = (18/100) * (renda - 3000.01)
    dif_anterior = (8/100) * (3000.00 - 2000.01)
    imposto_total = imposto + dif_anterior
    print("R$ %.2f" %imposto_total)
    
elif renda > 4500.00:
    imposto = (28/100) * (renda - 4500.00)
    dif_anterior = (8/100) * (3000.00 - 2000.01)
    dif_anterior2 = (18/100) * ( 4500.00 - 3000.01)
    imposto_total = imposto + dif_anterior + dif_anterior2
    print("R$ %.2f" %imposto_total)