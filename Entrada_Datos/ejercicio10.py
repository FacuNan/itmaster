persona1 = int(input("Ingrese su inversion: "))
persona2 = int(input("Ingrese su inversion: "))
persona3 = int(input("Ingrese su inversion "))

total_inversion = persona1 + persona2 + persona3

promedio1 = round((persona1 / total_inversion) * 100, 2)
promedio2 = round((persona2 / total_inversion) * 100, 2)
promedio3 = round((persona3 / total_inversion) * 100, 2)


print(f"""El promedio de inversion de la primer persona es: ==> {promedio1}%
El promedio de inversion de la segunda persona es: ==> {promedio2}%
El promedio de inversion de la tercer persona es: ==> {promedio3}%""")