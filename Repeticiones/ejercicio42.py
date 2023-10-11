numero = int(input("Ingrese un numero entero: "))
lista =[]
cantidad = len(lista)
suma = 0
promedio = 0


while numero != 0:
    lista.append(numero)
    for i in range(len(lista)):
        suma += lista[i]
        numero = int(input("Ingrese un numero entero: "))
        promedio += suma / cantidad
print(promedio)
    

