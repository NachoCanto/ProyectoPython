nombre= input("Hola! Bienvenido \n¿Cual es tu nombre? ").upper()
print("Hola " + nombre + " Hoy vas a hacer un programa que cuente la letra que elijas.")
mensaje= input("Cual quieres que sea tu mensaje?: ")
letra= input("Que letra quieres contar: ").lower()
contador= mensaje.count(letra)
#utilizar str para convertir en cadenas
print("Su letra se repite " + str(contador) + " veces la letra " + str(letra))