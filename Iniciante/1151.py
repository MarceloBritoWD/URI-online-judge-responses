valor = int(input())
A = 0
B = 1
 
print(A, end=" ")
A += 1
 
while 0 < (valor-1):
    if (valor-1) == 1:
        print(A, end="" + "\n")
    
    else:
        print(A, end=" ")
        C = A + B
        A = B
        B = C
     
    valor -= 1