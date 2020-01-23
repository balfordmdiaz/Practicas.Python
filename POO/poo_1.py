class Carro():

    def __init__(self):     #Metodo Constructor

        #Forman parte del estado inicial
        #OBJETOS:
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4       #Encapsulando la variable ---que no es accesible fuera de la clase
        self.__enmarcha = False


    def __chequeo_interno(self):
        print("Realizando Chequeo Interno")

        self.gasolina = "Ok"
        self.aceite = "Ok"
        self.puertas = "Cerradas"

        if(self.gasolina == "Ok" and self.aceite == "Ok" and self.puertas == "Cerradas"):
            return True
        
        else:
            return False

    #METODO
    def arrancar(self, arrancamos):
        
#        pass#Hace que pase ya que no tiene parametros el metodo
        self.__enmarcha = arrancamos

        if (self.__enmarcha):   #Si _enmarcha es = TRUE ... hara lo siguiente   
            chequeo = self.__chequeo_interno()  #Se crea esta variable para que sea accesible al metodo 
        
        if(self.__enmarcha and chequeo):
            return "El carro esta en marcha"
        
        if(self.__enmarcha and chequeo == False):
            return "Algo ha ido mal con el chequeo. No podemos arrancar"

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

