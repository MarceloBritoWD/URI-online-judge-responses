list = []
cont = 1

while cont <= 10:
    valor = int(input())
    list.append(valor)
    cont += 1

i = 0
while i < len(list):
    if list[i] <= 0:
        print("X" + "[" + str(i) + "] = " + "1")
    else:
        print("X" + "[" + str(i) + "] = " + str(list[i]) )
    i += 1