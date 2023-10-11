opcion = input("Continua [S/N]: ").upper()
nombre = input("Ingrese su nombre: ")

while opcion not in('S', 'N'):
    print(f"Lo siento la opcion {opcion} no es correcta")
    opcion = input("Continua[S/N]: ")

print(f"Muchas gracias por elegirnos {nombre.title()}")