import math
import cmath
print("Bienvenido a la aplicación de resolver ecuaciones cuadráticas")
print("""
\nUna ecuación cuadrática tiene la forma ax ^ 2 + bx + c = 0
Tus soluciones pueden ser números reales o complejos.
Un número complejo tiene dos partes: a + bj
Donde a es la porción real y bj es la porción imaginaria.""")

ecuacion = input("\n¿Cuantas ecuaciones quieres hacer?")
for i in range(1,int(ecuacion)+1):
    print(f"\nResolviendo la ecuacion #{i}")
    a = float(input("\tIngrese su valor de a (coeficiente de x ^ 2): "))
    b = float(input("\tIngrese su valor de b (coeficiente de x): "))
    c = float(input("\tPor favor ingrese su valor de c (coeficiente): "))
    
    raiz = b**2-4*a*c

    if raiz > 0:
        n1= (-b+math.sqrt(raiz))/2*a
        n2= (-b-math.sqrt(raiz))/2*a

    elif raiz == 0:
        n1= -b/2*a

    else:
        n1= (-b+cmath.sqrt(raiz))/2*a
        n2= (-b-cmath.sqrt(raiz))/2*a

        print(f"\nla solución a la ecuación {a}x²+{b}x+{c}")
    print(f"\tsolucion1 =  {n1}")
    print(f"\tsolucion1 =  {n2}")