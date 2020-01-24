class Persona():

    def __init__(self, nombre, edad, ciudad):

        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def descripcion(self):

        print("Nombre: ", self.nombre, " Edad: ", self.edad, "Ciudad: ", self.ciudad)


class Empleado(Persona):

    def __init__(self, salario, antiguedad, nom_empleado, ed_empleado, ciu_empleado):

        super().__init__(nom_empleado, ed_empleado, ciu_empleado)#Funcion super, llama al metodo de la clase padre y llama al metodo init

        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):

        super().descripcion()##llama al metodo descripcion de la clase padre

        print("Salario: ", self.salario, " Antiguedad: ", self.antiguedad)

pers1 = Empleado(10000, 2 ,"Balford", 22, "Managua")
pers1.descripcion() #Imprime los dos metodos llamados descripcion