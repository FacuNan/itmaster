numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

if(numero1 > numero2):
    print(f"El numero {numero1} es el mayor")
elif(numero2 > numero1):
    print(f"El numero {numero2} es el mayor")
else:
    print("Los numero son iguales")