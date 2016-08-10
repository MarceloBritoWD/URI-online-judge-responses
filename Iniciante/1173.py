list = []
valor = int(input())

while len(list) <= 9:
    list.append(valor)
    valor = valor * 2

i = 0
while i < len(list):
    print("N[" + str(i) + "] = " + str(list[i]))
    i += 1