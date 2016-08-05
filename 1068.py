# -*- coding: utf-8 -*-

while True:
	try:
		expressao = input();
		parentesesIncompletos = [];
				
		for caractere in expressao:
			if caractere == '(':
				parentesesIncompletos.append(caractere);
				
			elif caractere == ')' and len(parentesesIncompletos) > 0:
				if parentesesIncompletos[-1] == '(':
					parentesesIncompletos.pop();
				
				elif parentesesIncompletos[-1] == caractere:
					parentesesIncompletos.append(caractere);

			elif caractere == ')' and len(parentesesIncompletos) == 0:
				parentesesIncompletos.append(caractere);
			
		if len(parentesesIncompletos) == 0:
			print("correct")
			
		else:
			print("incorrect")

	except:
		break;