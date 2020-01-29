



def dividir():       ##AGREGAR EXCEPCIONES CUANTAS VECES SEA NECESARIO EN UNA MISMA FUNCION
    try:
        val1 = float(input(("Introduce el primer valor: " )))
        val2 = float(input(("Introduce el segundo valor: " )))

        print("La division es: " + str(val1/val2))

    except ValueError:##Excepcion del valor introducido es erroneo
        print("El valor introducido es erroneo")
    
    except ZeroDivisionError:   #Excepcion que muestra que no se puede dividir entre 0
        print("No se puede dividir entre 0")
        
    finally:####Siempre se ejecuta  ###Sirve para BD a que cierre la cesion...
        print("Calculo Finalizado")

dividir()
