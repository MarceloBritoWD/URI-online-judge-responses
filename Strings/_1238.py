foo = input().split();

fooParte1 = str(foo[0]);
fooParte2 = str(foo[1]);

StringFinal = ""
		
		
cont = 0
while cont <= (len(list(fooParte1)) and cont <= len(list(fooParte2))):
	StringFinal += fooParte1[cont]
	StringFinal += fooParte2[cont]
	cont += 1

i = 0;
while i <= int(cont/2):
	fooParte1Final = fooParte1.replace(fooParte1[i], "");
	fooParte2Final = fooParte2.replace(fooParte2[i], "");
	i += 1;
	
print(fooParte1Final)
print(fooParte2Final)

		

# StringFinal = StringFinal + (fooParte1Final + fooParte2Final);

print(StringFinal)