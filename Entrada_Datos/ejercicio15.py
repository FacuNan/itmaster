nombre = input("Ingrese su nombre: ")
cantidad_ventas = int(input("Ingrese la cantidad de ventas realizadas: "))
valor_ventas = float(input("Ingrese el valor de cada venta: "))
valor_total = valor_ventas * cantidad_ventas

salario_base = 200000
comision_fija = 15000

porcentaje_comision = round(float(valor_total * 5)/100, 2)


salario_mensual = salario_base + comision_fija + porcentaje_comision

print(f"Señor/a {nombre} su salario mensual es de: {salario_mensual}")