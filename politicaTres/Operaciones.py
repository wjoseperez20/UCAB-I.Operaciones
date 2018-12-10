import random


def GenerarRandom():
    numero = round(random.random(), 4)
    return numero


def OrdenarLista(diccionario):
    return [(k, diccionario[k]) for k in sorted(diccionario)]
