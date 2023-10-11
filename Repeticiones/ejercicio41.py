numero_entero = int(input("Ingrese un numero entero: "))
lista = []
maximo = 0

while numero_entero != 0:
    lista.append(numero_entero) 
    numero_entero = int(input("Ingrese un numero entero: "))
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
   

print(maximo)              