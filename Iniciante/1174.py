list = []
cont = 0
i = 0
while cont <= 99:
    valor = float(input())
    list.insert(i, valor)
    cont += 1
    i += 1

u = 0
while u < len(list):
    
    if list[u] <= 10:
        print("A[" + str(u) + "] = " + "%.1f" %list[u])
    u += 1