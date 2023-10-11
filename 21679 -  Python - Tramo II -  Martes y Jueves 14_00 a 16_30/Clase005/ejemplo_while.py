"""
Leer numeros hasta que se ingrese un cero. Mostrar la suma

lista1 ==> 1,2,4,4,7,8,5,2,1,4,5,6,9,8,7,4,5,7,1,0
lista2 ==> 1,2,4,4,7,8,5,7,4,5,7,1,0
lista3 ==> 1,2,0
lista4 ==> 0
"""
# ANTES
suma = 0
numero = int(input("Ing. un numero: "))
while  numero != 0 :
    # DURANTE
    suma += numero
    numero = int(input("Ing. un numero: "))
# DESPUES
print(f"La sema es: {suma}")




