minimo_edad = float("inf")

nombre = input("Porfavor ingrese su nombre: ").title()

while nombre != '*':
    edad = int(input("ingrese su edad: "))

    if(edad < minimo_edad):
        minimo_edad = edad
        nombre_minimo = nombre
    
    nombre = input("Ingrese su nombre: ")

print(f"El nombre de la persona mas joven es: {nombre_minimo} y su edad es {minimo_edad}")

   



