valores = input().split()

X = int(valores[0])
Y = int(valores[1])

while X != 0 and Y != 0:
    if X > 0 and Y > 0:
        print("primeiro")
    
    if X > 0 and Y < 0:
        print("quarto")
        
    if X < 0 and Y < 0:
        print("terceiro")
    
    if X < 0 and Y > 0:
        print("segundo")
        
    valores = input().split()
    X = int(valores[0])
    Y = int(valores[1])