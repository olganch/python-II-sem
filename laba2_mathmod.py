import numpy as np

Pol = list(map(float, input().split()))

def Diff_pol(Pol):                  #polinomial derivative
    Diff_pol = [0]*len(Pol)
    for i in range(len(Pol)):
        Diff_pol[i] = Pol[i]*(len(Pol)-1-i)
    Diff_pol.pop()
    return Diff_pol

def Horner(Pol, Xo):                #Horner's method
    Xn = Pol[0]
    for i in range (len(Pol)-1):
        Xn = Pol[i+1] + Xn*Xo
    return Xn

def Upper_Bound(Pol):               #Ну, в принципе, в заданиях отрезки получились вложbенными в мои
    """b0 = Pol[0]
    for i in range (len(Pol)):
        Pol[i] = Pol[i]/b0
    for i in range(len(Pol)):
        if (Pol[i] < 0):
            n = i
            break
    N = abs(min(Pol))
    An = 1 + pow(N, 1/n)"""
    """An = Pol[len(Pol)]/(max(Pol[0:(len(Pol)-1)])+Pol[len(Pol)])"""
    An = 1 + max(Pol[1:len(Pol)])/abs(Pol[0])
    return An

def Bottom_Bound(Pol):              #нижняя граница
    for i in range (0,len(Pol),2):
        Pol[i] *= (-1)
    Bn = -Upper_Bound(Pol)
    return Bn

def Dichotomy(An, Bn):
    while True:
        if (An*Bn > 0):
            print ("Fail\n")
        if (An*((An*Bn)/2) > 0):
            An = (An+Bn)/2
        elif (Bn*((An*Bn)/2) > 0):
            Bn = (An+Bn)/2
        if (abs((An-Bn)) >= 0.001):
            break
    return abs(An - Bn)

print(Dichotomy(Upper_Bound(Pol), Bottom_Bound(Pol)))


