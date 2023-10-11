
def es_entero(cadena):
    try:
        int(cadena)        
    except: # SI EXISTE UN ERROR 
        return False
    return True # SI NO EXISTE UN ERROR 

def es_float(cadena):
    try:
        float(cadena)        
    except: # SI EXISTE UN ERROR 
        return False
    else: # SI NO EXISTE UN ERROR 
        return True

def es_numero(cadena):
    return es_entero(cadena) or es_float(cadena)


def leer_float(cartel):
    datos_ok = False
    while not datos_ok: # datos_ok == False:
        cadena = input(cartel)
        if es_float(cadena):
            numero = float(cadena)
            datos_ok = True
        else:
            print(f"Error: '{cadena}' No es un numero.")
    return numero


def leer_entero(cartel):   
    while True: 
        cadena = input(cartel)
        if es_entero(cadena):
            numero = int(cadena)
            return numero
        else:
            print(f"Error: '{cadena}' No es un numero.")
    


def leer_entero_entre(cartel,desde,hasta):
    while True: 
        cadena = input(cartel)
        if es_entero(cadena):
            numero = int(cadena)
            if desde <= numero <= hasta:
                return numero
            else:
                print(f"Error: '{numero}' esta fuera de rango [{desde}..{hasta}]")
        else:
            print(f"Error: '{cadena}' No es un numero.")




def main():
    dia = leer_entero_entre("Dia: ",1,31)
    mes = leer_entero("Mes:")
    cant_patas_perr = leer_entero("Cantidad de patas de su perro: ")



main()

