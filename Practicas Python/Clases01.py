class Vuelo:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = []

    def getDisponibles (self):
        return self.capacidad - len (self.pasajeros)

    def addPasajero (self, nombre):
        if self.getDisponibles ():
            self.pasajeros.append(nombre)
            return True
        else:
            return False
            
vuelo = Vuelo (3)

print (vuelo.getDisponibles())
vuelo.addPasajero('Pau')
vuelo.addPasajero('Nacho')
vuelo.addPasajero('Raul')

print (vuelo.getDisponibles())       
