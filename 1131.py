grenal = input().split()
inter = int(grenal[0])
gremio = int(grenal[1])


grenais = 1
vitorias_inter = 0
vitorias_gremio = 0
empates = 0

if inter > gremio:
    vitorias_inter = vitorias_inter + 1

elif gremio > inter:
    vitorias_gremio = vitorias_gremio + 1

elif inter == gremio:
    empates = empates + 1


print("Novo grenal (1-sim 2-nao)")
novo_grenal = int(input())


while novo_grenal == 1:
    grenal = input().split()
    inter = int(grenal[0])
    gremio = int(grenal[1])
    grenais = grenais + 1
    
    if inter > gremio:
        vitorias_inter = vitorias_inter + 1
    
    elif gremio > inter:
        vitorias_gremio = vitorias_gremio + 1
    
    elif inter == gremio:
        empates = empates + 1
    
    print("Novo grenal (1-sim 2-nao)")
    novo_grenal = int(input())


if novo_grenal == 2:
    print(str(grenais) + " grenais")
    print("Inter:" + str(vitorias_inter))
    print("Gremio:" + str(vitorias_gremio))
    print("Empates:" + str(empates))
    
    if vitorias_inter > vitorias_gremio:
        print("Inter venceu mais")
    
    elif vitorias_gremio > vitorias_inter:
        print("Gremio venceu mais")
        
    else:
        print("Nao houve vencedor")