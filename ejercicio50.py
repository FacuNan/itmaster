nota = int(input("Ingrese su nota: "))

while nota not in range(1,11):
    print("Por favor ingrese una nota del 1 al 10")
    nota = int(input("Ingrese su nota: "))

if(nota >= 7):
    print("Usted esta aprobado")
else:
    print("Usted esta desaprobado")
    
