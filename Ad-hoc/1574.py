vezes = int(input())
cont = 0

while cont < vezes:
	qtdIntrucoes = int(input())
	movimentos = []
	posicao = 0
	contMovimentos = 0

	
	while contMovimentos < qtdIntrucoes:
		movimento = input()

		if movimento == "LEFT":
			posicao -= 1
			movimentos.append("LEFT")

		elif movimento == "RIGHT":
			posicao += 1
			movimentos.append("RIGHT")

		else:
			foo = movimento[8:]
			if movimentos[int(foo)-1] == "LEFT":
				posicao -= 1
				movimentos.append("LEFT")

			elif movimentos[int(foo)-1] == "RIGHT":
				posicao += 1
				movimentos.append("RIGHT")

		contMovimentos += 1

	print(posicao)
	cont += 1
