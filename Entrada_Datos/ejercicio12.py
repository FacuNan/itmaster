angulo_derecho = int(input("Ingrese el valor del angulo inferior derecho: "))
angulo_izquierdo = int(input("Ingrese el valor del angulo inferior izquierdo: "))


angulo_superior = 180 - (angulo_derecho + angulo_izquierdo)


print(f"El valor del angulo superiro es de {angulo_superior}")