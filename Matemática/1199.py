while 1:
	entrada = input()
	if entrada == "-1":
		break;
	
	elif  len(entrada) > 1 and entrada[1] == "x":
		print(int(entrada, 16))
		
	else:
		i = hex(int(entrada))
		i = i[0:2] + i[2:].upper()
		print(i)