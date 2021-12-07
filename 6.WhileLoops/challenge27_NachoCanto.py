print('\n Welcome to the Even Odd Number Sorter App')
activar = True

while activar :
    input_usuario = input('\n Enter a list of common seperated numbers : ')
    input_usuario_1 = input_usuario.replace(' ','')
    pares = list()
    impares = list()

    for i in input_usuario_1:
        if int(i) % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
        print(f'\n List of even numbers : {pares}')
        print(f'\n List of odds numbers : {impares}')
    continuar_programa = input('\n Do you want to continue the program ? (y/n) : ').lower().strip()
    if continuar_programa.startswith('n'):
        activar = False
        print('\n Have a nice day!')