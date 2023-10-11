"""
Ejercicio 026
Escribir un programa que permita ingresar la cantidad de invitados 
a una fiesta y la cantidad de asientos disponibles en el salon. 
Debes indicar si alcanzan los asientos, 
Si los asientos no alcanzaran indicar cuántos faltan para que 
todos los invitados puedan sentarse.
"""

cantidad_invitados = int(input("Cant. de inv.:"))
cantidad_asientos =  int(input("Cant. de asi.:"))

hay_lugar = cantidad_asientos <= cantidad_invitados

if hay_lugar:
    print("todo ok")
else:
    dif =  cantidad_invitados - cantidad_asientos  
    print(f"Faltan {dif} asientos")

