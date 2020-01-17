class Carro():

    def __init__(self):     #Metodo Constructor

        #Forman parte del estado inicial
        #OBJETOS:
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4       #Encapsulando la variable ---que no es accesible fuera de la clase
        self.enmarcha = False

    #METODO
    def arrancar(self, arrancamos):
        
#        pass#Hace que pase ya que no tiene parametros el metodo
        self.enmarcha = arrancamos

        if(self.enmarcha):
            return "El carro esta en marcha"
        
        else:
            return "El carro esta detenido"

    def estado(self):
        print("El carro tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)


miCarro = Carro() ####Instanciando una clase

print(miCarro.arrancar(True))
miCarro.estado()



print("-----------------------A continuacion el segundo objeto----------------------")

miCarro2 = Carro()

print(miCarro2.arrancar(False))
miCarro2.estado()

