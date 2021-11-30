print('\n Welcome to the Yes or No Issue Polling App')
preg_encuesta = input('\n What is the yes or no issue you will be voting on today:  ').title().strip()
max_votantes = int(input('\n What is the number of voters you will allow on the issue: : '))
mast_contraseña = input('\n Enter a password for polling results: ').strip()

yes_count = 0
no_count = 0
result_votos = dict()

for i in range(max_votantes):
    nombre_votantes = input('\n Enter your full name : ').lower().strip()
    if nombre_votantes in result_votos:
        print('\n Sorry! You have already voted!')
    else:
        print(f'\n {preg_encuesta}')
        respuesta_vot = input('\n Enter your response for above displayed question.(y/n) : ').lower().strip()
        if respuesta_vot.startswith('y'):
            yes_count += 1
            result_votos.update({nombre_votantes:'yes'})
        elif respuesta_vot.startswith('n'):
            no_count += 1
            result_votos.update({nombre_votantes:'no'})
        else:
            print('\n You entered an invalid response. It has been recorded but it will not affect the poll results.')
        print('\n Thank you for taking part in this poll. ')

print(f'\n Total number voters that took part : {max_votantes}')
for nombre in result_votos:
    print(f'\n {nombre}')
print(f'\n <-------Voting summary------->')
print(f'\n The Issue : {preg_encuesta}')
print(f'\n Yes : {yes_count} \t\t No: {no_count}')

if yes_count > no_count:
    print('\n Yes Won the poll. ')
elif yes_count < no_count:
    print('\n No Won the poll. ')
else: 
    print('\n It was a tie.') 

ingreso_contra = input('\n Enter the master password if you wish to see the poll results in detail. ').strip()
if ingreso_contra == mast_contraseña:
    for nombre, voto in result_votos.items():
        print(f'\n {nombre} - {voto}')
else:
    print('\nIncorrect password')
print('\n Thank you for using our program.')  