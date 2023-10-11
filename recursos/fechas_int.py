#% retorna los ultimos dos digitos del formato de la fecha
def el_dia(aaaammdd):
    return aaaammdd %100

def el_mes(aaaammaa):
    return (aaaammaa //100)%100

def el_anio(aaaammdd):
    return aaaammdd //10000

def str_es_fecha(aaaammdd):
    return f"{el_dia(aaaammdd):02}/{el_mes(aaaammdd):02}/{el_anio(aaaammdd)}"


def es_bisiesto(anio):
    return anio % 4 == 0

def dia_del_mes(mes, anio):
    dias = (0, 31, 28, 31,30,31, 30,31,31, 30,31,30,31)

    if mes == 2 and es_bisiesto(anio):
        
        return 29
    
    return dias[mes]




#Verifica la validez de las fechas

def fecha_valida(aaaammdd):
    anio = el_anio(aaaammdd)
    if anio < 1:
        return False
    
    mes = el_mes(aaaammdd)
    if mes < 1 or mes > 12:
        return False
    
    dia = el_dia(aaaammdd)
    if dia < 1 or dia > dia_del_mes(mes, anio):
        return False
    
    return True
    

def test():
    fecha =19631313
    if fecha_valida(fecha):
        return str_es_fecha(fecha)
    else:
        print("La fecha no es valida")


if __name__ == '__main__':
    test()

    


