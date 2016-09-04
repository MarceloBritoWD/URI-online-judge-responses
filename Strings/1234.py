while 1:
	try:
		entrada = input();
		final = ""
		cont = 1;
		
		for i in entrada:
			if i != " ":
				if (cont % 2) == 0:
					i = i.lower()
					cont += 1
					final += i
				else:
					i = i.upper()
					cont += 1
					final+= i
					
			else:
				final += i
		
		
		print(final)
		
	except:
		break;