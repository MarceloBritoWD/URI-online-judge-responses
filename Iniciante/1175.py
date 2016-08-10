list = []
cont = 0

while cont <= 19:
    valor = int(input())
    list.append(valor)
    cont += 1

u = -1
i = 0
while i < len(list):
    print("N[" + str(i) + "] = " + str(list[u]))
    
    i += 1
    u -= 1