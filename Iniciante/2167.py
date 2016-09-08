tamArray = int(input()) #python discard
entrada = input().split()
maior = 0
posicaoMenor = 0

for i in entrada:
	if int(i) > maior:
		maior = int(i)

	if int(i) < maior:
		posicaoMenor = entrada.index(i)+1
		break;

print(posicaoMenor)
