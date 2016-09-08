entrada = input().split()
tempo1 = int(entrada[0])
tempo2 = int(entrada[1])

voltas = 1
dif = tempo2 - tempo1

while dif < tempo2:

	dif += tempo2-tempo1
	voltas += 1

print(voltas)
