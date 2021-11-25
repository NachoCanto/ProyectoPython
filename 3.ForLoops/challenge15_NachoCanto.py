import statistics as stats
print(f"Bienvenido a la aplicación Calculadora de promedios\n")

nombre = input(f"Cuál es su nombre:  ").title()
numero_grados = int(input(f"¿A cuántos grados le gustaría ingresar?  "))

grados = []

for i in range(1,numero_grados+1):
    grade = int(input(f"Introduzca los grados  "))
    grados.append(grade)

print(f"\nGrados de mayor a menor: ")

clasif_grados = sorted(grados)
for i in range(1,numero_grados+1):
    print(f"{clasif_grados[len(clasif_grados)-i]}")

print(f"Resumen de calificaciones de {nombre}: ")
print(f"\tNúmero total de calificaciones: {numero_grados}")
print(f"\tCalificacion mas alta {max(clasif_grados)}")
print(f"\tCalificacion mas pequeña {min(clasif_grados)}")
print(f"\tPromedio: {round(stats.mean(clasif_grados),2)}")

next_grade = int(input(f"¿Cuál es su promedio deseado?  "))
print(f"\t\tBuena suerte {nombre}")