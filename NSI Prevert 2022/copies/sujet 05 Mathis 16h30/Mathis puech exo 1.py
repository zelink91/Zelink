# Créé par exam.NSI3, le 03/06/2022 en Python 3.7

def occurence_lettres(phrase):
    if len(phrase)>0:
        dico={}
        b=0
        for i in range (len(phrase)):
            for c in range (len(phrase)):
                if phrase[i]==phrase[c]:
                    b=b+1
            dico[phrase[i]]=b
            b=0
        return dico
    else:
        return "votre phrase est vide"

phrase=("bonjoure")

