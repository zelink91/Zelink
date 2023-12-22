# Créé par examen, le 01/06/2022 en Python 3.2

def recherche(a,t):
    occurrence=0
    for i in range(len(t)):
        if a==t[i]:
            occurrence+=1
    return occurrence


print(recherche(5,[]))

print(recherche(5,[-2, 3, 4, 8]))

print(recherche(5,[-2, 3, 1, 5, 3, 7, 4]))

print(recherche(5,[-2, 5, 3, 5, 4, 5]))
