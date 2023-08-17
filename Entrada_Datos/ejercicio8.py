valor_hora= int(input("Ingrese el valor por hora: "))
horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))

salario_diario = valor_hora * horas_trabajadas

salario_semanal = salario_diario * 5

horas_sabado =  horas_trabajadas / 2

salario_sabado = horas_sabado * valor_hora

salario_final = salario_semanal + salario_sabado

print(f"Al trabajador le corresponde un salario semanal de : {round(salario_final)}")