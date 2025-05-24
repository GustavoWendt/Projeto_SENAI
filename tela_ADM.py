# main.py - Com botão de voltar integrado

from tkinter import *
from tkinter import ttk, messagebox
import tkinter.font as tkFont


class TeldACASTRO:
    def __init__(self, root):
        self.root = root
        self.root.title("VGM Systems - Tela do ADM")
        self.root.geometry("800x400")
        self.root.configure(background="#002333")
        self.root.resizable(False, False)
        self.center_window(500, 500)

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

        self.subtitle_label = Label(self.main_frame, text="Painel do ADM", font=self.label_font,
                                    bg="#002333", fg="#a0a0a0")
        self.subtitle_label.pack(pady=(0, 30))

        # Botões centralizados em coluna
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

        self.Funcionario = Button(self.main_frame, text="ADM - Cliente", font=self.button_font,
                                  bg="#0078D7", fg="white", activebackground="#0063B1",
                                  activeforeground="white", borderwidth=0, width=25, pady=10,
                                  command=self.CRUD_cliente)
        self.Funcionario.pack(pady=8)

        self.Funcionario = Button(self.main_frame, text="ADM - Fazer pedido", font=self.button_font,
                                  bg="#0078D7", fg="white", activebackground="#0063B1",
                                  activeforeground="white", borderwidth=0, width=25, pady=10,
                                  command=self.pedido)
        self.Funcionario.pack(pady=8)

        Button(self.main_frame, text="LOGOUT", width=15, bg="#0078D7", fg="white",
            command=self.voltar_login).pack(pady=20)
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
        self.root.destroy()
        from Produto_adm import AbrirProduto_adm
        root = Tk()
        root.geometry("800x400")
        AbrirProduto_adm(root)
        logo = PhotoImage(file="icon/_SLA_.png") # Carrega a imagem do logo
        LogoLabel = Label(image=logo, bg="#002333") # Cria um label para a imagem do logo
        LogoLabel.place(x=490, y=180) # Posiciona o label no frame esquerdo
        # Centraliza a janela principal também
        self.center_window(root, 800, 600)

        root.mainloop()


    def fornecedor(self):
        self.root.destroy()
        from FornecedorADM import FornecedorADM
        root = Tk()
        root.geometry("800x400")
        FornecedorADM(root)
        logo = PhotoImage(file="icon/_SLA_.png") # Carrega a imagem do logo
        LogoLabel = Label(image=logo, bg="#002333") # Cria um label para a imagem do logo
        LogoLabel.place(x=490, y=150) # Posiciona o label no frame esquerdo

        root.mainloop()
        
    def funcionario(self):
        self.root.destroy()
        from TelaFuncionarios_adm import TelaGeral
        root = Tk()
        root.geometry("800x400")
        TelaGeral(root)
        logo = PhotoImage(file="icon/_SLA_.png") # Carrega a imagem do logo
        LogoLabel = Label(image=logo, bg="#002333") # Cria um label para a imagem do logo
        LogoLabel.place(x=490, y=150) # Posiciona o label no frame esquerdo

        root.mainloop()

    def CRUD_cliente(self):
        self.root.destroy()
        from cadastro_cliente import Abrir_Cliente
        root = Tk()
        root.geometry("800x400")
        Abrir_Cliente(root)
        root.mainloop()

    def pedido(self):
        self.root.destroy()
        from pedido import AbrirPedido_adm
        root = Tk()
        root.geometry("800x400")
        AbrirPedido_adm(root)
        root.mainloop()

    def voltar_menu(self):
        """Volta ao menu principal"""
        self.limpar_tela()
        self.center_window(800, 400)
        self.criar_widgets()

    def voltar_login(self):
        """Fecha a tela atual e abre uma NOVA janela com a tela de login"""
        self.root.destroy()  # Fecha a tela atual

        # Cria uma NOVA janela
        login_window = Tk()
        login_window.title("VGM Systems - Login")
        login_window.geometry("500x400")
        login_window.configure(bg="#002333")
        login_window.resizable(False, False)

        # Centraliza a nova janela
        self.center_window_on(login_window, 500, 400)

        # Carrega a tela de login nessa nova janela
        from tela_de_login import LoginSystem  # Substitua 'wig' pelo nome do arquivo da tela de login
        LoginSystem(login_window)  # Inicia a tela de login

        # Inicia o loop da nova janela
        login_window.mainloop()

    def center_window_on(self, window, width, height):
        """Centraliza qualquer janela na tela."""
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')
        
if __name__ == "__main__":
    root = Tk()
    app = TeldACASTRO(root)
    root.mainloop() 