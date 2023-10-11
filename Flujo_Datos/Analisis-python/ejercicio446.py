numero = int(input("Ingrese un numero: "))

def lista_numero(numero):
    lista_numeros = []
    while(numero != 0):
        lista_numeros.append(numero)
        numero = int(input("Ingrese un numero, y cero para terminar: "))
    return lista_numeros    
     
            

def min_max(lista):
    minimo= lista[0]
    maximo= lista[0]
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
        elif lista[i] < minimo:
            minimo = lista[i]
    return f"El maximo es {maximo} y el minimo es {minimo}"

lista = lista_numero(numero)
print(min_max(lista))