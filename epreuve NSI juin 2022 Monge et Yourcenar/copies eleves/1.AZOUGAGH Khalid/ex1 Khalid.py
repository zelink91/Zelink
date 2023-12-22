# Créé par examen, le 01/06/2022 en Python 3.2

def mini(releve,date):
    min=releve[0]
    ind=0
    for i in range (len(releve)-1):
        if releve[i]<min:
            min=releve[i]
            ind=i
    return min , date[ind]


t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 12.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]