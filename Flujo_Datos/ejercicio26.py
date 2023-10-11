invitados = []
asientos = 10


def verificar_asientos():
    while(asientos >= len(invitados)):
         invitado = input("Ingrese el nombre del invitado ")
         invitados.append(invitado)
         
    print( "Lo siento no hay mas asientos disponibles")


verificar_asientos()



