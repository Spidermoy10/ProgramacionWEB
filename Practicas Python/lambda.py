libros = [
    {'Titulo':'El principito', 'Año':1943},
    {'Titulo':'El arte de la guerra', 'Año':1772},
    {'Titulo':'La ciudad de las vestias', 'Año':2002},
    {'Titulo':'El hobbit', 'Año':1984},
    {'Titulo':'La grieta', 'Año':2007},
]

#No podemos comparar objetos sin decir algo mas sobre ellos
#libros.sort(key ='Año')
#sort no sabe que biscar dentro del diccionario

def ftitulo(libro):
    return libro['Titulo'].upper()

def fanio(libro):
    return libro['Año']

print(libros)
print()

#print('Libros ordenados por año:')
#libros.sort(key=fanio)
#print(libros)


#print('Libros ordenados por titulo:')
#libros.sort(key=ftitulo)
#print(libros)

libros.sort(key=lambda libro:libro['Año'])
for libro in libros:
    print(f"El libro {libro['Titulo']} fue publicado en {libro['Año']}")
    #print('El libro {Titulo} fue publicado en {Año}'.format(**libro))
#print(libros)

libros.sort(key=lambda libro:libro['Año'])
#print(libros)