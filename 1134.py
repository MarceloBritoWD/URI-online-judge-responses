alcool = 0
gasolina = 0
diesel = 0
continua = True

while continua:
    valor = int(input())
    
    while valor < 1 or valor > 4:
        valor = int(input())
    
    if valor == 1:
        alcool = alcool + 1
        
    elif valor == 2:
        gasolina = gasolina + 1
    
    elif valor == 3:
        diesel = diesel + 1
    
    elif valor == 4:
        continua = False

print("MUITO OBRIGADO")
print("Alcool: " + str(alcool))
print("Gasolina: " + str(gasolina))
print("Diesel: " + str(diesel))