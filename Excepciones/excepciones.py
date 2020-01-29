

def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):       ####A continuacion se escribe la excepcion de la division
    try:
        return n1 / n2
    
    except ZeroDivisionError:   #Excepcion que muestra que no se puede dividir entre 0
        print("No se puede dividir entre 0")
        return "Operacion Incorrecta"


"""while True:     #Bucle infinito. el cual mientras no se cumpla la excepcion no saldra del bucle
    try:
        val1 = int(input(("Introduce el primer valor: " )))
        val2 = int(input(("Introduce el segundo valor: " )))

        break
    
    except ValueError: #Excepcion que no se ingresan los valos o tipo de datos requeridos
        print("Los Valores Introducidos no son correctos. Intentalo Nuevamente")"""



################################SEGUNDO FORMA##########################
#######POR SI SE INGRESA ERRONEAMENTE ALGUNO DE LOS DOS VALORES REQUERIDOS
#######NO TENGA QUE VOLVER AL PRIMER VALOR PARA VOLVER INGRESAR EL DATO
while True:
    try:
        val1 = (int(input("Introduce el primer valor: " )))
        break
        
    except ValueError: #Excepcion que no se ingresan los valos o tipo de datos requeridos
        print("El primer valor es incorrecto. Intentalo Nuevamente")

while True:
    try:
        val2 = (int(input("Introduce el segundo valor: " )))
        break
        
    except ValueError: #Excepcion que no se ingresan los valos o tipo de datos requeridos
        print("El segundo valor es incorrecto. Intentalo Nuevamente")


####CODIGO A MEJORAR
"""print("Operaciones; Sumar    |   Restar   |   Multiplicar  |   Dividir")

while True:
    try:
        op = str(input("Ingresa la operacion a utilizar: "))
        break

    except ValueError:
        print("Has escrito mal la operacion. Intentelo Nuevamente")

op_=op.lower()#######funcion que permite que no importa como se escribe el dato lo haga pasar"""

print("Operaciones; Sumar    |   Restar   |   Multiplicar  |   Dividir")
op = input("Ingresa la operacion a utilizar: ")
op_=op.lower()#######funcion que permite que no importa como se escribe el dato lo haga pasar

if op_ == "sumar":
    print(suma(val1, val2))

elif op_ == "restar":
    print(resta(val1, val2))

elif op_ == "multiplicar":
    print(multiplicar(val1, val2))

elif op_ == "dividir":
    print(dividir(val1, val2))

else:
    print("No existe la operacion")

print("Operacion Ejecutada. Siga la ejecucion del Programa")



