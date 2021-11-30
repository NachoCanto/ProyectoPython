print("Welcome to the Thesaurus App!\nChoose a word from the thesaurus and I will give you a synonym.")
import random

print('\n Welcome to the thesaurus app')
sinonimos = {
    "hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
}

print('\n Here are the words in the thesaurus:')
for key in sinonimos:
    print(f'\n {key}')
palabra = input('\n Pick a word you want synonym for : ').lower()
random_no = random.randint(0,4)
if palabra in sinonimos:
    print(f'\n Synonym  for {palabra} is {sinonimos[palabra][random_no]}')
    respuesta = input('\n Would you like to see complete thesaurus ? (y/n) ').lower().strip()
    if respuesta == 'y':
        for key, values in sinonimos.items():
            print(f'\n Word {key} is synonym to : ')
            for value in values:
                print(f'\n - {value}')
    else:
        print('\n Goodbye! Have a nice day.')    
else:
    print(f'\n {palabra} doesn\'t exist!')  
