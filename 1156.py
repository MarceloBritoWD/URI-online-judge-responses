s1 = 1
cont = 3
cont2 = 2
soma = 0
while cont <= 39:
    s2 = cont/cont2
    soma = soma + s2
     
    cont += 2
    cont2 *= 2
 
S = s1 + soma
print("%.2f" %S)