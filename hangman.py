
import random
file = open("liste_francais.txt")
allText = file.read()
# print(allText)
words = list(map(str, allText.split()))


# print random string
random_words = random.choice(words)
randomToList = list(random_words)
userWord = []
print('random_words = ', random_words)
# print(randomToList)
compteur = 0 
lettre_trouver = ''



# function to generate underscore

def underscore(mot):
    r = '_ ' * len(mot)
    userWord = r[:-1].split(' ')
    print(' '.join(userWord))
    return userWord

userWord = underscore(randomToList)

while ((compteur <= 7)  or ''.join(userWord) == random_words):



# fonction pour afficher le pendu
    potence = []

    potence.append('     ==========Y===')
    potence.append('    ||  /      |')
    potence.append('    || /       |')
    potence.append('    ||/        O')
    potence.append('    ||        /|\\')
    potence.append('    ||        / \\')
    potence.append('    ||\n'
                '   /||\n'
                '  //||\n'
                '============')


    def display_pendue(nb):
        for e in range(nb):
            print(potence[e])

    display_pendue(compteur)

    if(compteur == 7):
        print("You Lose")
        quit()
    # fin de la fonction afficher le pendu



    # Vérification de la lettre

    def verifLetter(x):
        if x in random_words:
            global lettre_trouver
            lettre_trouver = x
            return lettre_trouver
        else:
            global compteur
            compteur += 1

    def add_letter_in_word(mot_1):
        INDICE_LIST = []

        for i in range(len(randomToList)):
            if mot_1 == randomToList[i]:
                INDICE_LIST.append(i)

        for i in INDICE_LIST:

            userWord[i] = lettre_trouver

        INDICE_LIST.clear()

    verifLetter(input('Choisir une lettre :').lower())
    add_letter_in_word(lettre_trouver)
    print(' '.join(userWord))