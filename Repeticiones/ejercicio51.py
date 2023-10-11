numero = int(input("Ingrese un numero cualquiera y 0 para terminar: "))

numeros =[]
while(numero != 0 ):
    numeros.append(numero)
    numero= int(input("Ingrese otro numero y 0 para terminar: "))

maximo = numeros[0]
minimo = numeros[0]

for i in range(len(numeros)):
    if maximo < numeros[i]:
        maximo = numeros[i]
    elif minimo > numeros[i]:
        minimo = numeros[i]
print(f"El numero maximo es {maximo}, y el minimo es {minimo}")

