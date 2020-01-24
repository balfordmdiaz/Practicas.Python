class Vehiculo():

    def __init__(self, marca, modelo):#Constructor

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):

        self.enmarcha = True

    def acelerar(self):

        self.acelera = True

    def frenar(self):

        self.frena = True

    def estado(self):

        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nacelera: ", self.acelera, "\nFrena: ", self.frena)


class Moto(Vehiculo): #Hereda de la SuperClase Vehiculos

    hcaballito = ""

    def caballito(self):

        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):

        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nacelera: ", self.acelera, "\nFrena: ", self.frena, "\n", self.hcaballito)    
            #Se sobre escribe este metodo ya que estamos llamando a la clase hijo


class Furgoneta(Vehiculo):

    def cargar(self, cargar):

        self.cargado = cargar

        if(self.cargado):#Es igual a True

            return "La furgoneta esta cargada"

        else:

            return "La furgoneta no esta cargada"
        


miMoto = Moto("Genesis", "RKS")

miMoto.estado()
miMoto.caballito()

miFurgoneta = Furgoneta("Kia", "Picanto")

miFurgoneta.estado()
miFurgoneta.arrancar()
print(miFurgoneta.cargar(True))



class VElectricos():

    def __init__(self):

        self.autonomia = 100

    def cargareEnergia(self):

        self.cargando = True



class BiciElectrica(Vehiculo, VElectricos):#Toma como prioridad los valores del constructor de la primera clase mencionada
    pass


miBici = BiciElectrica("HZ", "BMX") 


