a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

suma_pares = 0
suma_impares =0
producto_pares = 1
producto_impares = 1

for i in range(a, b, 1):
   if( i % 2 == 0):
      suma_pares += i
      producto_pares *= i
   else:
      suma_impares += i
      producto_impares *= i
print(f"La suma de los pares de {a} y {b} es {suma_pares}")
print(f"La suma de los impares de {a} y {b} es {suma_impares}")
print(f"El producto de los pares de {a} y {b} es {producto_pares}")
print(f"El producto de los impares de {a} y {b} es {producto_impares}")