while True:
    entrada = input().split()
    digitoComFalha = str(entrada[0])
    numeroNegociado = str(entrada[1])
    
    if (digitoComFalha == "0" and numeroNegociado == "0"):
        break;
        
    final = '';
    numeroNegociadoLista = list(numeroNegociado);
    
    for i in numeroNegociado:
        if (digitoComFalha != i):
            final += (str(i));
            
    if (final == ''):
        print (0)
    else:
        print (int(final))