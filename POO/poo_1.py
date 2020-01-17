class Carro():
    #OBJETOS:
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    #METODO
    def arrancar(self, arrancamos):
        
#        pass#Hace que pase ya que no tiene parametros el metodo
        self.enmarcha = arrancamos

        if(self.enmarcha):
            return "El carro esta en marcha"
        
        else:
            return "El carro esta detenido"

    def estado(self):
        print("El carro tiene ", self.ruedas, " ruedas. Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis)


miCarro = Carro() ####Instanciando una clase

print(miCarro.arrancar(True))
miCarro.estado()



print("-----------------------A continuacion el segundo objeto----------------------")

miCarro2 = Carro()

print(miCarro2.arrancar(False))
miCarro2.estado()

