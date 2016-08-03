valores = input().split()

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

x = (B**2)-(4*A*C)

if x < 0:
    print("Impossivel calcular")
    
elif A <= 0:
    print("Impossivel calcular")

else:
    import math
    
    x = math.sqrt(x)
    
    R1 = (-B+x)/(2*A)
    R2 = (-B-x)/(2*A)
    
    print("R1 = %.5f" %R1)
    print("R2 = %.5f" %R2)