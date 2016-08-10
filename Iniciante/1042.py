# -*- coding: utf-8 -*-

valores1 = input().split()

A = int(valores1[0])
B = int(valores1[1])
C = int(valores1[2])

if A>B>C:
    print(C)
    print(B)
    print(A)
    print()
    print(A)
    print(B)
    print(C)

elif B>C>A:
    print(A)
    print(C)
    print(B)
    print()
    print(A)
    print(B)
    print(C)
    
elif C>A>B:
    print(B)
    print(A)
    print(C)
    print()
    print(A)
    print(B)
    print(C)
    
elif A<B<C:
    print(A)
    print(B)
    print(C)
    print()
    print(A)
    print(B)
    print(C)
    
elif B<C<A:
    print(B)
    print(C)
    print(A)
    print()
    print(A)
    print(B)
    print(C)

elif C<A<B:
    print(C)
    print(A)
    print(B)
    print()
    print(A)
    print(B)
    print(C)