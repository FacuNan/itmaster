"""
Realizá un programa que permita ingresar valores del mismo tipo para las variables num1 y
num2. Una vez cargadas, mostrar ambas variables por pantalla, intercambiá sus valores (que
lo cargado en num1 quede en num2, y viceversa) y volvé a mostrarlas actualizadas.

leer dos numeros
mostrar los numeros
intercambio
mostrar los numeros
"""

n1 =  int(input("Num1: "))  
n2 =  int(input("Num2: "))  

print(f"{n1:3} <------> {n2:3}")
auxiliar = n1
n1 = n2
n2 = auxiliar
print(f"{n1:3} <------> {n2:3}")

n1,n2 = n2,n1 # solo python!!!

print(f"{n1:3} <------> {n2:3}")


a = 1,2,3,4,5
print(a)






