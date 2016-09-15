entrada = input()
vogais = ['a', 'e', 'i', 'o', 'u']
final = ""

for i in entrada:
    if i in vogais:
        final += i

invertido = final[::-1]

if invertido == final:
    print("S")
else:
    print("N")
