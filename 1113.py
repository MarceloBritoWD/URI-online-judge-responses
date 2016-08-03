valores = input().split()
    
X = int(valores[0])
Y = int(valores[1])


while X != Y:
    if X > Y:
        print("Decrescente")
        
    elif X < Y:
        print("Crescente")
    
    valores = input().split()
    
    X = int(valores[0])
    Y = int(valores[1])