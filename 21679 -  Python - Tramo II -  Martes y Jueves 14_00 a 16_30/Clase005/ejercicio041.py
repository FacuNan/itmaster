"""
Ejercicio 041

Escribir un programa que lea números enteros hasta que se 
ingrese un 0, y muestre el máximo.
"""
# ANTES (PARA TODOS)
maximo = float('-inf')
minimo = float('inf')
numero = int(input("numero: "))
hay_datos = False
while numero != 0:
    # DURANTE (PARA CADA DATO)
    hay_datos = True
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero
    
    # LO ULTIMO ES LEER UN NUEVO DATO
    numero = int(input("numero: "))
# DESPUES (TOTALES)
if hay_datos:
    print(f"maximo: {maximo}")
    print(f"minimo: {minimo}")
else:
    print("No se ing. numeros")


