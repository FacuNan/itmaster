

def leer_entero_entre(cartel,desde,hasta):
    while True: 
        cadena = input(cartel)
        try:
            numero = int(cadena)
        except:
            print(f"Error: '{cadena}' No es un numero.")
        else:
            if desde <= numero <= hasta:
                return numero
            else:
                print(f"Error: '{numero}' esta fuera de rango [{desde}..{hasta}]")
        


def main():
    dia = leer_entero_entre("Dia: ",1,31)
    mes = leer_entero_entre("Mes: ",1,12)
    



main()