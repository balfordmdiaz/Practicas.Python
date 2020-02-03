from io import open

'''
# w > write de archivo de modo escritura

archivo_texto = open("archivo.txt", "w")
#archivo que se abre en memoria

frase = "Buenos dias \nBalford" #


archivo_texto.write(frase) #incluye el contentido de la variable en el archivo creado (.txt)

archivo_texto.close() #cerrar el archivo creado en memoria'''


'''
#Archivo en modo lectura

archivo_texto = open("archivo.txt", "r")

texto = archivo_texto.read() #variable que almacena lo que se lee

archivo_texto.close()

print(texto) #Nos muestra la informacion almacena en el archivo externo'''


#Anadir datos al archivo por el metodo append

archivo_texto = open("archivo.txt", "a")

archivo_texto.write("\nMessi") ##Lo ejecute dos veces

archivo_texto.close()

