valor = int(input())
soma = 0
novo_valor = 1

while 1 <= valor:
    soma = valor * novo_valor
    novo_valor = soma
    valor -= 1
print(soma)