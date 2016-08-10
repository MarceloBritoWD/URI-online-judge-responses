entrada = int(input())
tipo = input()
linha = []
matriz = []
tam = 11
while len(matriz) <= tam:
    
    while len(linha) <= tam:
        valor = float(input())
        linha.append(valor)
        
    matriz.append(linha)
    linha = []
if tipo == "S":
    cont = 0
    soma = 0
    while cont <= tam:
        soma = soma + matriz[cont][entrada]
        
        cont += 1
    print("%.1f" %soma)
        
    
elif tipo == "M":
    cont = 0
    media = 0
    soma = 0
    while cont <= tam:
        soma = soma + matriz[cont][entrada]
        cont += 1
    media = soma/(tam+1)
    print("%.1f" %media)