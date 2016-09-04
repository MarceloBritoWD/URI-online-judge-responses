import math

vezes = int(input())
cont = 0

while cont < vezes:
	entrada = int(input())
	contaDivisores = 0
	raiz = int(math.sqrt(entrada)+1)
	
	for i in range(1, raiz):
		if entrada % i == 0:
			contaDivisores += 1
		
	if contaDivisores > 1:
		print("Not Prime")
	else:
		print("Prime")
	
	cont += 1