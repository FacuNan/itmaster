"""
Dados dos numeros mostrar el mayor
"""


n1 = 100
n2 = 20
n3 = 17

c1 = "ñsjkdsdñ"
c2 = "ñsdikcvo"


print(f"{n1}  {n2} ==> {max(n1,n2)}")
print(f"{c1}  {c2} ==> {max(c1,c1)}")

mayor = n1

if n2 > mayor:
    mayor = n2

if n3 > mayor:
    mayor = n3


print(f"Mayor: {mayor}")



