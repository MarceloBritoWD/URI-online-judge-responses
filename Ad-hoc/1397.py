qtdRodadas = int(input())

while qtdRodadas != 0:
	contRodadas = 0
	placar = [0, 0]

	while contRodadas < qtdRodadas:
		A, B = map(int, input().split())

		if A > B:
			placar[0] += 1

		elif A < B:
			placar[1] += 1

		contRodadas += 1
	print(placar[0], placar[1])

	qtdRodadas = int(input())
