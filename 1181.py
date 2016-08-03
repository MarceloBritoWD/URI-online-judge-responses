entrada = int(input())
tipo = input()
linha = []
matriz = []

soma = 0
while len(matriz) <= 11:
    
    while len(linha) <= 11:
        valor = float(input())
        linha.append(valor)
        
    matriz.append(linha)
    linha = []

if tipo == "S":
    soma = soma + sum(matriz[entrada])
    print(soma)
    
elif tipo == "M":
    media = sum(matriz[entrada])/12
    print(media)
