import math
print(f"Bienvenido a la aplicación de Calculo Factorial\n")

fact = int(input(f"¿De qué número le gustaría calcular el factorial?  "))
factorial = 1

for i in range(1,fact+1):

        if i == 1:
                print(f"\t{fact}! = 1*", end = "")
        
        elif i == fact:
                print(f"{i}\n")
        
        else:
                print(f"{i}*", end = "")

        factorial = factorial * i


print(f"\nAquí está el resultado de la biblioteca matemática:\nEl factorial de {fact} es {math.factorial(fact)}!\n")
print(f"Aquí está el resultado de mi propio algoritmo:\nEl factorial de {fact} es {math.factorial(fact)}!\n")
print(f"Se muestra dos veces que {fact}! = {factorial}")