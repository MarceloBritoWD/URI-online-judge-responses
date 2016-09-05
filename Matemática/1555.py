def funcaoRafael(x, y):
	a = (3*x)*(3*x)
	b = y*y
	return a + b
	
def funcaoBeto(x, y):
	a = 2*(x*x)
	b = (5*y)*(5*y)
	return a + b

def funcaoCarlos(x, y):
	a = (100*-1)*x
	b = y*y*y
	return a + b
	
	
def pegarMaior(x, y, z):
	maior = 0
	# acumula o maior
	if x > maior:
		maior = x
		
	if y > maior:
		maior = y
		
	if z > maior:
		maior = z
		
	# Retorna o maior
	if maior == x:
		return "x"
		
	elif maior == y:
		return "y"
		
	elif maior == z:
		return "z"


# main
vezes = int(input())
cont = 0

while cont < vezes:
	entrada = input().split()
	parte1 = int(entrada[0])
	parte2 = int(entrada[1])
	
	if (pegarMaior(funcaoRafael(parte1, parte2), funcaoBeto(parte1, parte2), funcaoCarlos(parte1, parte2))) == "x":
		print("Rafael ganhou")
		
	elif (pegarMaior(funcaoRafael(parte1, parte2), funcaoBeto(parte1, parte2), funcaoCarlos(parte1, parte2))) == "y":
		print("Beto ganhou")
		
	elif (pegarMaior(funcaoRafael(parte1, parte2), funcaoBeto(parte1, parte2), funcaoCarlos(parte1, parte2))) == "z":
		print("Carlos ganhou")
		
	cont += 1