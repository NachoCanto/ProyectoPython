#Usar import math1 para poder operar con raíces
import math
base= float(input("¿Cual es la base? "))
altura= float(input("¿Cual es la altura? "))
area= 0.5*base*altura
hipotenusa= round(math.sqrt((base**2)+(altura**2)),3)

print(f"La base es de: {base}")
print(f"La altura es de: {altura}")
print(f"El triangulo está formado por una altura de {altura}  y una base de  {base} . Su area es  {area}")
print(f"El triangulo está formado por una altura de {altura}  y una base de  {base} . Su hipotenusa es  {hipotenusa}")
