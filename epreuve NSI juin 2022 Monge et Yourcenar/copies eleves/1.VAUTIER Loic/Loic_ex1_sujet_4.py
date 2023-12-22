# Créé par examen, le 01/06/2022 en Python 3.2

def nb_repetitions(elt,tab):

    cpt = 0

    for element in tab:
        if element == elt:
            cpt+=1

    return cpt


print(nb_repetitions(5,[2,5,3,5,6,9,5]))
3
print(nb_repetitions('A',[ 'B', 'A', 'B', 'A', 'R']))
2
print(nb_repetitions(12,[1, '! ',7,21,36,44]))
0
