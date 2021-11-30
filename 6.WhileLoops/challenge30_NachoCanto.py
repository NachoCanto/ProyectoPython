import random

print('\n Welcome to the power ball App.')
bolas_blancas=int(input('\n Enter the white ball numeros : '))
bolas_rojas=int(input('\n Enter the red ball numeros : '))

if bolas_blancas  < 6:
    bolas_blancas = 5
if bolas_rojas < 2:
    bolas_rojas = 1
impares = 1
for i in range(5):
    impares *= bolas_blancas-1
impares *= bolas_rojas/120

print(f'\n odds of your winning with {bolas_blancas} white balls and {bolas_rojas} red balls are : {impares}')

intervalo_ticket = int(input('\n How many tickets would you like to purchase ? '))
numeros_ganadores = list()
while len(numeros_ganadores) < 5:
    bola_blanca_no = random.randint(1,bolas_blancas)
    if bola_blanca_no not in numeros_ganadores:
        numeros_ganadores.append(bola_blanca_no)
numeros_ganadores.sort()

bola_roja_no = random.randint(1,bolas_rojas)
numeros_ganadores.append(bola_roja_no)

print('\n Welcome to the Power ball Game')
print(f'\n Winning balls are : {numeros_ganadores}',end='')
input('\n Press Enter to purchase the tickets')

tickets_comprados=0
jugando=True
tickets_vendidos = []

while numeros_ganadores not in tickets_vendidos and jugando == True:
    numeros_loteria = []
    while len(numeros_loteria) < 5:
        numeros = random.randint(1,bolas_blancas)
        if numeros not in numeros_loteria:
            numeros_loteria.append(numeros)
    numeros_loteria.sort()

    numeros = random.randint(1,bolas_rojas)
    numeros_loteria.append(numeros)

    if numeros_loteria not in tickets_vendidos:
        tickets_comprados+=1
        tickets_vendidos.append(numeros_loteria)
        print(numeros_loteria)
    else:
        print('\n Losing ticket generated. disregard....')

    if tickets_comprados % intervalo_ticket == 0:
        print(str(tickets_comprados) + " tickets purchased so far with no winners...")
        choice = input("\nKeep purchasing tickets (y/n): ")
        if choice != 'y':
            jugando = False        

if numeros_loteria == numeros_ganadores:
    print("\nWinning ticket numeross: ", end='')
    for numeros in numeros_loteria:
        print(str(numeros), end=' ')
        print("\nPurchased a total of " + str(tickets_comprados) + " tickets.")

else:
    print("\nYou bought " + str(tickets_comprados) + " tickets and still lost!")
    print("Better luck next time!") 