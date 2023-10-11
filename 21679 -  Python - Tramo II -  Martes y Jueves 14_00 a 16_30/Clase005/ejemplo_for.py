"""
Leer 10 numeros y mostrar la suma.

"""
# ANTES
suma = 0
cantidad = 10
for contador in range(1,cantidad+1):
    # DURANTE
    numero = int(input(f"Ingrese el {contador} de {cantidad} Numero: "))
    suma += numero
# DESPUES    
print(f"La suma es: {suma}")

palabra = "pepepepepe"

for letra in palabra:
    print(letra)

cantidad_letras = len(palabra)
for x in range(cantidad_letras):
    print(palabra[x]) 

