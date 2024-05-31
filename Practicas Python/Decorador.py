#https://docs.python.org/3/library/typing.html#functions-and-decorators

def decora(f):
    def envuelve():
        print('Estoy a punto de ejecutar la funcion:')
        f()
        print('Termine de ejecutar la funcion')
    return envuelve

@decora
def hola():
    print('Hola mundo')

hola()
