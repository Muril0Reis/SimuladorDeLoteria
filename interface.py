import tkinter as tk
from loterias import gerar_numeros
from validacao import validar_entrada
from resultado import comparar_numeros


class LoteriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Loteria")
        self.root.geometry("600x700")

        # Variável para armazenar o tipo de loteria selecionado
        self.loteria_tipo = tk.IntVar(value=1)

        # Cores de fundo para cada loteria
        self.cores = {1: "#017a4f", 2: "#2a2879", 3: "#a7348b"}

        # Imagens para cada loteria
        self.mega_img = tk.PhotoImage(file="mega_sena.png").subsample(2, 2)  # Reduz tamanho da imagem
        self.quina_img = tk.PhotoImage(file="quina.png").subsample(2, 2)
        self.lotofacil_img = tk.PhotoImage(file="lotofacil.png").subsample(2, 2)

        # Exibe a primeira imagem (Mega-Sena por padrão)
        self.image_label = tk.Label(root, image=self.mega_img, bg=self.cores[1])
        self.image_label.pack(pady=10)

        # Título
        self.titulo_label = tk.Label(root, text="Escolha sua Loteria", font=("Arial", 20), bg=self.cores[1], fg="white")
        self.titulo_label.pack(pady=15)

        # Botões de seleção
        self.create_radio_buttons()

        # Entrada de números
        self.numeros_label = tk.Label(root, text="Digite seus números (separados por vírgula):", font=("Arial", 14),
                                      bg=self.cores[1], fg="white")
        self.numeros_label.pack(pady=10)
        self.numeros_entry = tk.Entry(root, width=40)
        self.numeros_entry.pack(pady=5)

        # Botão para jogar
        self.jogar_button = tk.Button(root, text="Jogar", font=("Arial", 14), command=self.jogar)
        self.jogar_button.pack(pady=10)

        # Resultado
        self.resultado_label = tk.Label(root, text="", font=("Arial", 14), bg=self.cores[1], fg="white")
        self.resultado_label.pack(pady=10)

    def create_radio_buttons(self):
        """Cria os botões de seleção de loteria."""
        self.radio_buttons_frame = tk.Frame(self.root, bg=self.cores[1])  # Frame identificado
        self.radio_buttons_frame.pack(pady=10)

        tk.Radiobutton(self.radio_buttons_frame, text="Mega-Sena", variable=self.loteria_tipo, value=1,
                       command=self.update_interface, bg=self.cores[1], fg="white").grid(row=0, column=0, padx=10)
        tk.Radiobutton(self.radio_buttons_frame, text="Quina", variable=self.loteria_tipo, value=2,
                       command=self.update_interface, bg=self.cores[1], fg="white").grid(row=0, column=1, padx=10)
        tk.Radiobutton(self.radio_buttons_frame, text="Lotofácil", variable=self.loteria_tipo, value=3,
                       command=self.update_interface, bg=self.cores[1], fg="white").grid(row=0, column=2, padx=10)

    def update_interface(self):
        """Atualiza a imagem, a cor do fundo e o frame com base na loteria selecionada."""
        tipo = self.loteria_tipo.get()
        cor = self.cores[tipo]

        # Atualiza o fundo geral
        self.root.config(bg=cor)
        self.titulo_label.config(bg=cor)
        self.numeros_label.config(bg=cor)
        self.resultado_label.config(bg=cor)

        # Atualiza o frame dos botões
        self.radio_buttons_frame.config(bg=cor)

        # Atualiza os botões de seleção
        for widget in self.radio_buttons_frame.winfo_children():
            widget.config(bg=cor)

        # Atualiza a imagem
        if tipo == 1:
            self.image_label.config(image=self.mega_img, bg=cor)
        elif tipo == 2:
            self.image_label.config(image=self.quina_img, bg=cor)
        elif tipo == 3:
            self.image_label.config(image=self.lotofacil_img, bg=cor)

    def jogar(self):
        """Simula o jogo, valida a entrada e exibe o resultado."""
        tipo = self.loteria_tipo.get()
        entrada = self.numeros_entry.get()

        # Definir os limites e quantidades com base na loteria selecionada
        limites = {1: (6, 60), 2: (5, 80), 3: (15, 25)}
        quantidade, limite = limites[tipo]

        try:
            # Converter entrada do usuário em uma lista de números
            numeros_usuario = list(map(int, entrada.replace(",", " ").split()))
            if not validar_entrada(tipo, numeros_usuario):
                raise ValueError(f"Você deve inserir {quantidade} números entre 1 e {limite}.")

            # Gerar números sorteados
            numeros_sorteados = gerar_numeros(tipo)

            # Comparar números e calcular acertos
            acertos = comparar_numeros(numeros_sorteados, numeros_usuario)

            # Mensagem de resultado
            resultado = f"Números sorteados: {numeros_sorteados}\n" \
                        f"Seus números: {numeros_usuario}\n" \
                        f"Acertos: {acertos}"

            if acertos == quantidade:
                resultado += "\nParabéns, você ganhou!"
            else:
                resultado += "\nNão foi desta vez. Tente novamente!"

            self.resultado_label.config(text=resultado, fg="white")

        except ValueError as e:
            self.resultado_label.config(text=str(e), fg="white")


# Inicializa a interface
if __name__ == "__main__":
    root = tk.Tk()
    app = LoteriaApp(root)
    root.mainloop()