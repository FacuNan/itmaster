segundos = int(input("Ingrese tiempo en segundos: "))

dias = segundos // 86400
horas = (segundos % 86400) // 3600
minutos = (segundos % 3600) // 60
segundos_restantes  = segundos % 60

print(f"""Dias: {dias}
Horas: {horas}
Minutos: {minutos}
Segundos: {segundos_restantes}""")
