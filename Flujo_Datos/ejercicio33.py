monto = float(input("Ingrese el monto: "))

while(monto > 0):
    if(monto < 5500):
        descuento = (monto * 4.5)/100
        precio_total = monto - descuento
        print(f"El monto total a pagar es: {precio_total}")
        monto = float(input("Ingrese el monto: "))
    elif monto >= 5500 and monto < 10000:
        descuento = (monto * 8)/100
        precio_total = monto - descuento
        print(f"El monto total a pagares: {precio_total}")
        monto = float(input("Ingrese el monto: "))
    else:
        descuento= (monto * 10.5)/100 
        precio_total = monto - descuento
        print(f"El monto total a paga r es de : {precio_total}")
        monto = float(input("Ingrese el monto: "))
print("El monto ingresado no es valido")





    