vezes = int(input());
count = 1;

while count <= vezes:
	bla = raw_input();
	valores = bla.split();
	nome = valores[0];
	forcaNewtons = int(valores[1]);

	thor = "Thor"

	if (nome != thor):
		print "N"

	else:
		print "Y" 

	count += 1
	