print("Bienvenido a la app de conversion de millas por hora\n")

velocidad = float(input(f"¿Cuál es su velocidad en millas por hora? "))

print(f" Tu velicidad en mp/h {velocidad}")
velocidad = velocidad * 0.447475
print(f" Tu velocidad en nm por s {round(velocidad,2)}")