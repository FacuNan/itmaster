nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura: "))

if(edad >= 10 and altura > 1.60):
    print(f"{nombre}, Bienvenido/a al parque diversiones")
else:
    if(edad < 10 and altura > 1.60):
        print("Usted no puede ingresar porque es menor de edad")
    elif(altura <= 1.60 and edad > 10):
        print("Usted no puede ingresar por su corta estatura")
    else:
        print("Usted es menor de edad y no tiene la altura mayor de 1.60")