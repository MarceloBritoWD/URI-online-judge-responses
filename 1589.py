vezes = int(input());
count = 1

while count <= vezes:
	cabos = input().split();
	cabo1 = int(cabos[0]);
	cabo2 = int(cabos[1]);

	print(cabo1 + cabo2)
	count += 1