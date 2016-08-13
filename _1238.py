vezes = int(input());
contVezes = 1;

while contVezes <= vezes:
	foo = input().split();
	fooParte1 = str(foo[0]);
	fooParte2 = str(foo[1]);
	StringFinal = ""
			
	cont = 0
	while cont < len(list(fooParte1)) and cont < len(list(fooParte2)):
		
		if (fooParte1[cont]):
			StringFinal += fooParte1[cont]
			
		if (fooParte2[cont]):
			StringFinal += fooParte2[cont]
			
		cont += 1
	
	fooParte1Final = ""
	fooParte2Final = ""

	fooParte1Final = fooParte1[(cont):]
	fooParte2Final = fooParte2[(cont):]
	
	StringFinal = StringFinal + fooParte1Final + fooParte2Final;
	print(StringFinal)

	contVezes += 1;
print()