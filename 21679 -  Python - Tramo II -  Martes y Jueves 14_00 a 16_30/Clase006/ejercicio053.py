"""
Ejercicio 053
Escribir un programa que permita ingresar nombre y edad de un grupo de personas (para cada una, nombre y edad). La carga termina cuando en el nombre de la persona se ingresa un asterisco ('*'). Mostrar al final cómo se llama la persona más joven.
"""


minima_edad = float("inf")
nombre = input("Nombre: ").title()
while nombre != "*":
    edad = int(input('Edad: '))

    if edad < minima_edad:
        minima_edad = edad
        minimo_nombre = nombre


    nombre = input("Nombre: ").title()

print(f"El menor es: {minimo_nombre}")