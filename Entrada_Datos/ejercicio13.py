sueldo_fijo = 200.000
ventas_realizadas = int(input("Ingrese la cantidad de ventas realizadas: "))

porcentaje = round((ventas_realizadas * 16)/ 100, 2)

sueldo_final = sueldo_fijo + porcentaje

print(f"El sueldo que le corresponde es: {sueldo_final}")
