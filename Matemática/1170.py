casos = int(input());
count = 0;

while count < casos:
	suprimento = float(input())
	dias = 0
	
	while suprimento > 1:
		suprimento = suprimento / 2
		dias += 1
	
	print("%s dias" %dias)
	
	count += 1