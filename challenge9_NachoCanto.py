#Ej 7
print("Bienvenido a la organizacion de la plantilla de basket")
base =input("\n¿Quién es tu base? ").upper()
escolta =input("¿Quién es tu escolta? ").upper()
alero = input("¿Quién es tu alero? ").upper()
ala_pivot = input("¿Quién es tu ala-pivot? ").upper()
central = input("¿Quién es tu central? ").upper()
print("\n")
print("Este es su 5 inicial para esta temporada: ")
print(f"""\n
Base        =          {base}
Escolta     =          {escolta}
Alero       =          {alero}
Ala-pivot   =          {ala_pivot}
Central     =          {central}""")
list = [base,escolta,alero,ala_pivot,central]
list.remove(central)
print("\n\n")
print(f"\n OH NO! tu jugador {alero} se ha lesionado, tendrás que reemplazarlo")
lesionado= input("\n ¿Quién te gustaría que lo reemplazara? ").upper()
print("\nSu nuevo 5 inicial para esta temporada es: ")
print(f"""\n
Base      =         {base}
Escolta   =         {escolta}
Alero     =         {lesionado}
Ala-pivot =         {ala_pivot}
Central   =         {central}""")
print("")
print(f"Buena suerte {lesionado} ¡Lo hará genial!")