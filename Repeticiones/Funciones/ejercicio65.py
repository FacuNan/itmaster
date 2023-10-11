import sys
sys.path.insert('Recursos/')

from Recursos import funciones




tupla_opciones = (
"Combo 1: Hamburguesa, papas fritas y gaseosa - $1550",

"Combo 2: Hamburguesa con queso, papas fritas y gaseosa - $1650",

"Hamburguesa sola - $1300",

"Hamburguesa con queso - $1400",

"Gaseosa - $700",

"Postre - $600",

"Agregar aderezo - $100",

"Terminar"

)



def main():
    terminar_programa = False

    while not terminar_programa:
        opcion = funciones.menu(tupla_opciones)



main()