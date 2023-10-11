kilometros = float(input("Ingrese la cantidad de kilometros a recorrer: "))

VIAJE_MINIMO = 50

valor_viaje = 0

if(kilometros >= 0 and kilometros <=10):
    valor_viaje += VIAJE_MINIMO + (kilometros * 15)
else:
    valor_viaje += VIAJE_MINIMO + (kilometros * 20)


print(f"El costo del viaje es: ${valor_viaje}")




