
primer_parcial = int(input("La nota del primer parcial: "))
segundo_parcial = int(input("Ingrese la nota del segundo parcial: "))

while primer_parcial not in range(1, 11) or segundo_parcial not in range(1,11):
    print("Las notas deben ser del 1 al 10")
    primer_parcial = int(input("La nota del primer parcial: "))
    segundo_parcial = int(input("Ingrese la nota del segundo parcial: "))

nota_final = (primer_parcial + segundo_parcial) / 2

if nota_final >= 7:
    print(f"Usted esta aprobado su nota final es: {nota_final}")
else:
    print(f"Usted esta desaprobado su nota final es: {nota_final}")