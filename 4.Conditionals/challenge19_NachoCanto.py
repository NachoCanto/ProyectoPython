
import random
intentosRealizados = 0
print('¡Hola! ¿Cómo te llamas?')

miNombre = input().title()
número = random.randint(1, 20)

print(f'\nBueno, {miNombre}, estoy pensando en un número entre 1 y 20.')

while intentosRealizados < 5:
    print('\nIntenta adivinar.')
    estimación = int(input("Escriba un número: "))
    intentosRealizados = intentosRealizados + 1

    if estimación < número:
        print('Tu estimación es muy baja.')
    if estimación > número:
        print('Tu estimación es muy alta.')
    if estimación == número:
        break
        
if estimación == número:
    intentosRealizados = str(intentosRealizados)
    print(f'\n¡Buen trabajo, {miNombre} ¡Has adivinado mi número en  {intentosRealizados} intentos!')
if estimación != número:
    número = str(número)
    print(f'\nPues no. El número que estaba pensando era {número}')