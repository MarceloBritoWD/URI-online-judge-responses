testes = int(input());
contTestes = 0;

while contTestes < testes:
	todosDiamantes = input();
	aberturasDeDiamante = [];
	cont = 0;

	for pedaco in todosDiamantes:
		if (pedaco == '<'):
			aberturasDeDiamante.append(pedaco);

		if (pedaco == '>') and (len(aberturasDeDiamante) >= 1):
			aberturasDeDiamante.pop(-1);
			cont += 1;

	print(cont);
	contTestes += 1;
