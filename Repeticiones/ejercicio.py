altura = float(input("Ingresar la altura: "))

jugadores = []
contador = 0
suma = 0

while altura != 0:
    jugadores.append(altura)
    altura = float(input("Ingrese la altura: "))

for i in range(len(jugadores)):
    contador += 1
    suma += jugadores[i]

promedio = suma / contador

print(f"El promedio de altura de cada jugador es de: {promedio}")


    