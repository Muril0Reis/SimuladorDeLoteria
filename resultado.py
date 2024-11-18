def comparar_numeros(numeros_sorteados, numeros_usuario):
    return len(set(numeros_sorteados).intersection(numeros_usuario))

def exibir_resultado(numeros_sorteados, numeros_usuario, acertos):
    print(f"Números sorteados: {numeros_sorteados}")
    print(f"Seus números: {numeros_usuario}")
    print(f"Quantidade de acertos: {acertos}")

    if acertos == len(numeros_sorteados):
        print("Parabéns! Você acertou todos os números!")
    else: print("Infelizmente não foi dessa vez. Mais sorte na próxima")