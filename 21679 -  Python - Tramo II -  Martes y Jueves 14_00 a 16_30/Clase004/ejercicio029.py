"""
Ejercicio 029
Escribir un programa que permita Ingresar las notas de los dos parciales de un 
alumno e indicar si promocionó, aprobó o debe recuperar. 

Si el valor de la nota no esta entre 0 y 10, debe informar un error.

Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
Se debe recuperar cuando al menos una de las dos notas es menor a 4.

P	Q	(P or Q)
V	V	    V
V	F	    V
F	V	    V
F	F	    F

"""

nota1 = 7
nota2 = 2

datos_ok = nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10
   