class Coche():

    def desplazamiento(self):

        print("Me desplazo en 4 ruedas")

class Moto():

    def desplazamiento(self):

        print("Me desplazo en 2 ruedas")

class Camion():

    def desplazamiento(self):

        print("Me desplazo en 6 ruedas")


'''miVehiculo = Coche()
miVehiculo.desplazamiento()

miVehiculo2 = Moto()
miVehiculo2.desplazamiento()

miVehiculo3 = Camion()
miVehiculo3.desplazamiento()'''


#POLIMORISMO

def desplazamientoVehiculo(Vehiculo):

    Vehiculo.desplazamiento()


miVehiculo = Camion()#inicializamos la variable con una de las clases
desplazamientoVehiculo(miVehiculo)#mandamos a llamar la funcion perteneciente de la clase a traves de la nueva funcion





