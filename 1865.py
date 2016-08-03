vezes = int(input());
count = 1;

while count <= vezes:
	teste = raw_input();
	valores = teste.split();
	nome = valores[0];
	forcaNewtons = int(valores[1]);

	thor = "Thor"

	if (nome != thor):
		print "N"

	else:
		print "Y"

	count += 1
