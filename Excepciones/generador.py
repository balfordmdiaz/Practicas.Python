



####GENERADORES

#########FORMA1



#def generaPares(limite):###########se crea la funcion con una un atributo declarado el cual es limite

#    num = 1

#   miLista=[]

#    while num < limite:

#        miLista.append(num*2)

#        num = num + 1

#    return miLista

#print(generaPares(10))#########Aqui agregamos el limite el cual es 10









###########FORMA 2




#def generaPares_2(limite):

#    num = 1


#    while num < limite:

#       yield num * 2           #########LA FUNCION YIELD DEVUELVE LOS VALORES GUARDADOS EN EL DE UNO EN UNO
#       num = num + 1

#devuelvePares = generaPares_2(5)

#for i in devuelvePares:
#   print(i)





##################################FORMA 3



def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Roma")

print(next(ciudades_devueltas))##Metodo que devuelve el atributo de la lista
print(next(ciudades_devueltas))##Devuelve el siguiente atributo de la lista
