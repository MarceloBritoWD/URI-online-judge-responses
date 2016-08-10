valor = int(input());

while (valor != 0):
	pilhaDeCartas = [];
	cont = 1;
	while (cont <= valor):
		pilhaDeCartas.append(cont);
		cont += 1;
		
	cartasDescartadas = "";
	while (len(pilhaDeCartas) >= 2):
		cartasDescartadas += str(pilhaDeCartas[0]);
		if len(pilhaDeCartas) != 2:
			cartasDescartadas += ", ";
		
		pilhaDeCartas.pop(0);
		pilhaDeCartas.append(pilhaDeCartas[0])
		pilhaDeCartas.pop(0);
	
	print("Discarded cards:", cartasDescartadas);
	print("Remaining card:", str(pilhaDeCartas[0]));
	
	pilhaDeCartas = [];
	valor = int(input());