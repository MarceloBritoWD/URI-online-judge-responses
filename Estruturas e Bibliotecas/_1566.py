vezes = int(input());
cont = 0;

while (cont <= vezes):
	qtdPessoas = int(input());
	alturas = input().split();
	cont2 = 0
	
	while (cont2 < len(alturas)):
		alturas[cont2] = int(alturas[cont2]);
		cont2 += 1;

	alturas.sort();
	
	cont3 = 0;
	while (cont3 < len(alturas)):
		if (cont3 + 1) < (len(alturas)):
			print(alturas[cont3], end=" ");
			
		else:
			print(alturas[cont3]);
		
		cont3 += 1;
		
		
	cont += 1;
