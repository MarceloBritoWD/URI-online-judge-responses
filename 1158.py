vezes = int(input())
cont = 1

while cont <= vezes:
    valores = input().split()
    valor1 = int(valores[0])
    valor2 = int(valores[1])
    
    cont2 = 1
    soma = 0
    
    while cont2 <= (valor2*2):
        if valor1%2 != 0:
            soma = soma + valor1
        valor1 += 1
        cont2 += 1
        
    print(soma)
    cont += 1