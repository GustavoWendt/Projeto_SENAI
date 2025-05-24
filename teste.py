# main.py - Com botão de voltar integrado

from tkinter import *
from tkinter import ttk, messagebox
import tkinter.font as tkFont


class TeldACASTRO:
    def __init__(self, root):
        self.root = root
        self.root.title("VGM Systems - Tela do Usuário")
        self.root.geometry("800x400")
        self.root.configure(background="#002333")
        self.root.resizable(False, False)
        self.center_window(800, 400)

        # Fontes
        self.title_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        self.button_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        self.label_font = tkFont.Font(family="Helvetica", size=12)

        # Frame principal
        self.main_frame = Frame(self.root, bg="#002333")
        self.main_frame.pack(expand=True, fill=BOTH)

        self.criar_widgets()

    def criar_widgets(self):
        # Header
        self.title_label = Label(self.main_frame, text="VGM Systems", font=self.title_font,
                                 bg="#002333", fg="white")
        self.title_label.pack(pady=(10, 5))

        self.subtitle_label = Label(self.main_frame, text="Painel do Usuário", font=self.label_font,
                                    bg="#002333", fg="#a0a0a0")
        self.subtitle_label.pack(pady=(0, 30))

        # Botões centralizados em coluna
        self.Produto = Button(self.main_frame, text="Consulta Produto", font=self.button_font,
                              bg="#0078D7", fg="white", activebackground="#0063B1",
                              activeforeground="white", borderwidth=0, width=25, pady=10,
                              command=self.produto)
        self.Produto.pack(pady=8)

        self.Fornecedor = Button(self.main_frame, text="Consulta Fornecedor", font=self.button_font,
                                 bg="#0078D7", fg="white", activebackground="#0063B1",
                                 activeforeground="white", borderwidth=0, width=25, pady=10,
                                 command=self.fornecedor)
        self.Fornecedor.pack(pady=8)

        self.Funcionario = Button(self.main_frame, text="Consulta Funcionário", font=self.button_font,
                                  bg="#0078D7", fg="white", activebackground="#0063B1",
                                  activeforeground="white", borderwidth=0, width=25, pady=10,
                                  command=self.funcionario)
        self.Funcionario.pack(pady=8)

        # Rodapé
        self.version_label = Label(self.main_frame, text="v1.0.0", font=("Helvetica", 8),
                                   bg="#002333", fg="#a0a0a0")
        self.version_label.pack(side=BOTTOM, pady=(30, 0))

    def limpar_tela(self):
        """Limpa todos os widgets dentro do main_frame."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def center_window(self, width, height):
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def voltar_menu_principal(self):
        """Volta para a tela inicial (menu principal)."""
        self.limpar_tela()
        self.center_window(800, 400)  # Redefine o tamanho original
        self.criar_widgets()  # Recarrega os widgets do menu inicial

    def produto(self):
        self.limpar_tela()
        from Procura_Produto import AbrirProduto_cliente
        self.center_window(800, 500)
        AbrirProduto_cliente(self.main_frame, self.voltar_menu_principal)
        self.criar_botao_voltar()

    def fornecedor(self):
        self.limpar_tela()
        from Procura_Fornecedor import ProcuraFornecedor
        ProcuraFornecedor(self.main_frame, self.voltar_menu_principal)
        self.criar_botao_voltar()

    def funcionario(self):
        self.limpar_tela()
        from tela_usuario_funcionario import TelaGeral
        self.center_window(800, 500)
        TelaGeral(self.main_frame, self.voltar_menu_principal)
        self.criar_botao_voltar()

    def criar_botao_voltar(self):
        """Cria um botão de voltar na tela atual."""
        self.btn_voltar = Button(self.main_frame, text="← Voltar", font=self.button_font,
                                 bg="#FF4C4C", fg="white", activebackground="#CC0000",
                                 activeforeground="white", borderwidth=0, width=15,
                                 command=self.voltar_menu_principal)
        self.btn_voltar.pack(pady=20)


if __name__ == "__main__":
    root = Tk()
    app = TeldACASTRO(root)
    root.mainloop()