numero = int(input("Ingrese un numero: "))

def crear_lista(numero):
    lista = []
    while numero != 0:
         lista.append(numero)
         numero = int(input("Ingrese otro numero: "))
    return lista


def ordenar_lista(lista):
     for i in range(len(lista)):
          for j in range(len(lista) - i - 1):
                if lista[j] > lista[j + 1]:
                     lista[j], lista[j + 1] = lista[j + 1], lista[j]
     return lista
print(ordenar_lista(crear_lista(numero)))