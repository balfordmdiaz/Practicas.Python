#EJERCICIO DE INGRESAR UN CORREO CORRECTAMENTE

correo = input("Ingresa tu correo: ")
correo.lower()

while True:
    
    if correo.count("@") and correo.endswith(".com"):
        
        print("Tu correo es: ", correo)
        break
            
    else:

        correo = input("Ingresa correctamente tu correo: ")
        print("Has escrito mal el correo")
        correo.lower()
    



        