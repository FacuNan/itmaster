"""
Este Módulo implementa funciones de uso general.

- es_entero(str_numero) 
- es_flotante(str_numero) 
- es_entero_entre(str_numero) 
- es_flotante_entre(str_numero) 

"""

from os import system


def es_entero(str_numero:str)->bool:
    try:  # INTENTO        
        int(str_numero)
    except:  # SI HAY ERROR
        return False
    else:   # SI NO HAY ERROR
        return True


def es_flotante(str_numero:str)->bool:
    try:  # INTENTO
        float(str_numero)
    except:  # SI HAY ERROR
        return False
    else:   # SI NO HAY ERROR
        return True


def es_numero(str_numero:str)->bool:
    return es_entero(str_numero) or es_flotante(str_numero)


def leer_numero(cartel:str="Ingrese un numero: ")->int|float:    
    while True: 
        cadena = input(cartel)
        if es_entero(cadena):
            return int(cadena)
        elif es_flotante(cadena):            
            return float(cadena)
        else:
            print("Error: Tiene que ingresar un numero.")


def leer_entero(cartel:str="Ingrese un entero: ", 
                    desde:int=-999999999999999, 
                        hasta:int=999999999999999)->int:
    todo_ok = False
    while not todo_ok:  # mientras error
        cadena = input(cartel)
        if es_entero(cadena):
            numero = int(cadena)
            if desde <= numero <= hasta:  # if numero >= desde and numero <= hasta
                todo_ok = True
            else:
                print(
                    f"Error: El numero no esta en el rango: [{desde}..{hasta}].")
        else:
            print("Error: Tiene que ingresar un numero entero.")
    return numero


def leer_flotante(cartel:str = "Ingrese un Float: ", 
                    desde:float=-float('inf'), 
                        hasta:float=float('inf'))->float:
    todo_ok = False
    while not todo_ok:  # mientras error
        cadena = input(cartel)
        if es_flotante(cadena):
            numero = float(cadena)
            if desde <= numero <= hasta:  # if numero >= desde and numero <= hasta
                todo_ok = True
            else:
                print(
                    f"Error: El numero no esta en el rango: [{desde}..{hasta}].")
        else:
            print("Error: Tiene que ingresar un numero float.")
    return numero



def titulo(texto:str)->str:
    return f"{'-'*80}\n{texto.title().center(80)}\n{'-'*80}"

def menu(tupla_opciones:tuple[str])->int:    
    system('cls')
    for index,opcion in enumerate(tupla_opciones):
        if index == 0:
            print(titulo(opcion))
        else:
            print(f"{index} {opcion}")
    return leer_entero("Ingrese una opcion: ",1,index)

def test_funciones():    
    dia = leer_entero("Dia: ", 1, 31)
    x = leer_entero(desde=0,cartel_para_el_usuario="pepe")
    mes = leer_entero("Mes: ", 1, 12)
    print(leer_flotante("Importe: "))
    

if __name__ == '__main__':
    test_funciones()
