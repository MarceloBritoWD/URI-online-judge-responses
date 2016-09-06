tamanho = int(input())
entrada = input().split()

multiplosDois = 0
multiplosTres = 0
multiplosQuatro = 0
multiplosCinco = 0

for i in entrada:
	if int(i) % 2 == 0:
		multiplosDois += 1
	if int(i) % 3 == 0:
		multiplosTres += 1
	if int(i) % 4 == 0:
		multiplosQuatro += 1
	if int(i) % 5 == 0:
		multiplosCinco += 1

print(str(multiplosDois) + " Multiplo(s) de 2")
print(str(multiplosTres) + " Multiplo(s) de 3")
print(str(multiplosQuatro) + " Multiplo(s) de 4")
print(str(multiplosCinco) + " Multiplo(s) de 5")
