
letra1 = input("Ingresar una letra: ")
letra2 = input("Ingresar otra letra: ")


while(len(letra1) == 1 and len(letra2) == 1):
    if(letra1 == letra2):
        print("Las letras son iguales")
        letra1 = input("Ingresar una letra: ")
        letra2 = input("Ingresar otra letra: ")
    else:
        print("Las letras no son iguales")
        letra1 = input("Ingresar una letra: ")
        letra2 = input("Ingresar otra letra: ")


print("solo debe ingresar un solo caracter")