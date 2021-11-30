from collections import Counter
print('\n Welcome the Frequency Analysis app.')


def analyse_phrase():
    no_letras = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ','.', '?', '!', ',', '"', "'", ':', ';', '(', ')', '%', '$', '&', '#', '\n', '\t']

    frase_usuario = input('\nEnter a phrase to be analyzed : ').lower().strip()

    for caracter in no_letras:
        frase_usuario = frase_usuario.replace(caracter,'')

    total_frase = len(frase_usuario)
    contador = Counter(frase_usuario)

    print("\nHere is the frequency analysis from key phrase 1: ")
    print("\n\tLetter\t\tOccurrence\tPercentage")
    # Result
    for char, count in sorted(contador.items()):
        print(
            f'\nCharacter : {char}\t\t count : {count} \t\t % : {round((count/total_frase)*100)}')

    orden_contador = contador.most_common()
    frase_usuario_letras_ordenadas = []
    for pair in orden_contador:
        frase_usuario_letras_ordenadas.append(pair[0])

    print("\nLetters ordered from highest occurrence to lowest: ")
    for letra in frase_usuario_letras_ordenadas:
        print(letra, end='')

analyse_phrase() 