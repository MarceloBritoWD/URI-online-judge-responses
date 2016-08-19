vezes = int(input())
cont = 0

while cont < vezes:
	entrada = list(input())
	
	soma = 0.08
	for i in entrada:
		if i == 'e':
			soma += 0.01
	
	print('%.2f' % soma)
	cont += 1
