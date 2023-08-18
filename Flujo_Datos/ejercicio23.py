numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
numero3 = int(input("Ingrese otro numero: "))

numero_maximo = max(numero1, numero2, numero3)
numero_minimo = min(numero1, numero2, numero3)


def medio(num1, num2 , num3):
    if(num1 > num2 > num3 or num3 > num2 > num1):
        return num2
    elif(num1 > num3 > num2 or num2 > num3 > num1):
        return num3
    else:
        return num1
   

mediano = medio(numero1, numero2, numero3)

print(f"""El numero mayor es {numero_maximo}
El numero mediano es {mediano}
El numero menor es {numero_minimo}""")