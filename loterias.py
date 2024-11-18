import random

def mega_sena():
    return random.sample(range(1, 61), 6)

def quina():
    return random.sample(range(1, 81), 5)

def lotofacil():
    return random.sample(range(1, 26), 15)

def gerar_numeros(tipo):
    if tipo == 1:
        return mega_sena()
    elif tipo == 2:
        return quina()
    elif tipo == 3:
        return lotofacil()
