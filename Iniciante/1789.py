while 1:
	try:
		tamanhoLista = int(input())
		entrada = input().split()
		entradaInt = []
		
		maior = 0
		for i in entrada:
			entradaInt.append(int(i))
			if int(i) >= maior:
				maior = int(i)
				
		if maior < 10:
			print(1)
		
		elif maior >= 10 and maior < 20:
			print(2)
			
		else:
			print(3)
	except:
		break;
