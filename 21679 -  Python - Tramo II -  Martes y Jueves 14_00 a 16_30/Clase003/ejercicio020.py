enunciado = """
Ejercicio 020

Escribir un programa que permita ingresar dos cadenas de caracteres e 
indicar si son iguales o distintas.
"""

cad1 = "ab"
cad2 = 'aa'

print('-'*80)
print(f"{cad1} == {cad2} ==> {cad1==cad2}")
print(f"{cad1} > {cad2} ==> {cad1>cad2}")
print(f"{cad1} < {cad2} ==> {cad1<cad2}")
print(cad1*10+cad2*10)
print('~.~'*10) # esto es un comentario de linea

# esto es un comentario de linea
# jkkjsaJas
# lakjlkjasdjk

if cad1 == cad2:
    print("iguales")
else:
    print("distintas")


