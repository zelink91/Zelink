# Créé par examen, le 01/06/2022 en Python 3.2

def moyenne(list):
    if list == []:
        return "erreur"
    else:
        moyenne=0
        for elmt in list:
            moyenne+=elmt
        return moyenne/len(list)


print(moyenne([5,3,8]))
print(moyenne([]))