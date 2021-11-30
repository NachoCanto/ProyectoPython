import time

print('\n Welcome to the prime number app')

activar =True

while activar:
    programa_tipo = input('\n What kind of prime no. app do you want (1/2/3) . : ')

    if programa_tipo == '1':
        input_numero_ususario = int(input('\n Enter the number you want to check :'))
        premium=True
        for i in range(2,input_numero_ususario):
            if input_numero_ususario%i == 0:
                premium=False
                break

        if premium:
            print(f'\n Entered number {input_numero_ususario} is prime.')    
        else:
            print(f'\n Entered number {input_numero_ususario} is not prime. ')    

    elif programa_tipo == '2':
        limite_inferior = int(input('\n Enter the lower bound for the range of numbers. '))
        limite_superior = int(input('\n Enter the upper bound for the range of numbers. '))        
        primes = list()
        start_time = time.time()
        for i in range(limite_inferior, limite_superior+1):
            if i > 1:
                premium=True
                for j in range(2,i):
                    if i % j == 0:
                        premium=False
                        break

            else:
                premium=False

            if premium:
                primes.append(i)
        end_time = time.time()
        delta_time = round(end_time - start_time, 4)
        print('\n Calculations took a total of'+ str(delta_time)+ ' seconds.')
        print("The following numbers between " + str(limite_inferior) + " and " + str(limite_superior) + " are prime: ")
        input("Press enter to continue.")
        for prime in primes:
            print(prime)

    else:
        print('\n That is not a valid option.')

    continue_program = input('\n Do you want to continue the program ? (y/n) : ').lower().strip()
    if continue_program.startswith('n'):
            activar = False
            print('\n Have a nice day!')