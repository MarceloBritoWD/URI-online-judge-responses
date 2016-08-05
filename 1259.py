vezes = int(input());
cont = 0;
numerosPares = [];
numerosImpares = [];

while (cont < vezes):
	valor = int(input());
	
	if (valor%2) == 0:
		numerosPares.append(valor);
	else:
		numerosImpares.append(valor);
	cont += 1;

numerosPares.sort()
numerosImpares.sort(reverse=True);

for i in numerosPares:
	print(i);
	
for i in numerosImpares:
	print(i);