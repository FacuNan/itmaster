"""
2. Realizá un programa que permita ingresar 3 notas pertenecientes a tres trimestres distintos
para cierto alumno de nivel secundario. 
Debe calcularse y mostrarse la nota promedio. 



"""

n1 =  int(input("Nota 1: "))  
n2 =  int(input("Nota 2: "))  
n3 =  int(input("Nota 3: "))  

prom = (n1 + n2 + n3) / 3

print("Notas: ",n1,n2,n3,"Promedio:",prom)
cadena_formato = f"Notas:{n1:03}{n2:03}{n3:03} ==> Promedio:{prom:8.02}"
print(cadena_formato)

