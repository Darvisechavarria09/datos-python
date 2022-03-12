listaNumeros=[]

longitud=int(input("ingrese el tamaño de la lista: "))
for i in range(longitud):
    numeroIngresado=int(input("ingrese un numero: "))
    listaNumeros.append(numeroIngresado)

buscarNumero=int(input("que numero buscas?: "))
if(buscarNumero in listaNumeros):
    print(f"el numero {buscarNumero}, si está")
else:
    print(f"el numero {buscarNumero}, no está")
