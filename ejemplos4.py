numeros=[]

longitud=int(input("ingrese la cantidad de numeros a ingresar: "))
for i in range(longitud):
    numero=int(input("ingrese valores: "))
    numeros.append(numero)

buscar=int(input("ingrese el numero a buscar: "))
loTengo=False
for numero in numeros:
    if(buscar==numero):
        loTengo=True
        break
    else:
        loTengo=False

if(loTengo==True):
    print("si lo encontre")
else:
    print("no lo encontre")