ancho = float(input("Ingrese el ancho de su terreno: "))
largo = float(input("Ingrese el largo de su terreno: "))
valor_metro_cuadrado = float(input("Ingrese el valor del metro cuadrado: "))

metro_cuadrado_terreno = round(float(ancho * largo),2)

precio_terreno = round(float(valor_metro_cuadrado * metro_cuadrado_terreno), 2)

#Calcular la cantidad de alambre a autilizar

perimetro =round((ancho*2) + (largo *2),2)

un_metro = round((perimetro * 1), 2)

dos_metros = round((perimetro * 2), 2)

tres_metros =round((perimetro * 3), 2)


print(f"El valor del terreno es: {precio_terreno}")
print(f"""La cantidad de alambre necesario para cubrir el terreno a la altura de un metro es de: {un_metro}
La cantidad de alambre necesario para dos metros es de: {dos_metros}
La cantidad de alambre necesario para tres metros es de: {tres_metros} """)


                       
