a = int(input("Ingrese el numero a dividir: "))
b= int(input("Ingrese el numero por el cualquiere dividirlo: "))


if(a <= b):
    print("Lo siento no pued erealizarse la division")
else:
    if(a % b ==0):
        print("El numero es divisible")
    else:
        print("Los numero no son divisibles")