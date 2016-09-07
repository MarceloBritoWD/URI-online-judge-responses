entrada = input().split()
precoAntigo = float(entrada[0])
precoNovo = float(entrada[1])
res = precoNovo - precoAntigo

resultado = (res/precoAntigo)*100

print("%.2f" %resultado + "%")
