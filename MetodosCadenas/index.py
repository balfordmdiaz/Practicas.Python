'''
upper = metodo para hacer mayuscula todas las letras de un string

lower = pasa a mayuscula los string

capitalize = pone la primera letra de un string en mayuscula

count = contar las veces que aparecen una letra o una cadena en un string

find = representa la posicion en la que aparece un caracter o un grupo de caracteres

isdigit = devuelve un boolean donde dice si es un digito o no

isalpha =  comprueba si hay solo letras (especios no cuentan)

split = separa por palabras utilzando espacios

strip = borra los espacios sobrantes del inicio y final

replace = cambia una letra o palabra por otra

rfind = representa el indice de una letra, contando desde el principio del string

'''

edad = input("Introduce la edad: ")

while(edad.isdigit()==False):       ###Metodo excepcion

    print("Por favor, introduce un valor numerico")

    edad = input("Introduce la edad: ")

if (int(edad)<18):

    print("No puede pasar")

else:

    print("Puedes pasar")



