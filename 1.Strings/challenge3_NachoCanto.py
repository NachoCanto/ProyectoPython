print("Bienvenido a la aplicación de conversión de temperatura")
Fahrenheit= float(input("¿Cuál es la temperatura dada en grados Fahrenheit?"))
print(f"{Fahrenheit}")
Celcius = (Fahrenheit-32)*1.8
print(f"Grados celcius : {round(Celcius,4)}")
kelvin = Fahrenheit +273
print(f"Grados kelvin : {round(kelvin,4)}")