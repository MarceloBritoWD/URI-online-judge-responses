def formatacaoMonetaria(dols, cents):
    final = []
    final.insert(0, "$")

    # laço que adiciona "." a cada tres casas
    cont = len(dols)
    while cont > 0:
        dols.insert(cont, ",")
        cont -= 3
    dols.pop()

    # adiciona 0 caso o len de cents for igual a 1
    if len(cents) == 1:
        cents.insert(0, "0")
    cents.insert(0,".")

    #transforma tudo em string e soma-as
    strDols = ''.join(dols)
    strCents = ''.join(cents)
    strFinal = ''.join(final)
    strFinal += strDols
    strFinal += strCents
    return strFinal

while True:
    try:
        dolares = list(input())
        centavos = list(input())
        print(formatacaoMonetaria(dolares, centavos))

    except:
        break;
