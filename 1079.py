vezes = int(input())
cont = 1

while cont <= vezes:
    valores = input().split()
    
    valor1 = float(valores[0])
    valor2 = float(valores[1])
    valor3 = float(valores[2])
    
    peso1 = valor1 * 2
    peso2 = valor2 * 3
    peso3 = valor3 * 5
    
    media = (peso1 + peso2 + peso3)/10
    
    print("%.1f" %media)
    
    
    cont += 1