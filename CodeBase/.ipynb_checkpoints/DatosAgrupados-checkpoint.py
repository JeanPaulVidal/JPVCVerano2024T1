# Frecuencia Relativa
def frecRel(frecAbs):
    frecRel = []
    frecAbsT = sum(frecAbs)
    for element in frecAbs:
        fr = 100 / frecAbsT * element
        frecRel.append(fr)
    return frecRel

# Frecuencia Acumulada
def frecAc(frec):
    frecAc = []
    ultVal = 0
    for element in frec:
        fAc = element
        frecAc.append(fAc+ultVal)
        ultVal += fAc
    return frecAc


import math

import math

def clases_groped(datos):
    datos.sort()
    minVal = datos[0]
    maxVal = datos[-1]
    
    rango = maxVal - minVal
    numClases = 6
    anchoClase = rango / numClases

    limsInf = []
    limsSup = []
    mrksClases = []
    for i in range(1, numClases+1):
        limInf = minVal + (i-1) * anchoClase
        limSup = minVal + i * anchoClase
        mrkClase = (limInf + limSup) / 2
        limsInf.append(limInf)
        limsSup.append(limSup)
        mrksClases.append(mrkClase)
    
    clases = list(range(1, numClases+1))
    return clases, limsInf, limsSup, mrksClases


def faGrouped(limSup, limInf, datos):
    fa = [0] * len(limInf)
    for dato in datos:
        for j in range(len(limInf)):
            if limInf[j] <= dato <= limSup[j]:
                fa[j] += 1
                break

    return fa
