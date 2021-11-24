print("Bienvenido a la aplicación de tablas de multiplicar")
nombre = input("¿Cual es tu nombre? ").title()
numero = float(input("¿Que numero quieres utilizar? "))
#Uso float por los decimales a la hora de operar 
print(f"Tabla de multiplicar del {numero}")
print(f"""\t   1.0*{numero} = {numero * 1} 
           2.0*{numero} = {numero * 2}
           3.0*{numero} = {numero * 3}
           4.0*{numero} = {numero * 4}
           5.0*{numero} = {numero * 5}
           6.0*{numero} = {numero * 6}
           7.0*{numero} = {numero * 7}
           8.0*{numero} = {numero * 8}
           9.0*{numero} = {numero * 9}
           0.0*{numero} = {numero * 0}""")
print(f""" Ahora lo elevaremos a {numero}
           1.0**{numero} = {numero ** 1}
           2.0**{numero} = {numero ** 2}
           3.0**{numero} = {numero ** 3}
           4.0**{numero} = {numero ** 4}
           5.0**{numero} = {numero ** 5}
           6.0**{numero} = {numero ** 6}
           7.0**{numero} = {numero ** 7}
           8.0**{numero} = {numero ** 8}
           9.0**{numero} = {numero ** 9}
           0.0**{numero} = {numero ** 0}""")
print(f"{nombre} LAS MATEMÁTICAS SON GENIALES")