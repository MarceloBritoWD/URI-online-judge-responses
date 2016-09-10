while 1:
	try:
		discard = int(input())
		largada = input().split()
		chegada = input().split()

		contador = 0

		for i in range(len(largada)):
			if int(largada[i]) > int(chegada[i]):
				contador += (int(largada[i]) - int(chegada[i]))

		print(contador)

	except:
		break;
