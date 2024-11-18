from loterias import gerar_numeros
from validacao import validar_entrada
from resultado import comparar_numeros, exibir_resultado

def menu():
    print("Bem-vindo ao simulador de loteria!")
    print("Escolha o tipo de loteria:")
    print("1 - Mega Sena")
    print("2 - Quina")
    print("3 - Lotofácil")
    
    tipo = int(input("Digite o número da loteria que você quer jogar (1, 2 ou 3): "))
    
    if tipo not in [1, 2, 3]:
        print("Opção inválida. Tente novamente.")
        return

    numeros_sorteados = gerar_numeros(tipo)

    print("Digite seus números da sorte:")
    if tipo == 1:
        limite = 60
        quantidade = 6
    elif tipo == 2:
        limite = 80
        quantidade = 5
    else:
        limite = 25
        quantidade = 15

    while True:
        try:
            entrada_usuario = input(f"Digite {quantidade} números entre 1 e {limite}: ")
            numeros_usuario = []

            if ',' in entrada_usuario:
                numeros_usuario = list(map(int, entrada_usuario.replace(',', ' ').split()))
            elif ' ' in entrada_usuario:
                numeros_usuario = list(map(int, entrada_usuario.split()))

            if len(numeros_usuario) != quantidade:
                print(f"Você deve inserir exatamente {quantidade} números.")
                continue
            if not validar_entrada(tipo, numeros_usuario):
                print(f"Os números devem estar no intervalo correto. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros separados por espaço ou vírgula.")
    
    acertos = comparar_numeros(numeros_sorteados, numeros_usuario)
    exibir_resultado(numeros_sorteados, numeros_usuario, acertos)

menu()
