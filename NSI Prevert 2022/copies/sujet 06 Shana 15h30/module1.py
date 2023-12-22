# Créé par exam.NSI3, le 03/06/2022 en Python 3.7

def nb_repetitions (elt,tab) :
    repetition = 0
    for i in range (len(tab)) :
        if elt == tab[i]:
            repetition +=1
    return repetition




