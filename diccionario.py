estudiante={
    
    'nombre':'james',
    'edad':30,
    'posicion':'delantero',
    'convocado':True
}
#acceder a todas las llaves de mi diccionario
#print(estudiante)
#necesito acceder a un atributo o llave de mi diccionario
#print(estudiante['nombre'])

for llave,valor in estudiante.items():
    print(llave,valor)

for valor in estudiante.values():
    print(valor)