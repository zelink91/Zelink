def insere(a, tab):
    l = list(tab) #l contient les mÃªmes Ã©lÃ©ments que tab
    l.append(a)
    i = len(tab)-1
    while a < tab[i]  and i >= 0:
      l[i+1] = tab[i]
      l[i] = a
      i = i-1
    return l
print(insere(2,[1,3,5]))