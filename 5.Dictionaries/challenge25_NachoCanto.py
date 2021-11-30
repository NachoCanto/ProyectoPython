from collections import Counter
"""
RULES 
You should be able to encode or decode a message regardless of the key phrases
chosen.
To In order to accomplish this, you must look at the frequency analysis of the two key
phrases.
Given a character in the secret message that is to be encoded, you must find its index in
the frequency analysis of the first message.
Then find the letter that appears at the same index in the frequency analysis of the
second message.
This is your encoding rule to encode one character as another.
For example, the letter "o" appears at index 1 in the first frequency analysis. The letter "t"
appears at index 1 in the second frequency analysis. Therefore the letter “o” would be
encoded to the letter “t”.
The letter “h” appears at index 7 in the first frequency analysis. The letter “r” appears at
index 7 in the second frequency analysis. Therefore the letter “h” would be encoded to
the letter “r”.
Similarly, the word “oh” would be encoded to “tr” using the given key phrases.
"""

def filtro_letras(input_frase:str):
    no_letras = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '@','.', '?', '!', ',', '"', "'", ':', ';', '(', ')', '%', '$', '&', '#', '\n', '\t']

    frase_usuario = input_frase.lower().strip()

    for caracter in no_letras:
        frase_usuario = frase_usuario.replace(caracter,'')

    return frase_usuario

def analyse_phrase(input_frase:str):

    frase_usuario = filtro_letras(input_frase)

    total_ocurrencias = len(frase_usuario)
    contador_letras = Counter(frase_usuario)

    print("\nHere is the frequency analysis from key phrase 1: ")
    print("\n\tLetter\t\tOccurrence\tPercentage")
    # Result
    for char, count in sorted(contador_letras.items()):
        print(
            f'\n Character : {char}\t\t count : {count} \t\t % : {round((count/total_ocurrencias)*100)}')

    contador_letras_ordenadas = contador_letras.most_common()
    frase_usuario_letras_ordenadas = []
    for pair in contador_letras_ordenadas:
        frase_usuario_letras_ordenadas.append(pair[0])

    print("\nLetters ordered from highest occurrence to lowest: ")
    for letter in frase_usuario_letras_ordenadas:
        print(letter, end='')

    return frase_usuario_letras_ordenadas

texto_1 = """
To Sherlock Holmes she is always the woman. I have seldom heard him mention her under any
other name.
In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any
emotion akin to love for Irene Adler.
All emotions, and that one particularly, were abhorrent to his cold, precise but admirably
balanced mind.
He was, I take it, the most perfect reasoning and observing machine that the world has seen,
but as a lover he would have placed himself in a false position.
He never spoke of the softer passions, save with a gibe and a sneer.
They were admirable things for the observer excellent for drawing the veil from men's motives
and actions.
But for the trained reasoner to admit such intrusions into his own delicate and finely adjusted
temperament was to introduce
a distracting factor which might throw a doubt upon all his mental results.
Grit in a sensitive instrument, or a crack in one of his own highpower lenses,
would not be more disturbing than a strong emotion in a nature such as his.
And yet there was but one woman to him, and that woman was the late Irene Adler, of dubious
and questionable memory.
I had seen little of Holmes lately. My marriage had drifted us away from each other.
My own complete happiness, and the homecentred interests which rise up around the man who
first finds himself master of his own establishment,
were sufficient to absorb all my attention, while Holmes, who loathed every form of society with
his whole Bohemian soul,
remained in our lodgings in Baker Street, buried among his old books, and alternating from
week to week between cocaine and ambition,
the drowsiness of the drug, and the fierce energy of his own keen nature.
He was still, as ever, deeply attracted by the study of crime,
and occupied his immense faculties and extraordinary powers of observation in following out
those clues,
and clearing up those mysteries which had been abandoned as hopeless by the official police.
From time to time I heard some vague account of his doings: of his summons to Odessa in the
case of the Trepoff murder,
of his clearing up of the singular tragedy of the Atkinson brothers at Trincomalee,
and finally of the mission which he had accomplished so delicately and successfully for the
reigning family of Holland.
Beyond these signs of his activity, however, which I merely shared with all the readers of the
daily press, I knew little of my former friend and companion.
"""

texto_2 = """
Quite so! You have not observed. And yet you have seen.
That is just my point. Now, I know that there are seventeen steps, because I have both seen
and observed.
By the way, since you are interested in these little problems,
and since you are good enough to chronicle one or two of my trifling experiences, you may be
interested in this.
He threw over a sheet of thick, pink tinted notepaper which had been lying open upon the table.
It came by the last post, said he. Read it aloud.
The note was undated, and without either signature or address.
There will call upon you tonight, at a quarter to eight o'clock,
it said, "a gentleman who desires to consult you upon a matter of the very deepest moment.
Your recent services to one of the royal houses of Europe have shown that you are one who
may safely be trusted
with matters which are of an importance which can hardly be exaggerated.
This account of you we have from all quarters received.
Be in your chamber then at that hour, and do not take it amiss if your visitor wear a mask.
This is indeed a mystery, I remarked. What do you imagine that it means?
I have no data yet. It is a capital mistake to theorise before one has data.
Insensibly one begins to twist facts to suit theories, instead of theories to suit facts.
But the note itself. What do you deduce from it?
I carefully examined the writing, and the paper upon which it was written.
The man who wrote it was presumably well to do, I remarked, endeavouring to imitate my
companion's processes.
Such paper could not be bought under half a crown a packet.
It is peculiarly strong and stiff.
"""



def main_app ():
    print('\n Welcome to the Code Breaker App')

    frase_ordenada_1 = analyse_phrase(texto_1)
    frase_ordenada_2 = analyse_phrase(texto_2)

    respuesta_usuario = input('\n Would You like to encode or decode : (e/d) ').lower().strip()
    mensaje_usuario = input('\n Enter your message. : ').lower().strip()

    mensaje_filtrado = filtro_letras(mensaje_usuario)

    lista_codificada = list()
    lista_descifrada = list()

    if respuesta_usuario.startswith('e'):
        for letra in mensaje_filtrado:
            indice = frase_ordenada_1.indice(letra)
            letra  = frase_ordenada_2[indice]
            lista_codificada.append(letra)

        print('\n Encoded message :')
        for letra in lista_codificada:
            print(letra, end='')    

    elif respuesta_usuario.startswith('d'):
        for letra in mensaje_filtrado:
            indice = frase_ordenada_2.indice(letra)
            letra = frase_ordenada_1[indice]
            lista_descifrada.append(letra)

        print('\n Decoded message : ')
        for letra  in lista_descifrada:
            print(letra, end='')    
    else:
        print('\n Well, that\'s an invalid selection.')

main_app() 