"""
generar 10000 numeros y mostrar el mayor y cuantas repet. tiene

1,4,5,1,7,5,1,7,1,7,1,3,5,5

"""

from random import randint

CANTIDAD = 20
maximo = -float('inf')
cantidad_maximos  = 0
los_numeros = "Numero: "
for x in range(CANTIDAD):
    numero = randint(1,10)
    los_numeros += f'{numero} ' 
    if numero > maximo:
        maximo = numero
        cantidad_maximos = 0
    elif numero == maximo:
        cantidad_maximos += 1
print(los_numeros)
print(f"Maximo: {maximo} Rep: {cantidad_maximos}")

