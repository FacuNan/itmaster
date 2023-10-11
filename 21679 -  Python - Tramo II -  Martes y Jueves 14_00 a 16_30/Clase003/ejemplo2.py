"""
Dados tres numeros mostrar:

maximo
medio
minimo
reminimo
"""

n1 = 14
n2 = 14
n3 = -11
n4 = 8

maximo = n1
medio = n2
minimo = n3

if n2 > maximo:
    maximo = n2
    medio = n1
    minimo = n3

if n3 > maximo:
    maximo = n3
    medio = n1
    minimo = n2

if medio < minimo:
    medio,minimo = minimo,medio

print(maximo,medio,minimo)