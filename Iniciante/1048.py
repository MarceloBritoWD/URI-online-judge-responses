# -*- coding: utf-8 -*-

salario = float(input())



if salario <= 400.00:
    reajuste_calc = (15/100) * salario
    novo_salario = salario + reajuste_calc
    reajuste = novo_salario - salario
    print("Novo salario: %.2f" %novo_salario)
    print("Reajuste ganho: %.2f" %reajuste)
    print("Em percentual: 15 %")
    
elif salario >= 400.01 and salario <= 800.00:
    reajuste_calc = (12/100) * salario
    novo_salario = salario + reajuste_calc
    reajuste = novo_salario - salario
    print("Novo salario: %.2f" %novo_salario)
    print("Reajuste ganho: %.2f" %reajuste)
    print("Em percentual: 12 %")
    
elif salario >= 800.01 and salario <= 1200.00:
    reajuste_calc = (10/100) * salario
    novo_salario = salario + reajuste_calc
    reajuste = novo_salario - salario
    print("Novo salario: %.2f" %novo_salario)
    print("Reajuste ganho: %.2f" %reajuste)
    print("Em percentual: 10 %")
    
elif salario >= 1200.01 and salario <= 2000.00:
    reajuste_calc = (7/100) * salario
    novo_salario = salario + reajuste_calc
    reajuste = novo_salario - salario
    print("Novo salario: %.2f" %novo_salario)
    print("Reajuste ganho: %.2f" %reajuste)
    print("Em percentual: 7 %")
    
elif salario > 2000.00:
    reajuste_calc = (4/100) * salario
    novo_salario = salario + reajuste_calc
    reajuste = novo_salario - salario
    print("Novo salario: %.2f" %novo_salario)
    print("Reajuste ganho: %.2f" %reajuste)
    print("Em percentual: 4 %")