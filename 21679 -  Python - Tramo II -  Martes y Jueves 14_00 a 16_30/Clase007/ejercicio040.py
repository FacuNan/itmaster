"""
Ejercicio 040
Escribir un programa que permita ingresar dos numeros 
enteros a y b. 

El programa debe mostrar:
La suma de los numeros pares entre a y b.
El producto de los numeros impares entre a y b.

"""

a = int(input('Ingrese el primer número: '))
b = int(input('Ingrese el segundo número: '))
numeros_sumados = ''
numeros_multiplicados = ''
suma = 0
producto = 1
for i in range (a,b+1):
    if i % 2 == 0:
        suma += i
        numeros_sumados += f"{i} "
    else:
        numeros_multiplicados += f"{i} "
        producto *= i
print(f'Suma ==> {suma} [{numeros_sumados}]')
print(f'Producto ==> {producto} [{numeros_multiplicados}]')