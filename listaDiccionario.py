estudiantes=[

    {'nombre':'james','edad':34,'posicion':'delantero','convocado':True},
    {'nombre':'cuadra','edad':30,'posicion':'delantero','convocado':True},
    {'nombre':'lucho','edad':22,'posicion':'delantero','convocado':True},
    {'nombre':'falcao','edad':26,'posicion':'delantero','convocado':True}

]

for i in estudiantes:
    i.setdefault('paisa', True)
    print(estudiantes)