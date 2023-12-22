# Créé par exam.NSI5, le 03/06/2022 en Python 3.7
def multiplication(n1,n2):
    a=0
    if n1>0 and n2>0:
        for i in range(n2):
            a+=n1
    elif n1<0 and n2<0:
        for i in range(-n2):
            a+=-n1
    elif n1<0:
        for i in range(n2):
            a +=n1
    elif n2<0:
        for i in range(n1):
            a+=n2
    return a

