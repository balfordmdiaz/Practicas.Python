class Carro():
    #OBJETOS:
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    #METODO
    def arrancar(self):
        
#        pass#Hace que pase ya que no tiene parametros el metodo
        self.enmarcha = True
    
    def estado(self):
        if(self.enmarcha):
            return "El carro esta en marcha"
        
        else:
            return "El carro esta detenido" #Si no se llama al metido arrancar devolvera esto EJ: linea 28


miCarro = Carro() ####Instanciando una clase

print("El largo del coche es: ", miCarro.largoChasis)

print("El carro tiene ", miCarro.ruedas, " ruedas")

miCarro.arrancar()

print(miCarro.estado())



print("-----------------------A continuacion el segundo objeto----------------------")

miCarro2 = Carro()
print("El largo del coche es: ", miCarro.largoChasis)
print("El carro tiene ", miCarro2.ruedas, " ruedas")
print(miCarro2.estado())

