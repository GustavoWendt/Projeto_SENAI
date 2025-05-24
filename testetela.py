from tkinter import *
from tkinter import ttk, messagebox
import tkinter.font as tkFont
from DataBase import Database  # Certifique-se de ter esse módulo com buscar_fornecedor(id)


class TeldACASTRO:
    def __init__(self, root):
        self.root = root
        self.root.title("VGM Systems - Tela do ADM")
        self.root.geometry("800x500")
        self.root.configure(background="#002333")
        self.root.resizable(False, False)
        self.center_window(800, 500)

        # Fontes
        self.title_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        self.button_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        self.label_font = tkFont.Font(family="Helvetica", size=12)

        # Frame principal
        self.main_frame = Frame(self.root, bg="#002333")
        self.main_frame.pack(expand=True, fill=BOTH)

        self.criar_widgets()

    def criar_widgets(self):
        """Cria os widgets do menu principal."""
        # Header
        self.title_label = Label(self.main_frame, text="VGM Systems", font=self.title_font,
                                 bg="#002333", fg="white")
        self.title_label.pack(pady=(10, 5))

        self.subtitle_label = Label(self.main_frame, text="Painel do ADM", font=self.label_font,
                                    bg="#002333", fg="#a0a0a0")
        self.subtitle_label.pack(pady=(0, 30))

        # Botões centralizados
        self.Produto = Button(self.main_frame, text="ADM - Produto", font=self.button_font,
                              bg="#0078D7", fg="white", activebackground="#0063B1",
                              activeforeground="white", borderwidth=0, width=25, pady=10,
                              command=self.produto)
        self.Produto.pack(pady=8)

        self.Fornecedor = Button(self.main_frame, text="ADM - Fornecedor", font=self.button_font,
                                 bg="#0078D7", fg="white", activebackground="#0063B1",
                                 activeforeground="white", borderwidth=0, width=25, pady=10,
                                 command=self.fornecedor)
        self.Fornecedor.pack(pady=8)

        self.Funcionario = Button(self.main_frame, text="ADM - Funcionário", font=self.button_font,
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

    def produto(self):
        self.limpar_tela()
        from Produto_adm import AbrirProduto_adm
        AbrirProduto_adm(self.main_frame)

    def fornecedor(self):
        self.limpar_tela()
        from Procura_Fornecedor import Procura_Fornecedor
        Procura_Fornecedor(self.main_frame)  # Carrega a tela de busca no mesmo frame

    def funcionario(self):
        self.limpar_tela()
        from TelaFuncionarios_adm import TelaGeral
        TelaGeral(self.main_frame)

    def voltar_menu(self):
        """Volta ao menu principal"""
        self.limpar_tela()
        self.center_window(800, 500)
        self.criar_widgets()



if __name__ == "__main__":
    root = Tk()
    app = TeldACASTRO(root)
    root.mainloop()