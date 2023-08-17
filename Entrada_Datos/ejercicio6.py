primer_trimestre = int(input("Ingrese la nota: "))
segundo_trimestre = int(input("Ingrese la nota: "))
tercer_trimestre = int(input("Ingrese la nota: "))

suma = primer_trimestre + segundo_trimestre + tercer_trimestre

promedio = suma / 3 

print(f"""notas: {primer_trimestre}. {segundo_trimestre}, {tercer_trimestre},
promedio: {promedio}""")