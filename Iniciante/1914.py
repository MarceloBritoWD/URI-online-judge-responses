vezes = int(input());
count = 1;

while count <= vezes:

	jogada = input().split();
	numerosJogadas = input().split();

	numero1 = int(numerosJogadas[0]);
	numero2 = int(numerosJogadas[1]);

	resultado = numero1 + numero2;

	if (resultado%2) == 0 and jogada[1] == "PAR":
		vencedor = jogada[0];

	elif (resultado%2) != 0 and jogada[1] == "IMPAR":
		vencedor = jogada[0];

	elif (resultado%2) != 0 and jogada[3] == "IMPAR":
		vencedor = jogada[2]

	elif (resultado%2) == 0 and jogada[3] == "PAR":
		vencedor = jogada[2]

	print(vencedor)

	count += 1;
