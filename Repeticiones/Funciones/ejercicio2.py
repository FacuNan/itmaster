def leer_enteros(cartel):
    datos_Ok =False
    while not datos_Ok:
        cadena = input(cartel)
        if cadena.isnumeric():
            numero = int(cadena)
            datos_OK =True
        else:
            print("El valor ingreasado no es un numero")


def es_entero(cadena):
     try:
         int(cadena)
     except:
        return False
     else: 
         return True

def es_float(cadena):
    try:
        float(cadena)
    except:
        return False
    else:
        return True
    
def es_numero(cadena):
    return es_entero(cadena) or es_float(cadena)

