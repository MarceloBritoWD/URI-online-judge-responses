def verificaTermos(item):
	if len(item) == 1:
		l = []
		l.append("0")
		l.append(item)
		item = ''.join(l)
	return item

vezes = int(input())
cont = 0

while cont < vezes:
	entrada = input().split()
	hora = entrada[0]
	minuto = entrada[1]
	ocorrencia = entrada[2]

	hora = verificaTermos(hora)
	minuto = verificaTermos(minuto)

	if ocorrencia == str(1):
		print(hora + ":" + minuto + " - A porta abriu!")
	else:
		print(hora + ":" + minuto + " - A porta fechou!")

	cont += 1
