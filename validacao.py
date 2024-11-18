def validar_entrada(tipo, numeros_usuario):
    if tipo == 1 and len(numeros_usuario) != 6:
        return False
    elif tipo == 2 and len(numeros_usuario) != 5:
        return False
    elif tipo == 3 and len(numeros_usuario) != 15:
        return False

    if tipo == 1 and not all(1 <= n <= 60 for n in numeros_usuario):
        return False
    elif tipo == 2 and not all(1 <= n <= 80 for n in numeros_usuario):
        return False
    elif tipo == 3 and not all(1 <= n <= 25 for n in numeros_usuario):
        return False

    return True
