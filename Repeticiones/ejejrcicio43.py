suma = []
numero = int(input("Ingrese un nuemero: "))

while not sum(suma) > 100:
    if sum(suma) == 100:
        contador = len(suma)
        print(contador)
     
    else:
        suma.append(numero)
        numero = int(input("Ingrese otro numero: "))
sumador = sum(suma)
print(f"El valor ha excedido los 100 {sumador}")



