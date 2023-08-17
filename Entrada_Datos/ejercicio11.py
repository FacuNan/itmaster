nombre1 = input("Ingrese su nombre: ")
capital1 = int(input("ingrese su capital aportado: "))
nombre2= input("Ingrese su nombre: ")
capital2=int(input("Ingrese el capital aportado: "))

suma_capital  = capital1 + capital2

promedio1 = round((capital1 / suma_capital)* 100, 2)
promedio2 = round((capital2 / suma_capital)* 100, 2)

print(f"""Señor/a {nombre1} su promedio de capital aportado es {promedio1} 
Señor/a su promedio de capital aportado es {promedio2}""")