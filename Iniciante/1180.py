tamanhoVetor = int(input());
vetor = input().split();
vetorInt = [];

for i in vetor:
	vetorInt.append(int(i));


menor = 0;
posicaoDoMenor = 0;

for i in vetorInt:
	
	if i < menor:
		menor = i;
		posicaoDoMenor = vetorInt.index(i);
		

print("Menor valor:", menor);
print("Posicao:", posicaoDoMenor)
