"""
Ejercicio 049
Escribir un programa que permita validar una opción ingresada. Se le preguntará al usuario si desea continuar con alguna operación de la forma 
"¿Deseás continuar? [S/N]". Se espera que el usuario ingrese una 'S' o una 'N' (incluir las minúsculas). La opción debe ser ingresada tanto como sea necesario hasta que quede comprendida dentro de las posibilidades esperadas.
"""

opcion = input("Continua? [S/N] :").upper()
while opcion not in ('S','N'):
    print(f"{opcion} No es valida!")
    opcion = input("Continua? [S/N] :").upper()
print(f"Opcion: {opcion}")

print(    input("Nombre: ").title()   )

cadena = 'Escribir un programa que permita validar una opción ingresada'
print(cadena.title())
print(cadena.upper())
print(cadena.lower())
print(cadena.capitalize())
print(len(cadena))



