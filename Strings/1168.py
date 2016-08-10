vezes = int(input());
count = 1

while count <= vezes:

	valores = input();
	i = 0;
	soma = 0;
	
	while i < len(valores):

		if valores[i] == "1":
			soma += 2;

		elif valores[i] == "2" or valores[i] == "3" or valores[i] == "5":
			soma += 5;

		elif valores[i] == "4":
			soma += 4;

		elif valores[i] == "6" or valores[i] == "9" or valores[i] == "0":
			soma += 6;

		elif valores[i] == "7":
			soma += 3;

		else:
			soma += 7;

		
		i += 1;
		
		
	print(str(soma) + " leds");
	count += 1;