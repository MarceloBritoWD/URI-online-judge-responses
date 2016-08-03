vezes = int(input())
cont = 1

total = 0
total_coelhos = 0
total_ratos = 0
total_sapos = 0

while cont <= vezes:
    exp = input().split()
    valor1 = int(exp[0])
    valor2 = exp[1]
    
    total = valor1 + total
    
    if valor2 == "C":
        total_coelhos = valor1 + total_coelhos
    
    if valor2 == "R":
        total_ratos = valor1 + total_ratos
    
    if valor2 == "S":
        total_sapos = valor1 + total_sapos
    cont += 1

print("Total: " + str(total) + " cobaias")
print("Total de coelhos: " + str(total_coelhos))
print("Total de ratos: " + str(total_ratos))
print("Total de sapos: " + str(total_sapos))

perc_coelhos = (total_coelhos*100)/total
perc_ratos = (total_ratos*100)/total
perc_sapos = (total_sapos*100)/total

print("Percentual de coelhos: %.2f" %perc_coelhos + " %")
print("Percentual de ratos: %.2f" %perc_ratos + " %")
print("Percentual de sapos: %.2f" %perc_sapos + " %")