"""
Ejercicio 065
Una cadena de comida rápida solicita el desarrollo de una aplicación para sus terminales de autoservicio que permita a los clientes armar su propio menú. 
Los clientes pueden elegir entre diferentes opciones de combos o pedir por separado la comida, bebida y postre.

Al iniciar la aplicación, se debe mostrar el siguiente menú de opciones:

1) Combo 1: Hamburguesa, papas fritas y gaseosa - $1550
2) Combo 2: Hamburguesa con queso, papas fritas y gaseosa - 1650
3) Hamburguesa sola - 1300
4) Hamburguesa con queso - 1400
5) Gaseosa - 700
6) Postre - 600
7) Agregar aderezo - 100
8) Terminar
Luego de seleccionar cada ítem, se debe mostrar el subtotal para que el cliente pueda decidir si desea agregar más productos a su pedido antes de terminar.

El valor mínimo del pedido debe ser de $1550. Si el cliente elige un combo, se debe sumar el importe total al subtotal. Si el cliente selecciona opciones 3 a 7, se le debe preguntar la cantidad deseada y calcular el valor total antes de sumarlo al subtotal.
Al finalizar el pedido, se debe mostrar el monto total a pagar, el ítem más caro y, si no se han seleccionado productos, mostrar un mensaje que diga 
"Pedido cancelado".
"""

import sys
sys.path.insert(0,'recursos/')
import funciones as fun 
from os import system

PRECIOS = (0.0,2300.25,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,)
#index            1

TUPLA_OPCIONES = (
"Comidas Cachito",   
"Combo 1: Hamburguesa, papas fritas y gaseosa",
"Combo 2: Hamburguesa con queso, papas fritas y gaseosa",
"Hamburguesa sola - 1300",
"Hamburguesa con queso - 1400",
"Gaseosa - 700",
"Postre - 600",
"Agregar aderezo - 100",
"Terminar"
 )


def proc_un_pedido(opcion:str,subtotal:float)->list:
    
    system('cls')
    print(f"Importe: {subtotal:8.2f}")
    cantidad = fun.leer_entero(f"{TUPLA_OPCIONES[opcion]} Cantidad: ")
    importe = cantidad * PRECIOS[opcion]
    return [f"{TUPLA_OPCIONES[opcion]} {cantidad} {importe}",cantidad,importe]

def imprimir_pedido(lista_pedido):
    system('cls')
    system('pause') # input("Presione una tecla para continuar...")
    

def main():    
    terminar_programa = False
    while not terminar_programa:
        terminar_pedido = False
        lista_pedido = []
        subtotal = float(0)
        while not terminar_pedido:
            opcion = fun.menu(TUPLA_OPCIONES)
            if opcion != 8:
                renglon = proc_un_pedido(opcion,subtotal)
                subtotal += renglon[2]
                lista_pedido.append(renglon)
            else:
                if len(lista_pedido) > 0:
                    imprimir_pedido(lista_pedido)    
                terminar_pedido = True
        terminar_programa = input("Continua [S/N]: ").upper() == 'N'
main()