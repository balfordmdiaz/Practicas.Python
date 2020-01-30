def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    try:
        return n1 / n2
    
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operacion Incorrecta"

def potencia(n1, n2):

    if n2 == 2:

        print("El resultado de ", n1, " al cuadrado es: ", n1**n2)

    elif n2 == 3:

        print("El resultado de ", n1, " al cubo es: ", n1**n2)

    else:

        print("El resultado de ", n1, " a la ", n2, " es: ", n1**n2)


def redondear(n):

    print ("El resultado de ", n, " redondeado es: ", round(n))

    