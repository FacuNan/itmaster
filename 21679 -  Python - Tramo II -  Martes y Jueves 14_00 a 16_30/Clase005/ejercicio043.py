"""
Ejercicio 043
Escribir un programa que lea números enteros hasta que se la 
suma de éstos sea mayor que 100, y muestre la cantidad de 
números ingresados.

random 0.0 ... 0.9999999999999

"""
import random

numero = random.randint(1,10)
contador = 0
suma = 0
while suma <= 100:
    contador += 1
    suma += numero
    print(f"Numero: {numero} Suma: {suma} Cantidad: {contador}")
    numero = random.randint(1,10)
print(f"Cantidad de numeros: {contador}")