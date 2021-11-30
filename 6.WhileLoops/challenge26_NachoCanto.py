print('\n Welcome to the factor generator app.')
activar = True

while activar:
    input_usuario = int(input('\n Enter a number to determine all factors of that number: '))
    factores = list()
    for i in range(1,input_usuario+1):
        if input_usuario % i == 0:
            factores.append(i)
    print('\n Printing all the factores.') 
    print(f'\n All the factores for {input_usuario} are : {factores}')

    for i in range(int(len(factores)/2)):
        print(f'\n {factores[i]} * {factores[-i-1]} ')

    continuar_programa = input('\n Do you want to continue the program ? (y/n) : ').lower().strip()

    if continuar_programa.startswith('n'):
        activar = False
        print('\n Have a nice day!')