vezes = int(input())
cont = 0
list = []

while cont < vezes:

    valor = int(input())
    foo = valor
    A = 0
    B = 1

    while 0 < (valor+1):
        if (valor+1) == 1:
            list.append(A)

        else:
            list.append(A)
            C = A + B
            A = B
            B = C

        valor -= 1

    print("Fib(" + str(foo) + ") = " + str(list[-1]))
    list = []

    cont += 1
