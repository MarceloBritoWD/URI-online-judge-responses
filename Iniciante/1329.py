valor = int(input());

while True:
	if valor == 0:
		break;

	else:
		casos = input().split();
		count = 0;
		maryWons = 0;
		johnWons = 0;

		while count < len(casos):

			if casos[count] == "0":
				maryWons += 1;

			elif casos[count] == "1":
				johnWons += 1;

			count+=1

		print("Mary won " + str(maryWons) + " times and John won " + str(johnWons) + " times");

	valor = int(input());
