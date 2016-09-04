while 1:
	try:
		entrada = input().split()
		exercito1 = int(entrada[0])
		exercito2 = int(entrada[1])

		if exercito1 > exercito2:
			print(exercito1 - exercito2)

		else:
			print(exercito2 - exercito1)

	except:
		break;