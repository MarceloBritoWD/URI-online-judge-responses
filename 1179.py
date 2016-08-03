cont = 1
lista_um = []
lista_dois = []

while cont <= 15:
    valor = int(input())
    
    if valor%2 == 0:
        lista_um.append(valor)
        
    else:
        lista_dois.append(valor)
        
    
    if len(lista_um) == 5:
        i = 0
        while i < 5:
            print("par[" + str(i) + "] = " + str(lista_um[i]))
            i += 1
        del lista_um
        lista_um = []
        
        
    if len(lista_dois) == 5:
        i = 0
        while i < 5:
            print("impar[" + str(i) + "] = " + str(lista_dois[i]))
            i += 1
        del lista_dois
        lista_dois = []
        
    
    
    if cont == 15:
        if len(lista_dois) > 0:
            i = 0
            while i < len(lista_dois):
                print("impar[" + str(i) + "] = " + str(lista_dois[i]))
                i += 1
                
        if len(lista_um) > 0:
            i = 0
            while i < len(lista_um):
                print("par[" + str(i) + "] = " + str(lista_um[i]))
                i += 1
    cont += 1