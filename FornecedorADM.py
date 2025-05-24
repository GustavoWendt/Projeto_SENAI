from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database
import smtplib
from email.message import EmailMessage

class FornecedorADM():
    def __init__(self, root):
        self.root = root
        self.main_frame = Frame(self.root, bg="#002333")
        self.main_frame.pack(expand=True, fill=BOTH)

        Label(self.main_frame, text="FORNECEDORES | ADM :", bg="#002333", fg="white").place(x=160, y=10)

        Label(self.main_frame, text="ID do Fornecedor:", bg="#002333", fg="white").place(x=400, y=50)
        self.idEntry = ttk.Entry(self.main_frame, width=30)
        self.idEntry.place(x=525, y=50)

        Label(self.main_frame, text="Nome do Fornecedor:", bg="#002333", fg="white").place(x=15, y=50)
        self.FornecedorEntry = ttk.Entry(self.main_frame, width=30)
        self.FornecedorEntry.place(x=150, y=50)

        Label(self.main_frame, text="CNPJ do Fornecedor:", bg="#002333", fg="white").place(x=15, y=90)
        self.CpfFornecedorEntry = ttk.Entry(self.main_frame, width=30)
        self.CpfFornecedorEntry.place(x=150, y=90)

        Label(self.main_frame, text="Telefone do fornecedor:", bg="#002333", fg="white").place(x=15, y=130)
        self.TelefoneFornecedorEntry = ttk.Entry(self.main_frame, width=30)
        self.TelefoneFornecedorEntry.place(x=150, y=130)

        Label(self.main_frame, text="Email do Fornecedor:", bg="#002333", fg="white").place(x=15, y=170)
        self.EmailFornecedorEntry = ttk.Entry(self.main_frame, width=30)
        self.EmailFornecedorEntry.place(x=150, y=170)

        Label(self.main_frame, text="Endereço do Fornecedor:", bg="#002333", fg="white").place(x=15, y=210)
        self.EnderecoFornecedorEntry = ttk.Entry(self.main_frame, width=30)
        self.EnderecoFornecedorEntry.place(x=150, y=210)

        Label(self.main_frame, text="Produto Fornecido:", bg="#002333", fg="white").place(x=15, y=250)
        self.ProdutoFornecedorEntry = ttk.Entry(self.main_frame, width=30)
        self.ProdutoFornecedorEntry.place(x=150, y=250)

        Label(self.main_frame, text="Quantia de Produto:", bg="#002333", fg="white").place(x=10, y=290)
        self.QuantidadeFornecedorEntry = ttk.Entry(self.main_frame, width=30)
        self.QuantidadeFornecedorEntry.place(x=150, y=290)

        # Botões
        ttk.Button(text="Cadastrar", width=15, command=self.RegistrarNoBancoFornecedor).place(x=50, y=330)
        ttk.Button(text="ALTERAR", width=15, command=self.alterarFornecedor).place(x=250, y=330)
        ttk.Button(text="BUSCAR", width=15, command=self.buscaFornecedor).place(x=500, y=100)
        ttk.Button(text="EXCLUIR", width=15, command=self.excluirFornecedor).place(x=50, y=370)
        ttk.Button(text="LIMPAR", width=15, command=self.LimparCampos).place(x=250, y=370)

        Button(self.main_frame, text="VOLTAR AO MENU", width=15, command=self.juntar_funcoes).place(x=650, y=100)

    def RegistrarNoBancoFornecedor(self):
        fornecedores = self.FornecedorEntry.get()
        cpf = self.CpfFornecedorEntry.get()
        telefone = self.TelefoneFornecedorEntry.get()
        email = self.EmailFornecedorEntry.get()
        endereco = self.EnderecoFornecedorEntry.get()
        produto = self.ProdutoFornecedorEntry.get()
        quantidade = self.QuantidadeFornecedorEntry.get()

        if "" in [fornecedores, cpf, telefone, email, endereco, produto, quantidade]:
            messagebox.showerror("Erro de Cadastro", "PREENCHA TODOS OS CAMPOS")
        else:
            db = Database()
            db.RegistrarNoBancoFornecedor(fornecedores, cpf, telefone, email, endereco, produto, quantidade)
            messagebox.showinfo("Sucesso", "Fornecedor registrado com sucesso!")

    def enviar_email_confirmacao(self, email, Fornecedor):
        try:
            msg = EmailMessage()
            msg['Subject'] = 'Cadastro Realizado com Sucesso'
            msg['From'] = 'gustavowendt14@gmail.com'  
            msg['To'] = email
            msg.set_content(f"""
Olá {Fornecedor},

Seu cadastro como funcionário foi realizado com sucesso.

Atenciosamente,
Equipe Vgm Power
""")

            servidor_smtp = 'smtp.gmail.com'
            porta = 465
            email_remetente = 'gustavowendt14@gmail.com'  
            senha = 'rpyo nwlp qynn iple'

            with smtplib.SMTP_SSL(servidor_smtp, porta) as smtp:
                smtp.login(email_remetente, senha)
                smtp.send_message(msg)

        except Exception as e:
            messagebox.showerror("Erro ao enviar e-mail", f"Ocorreu um erro ao enviar o e-mail:\n{e}")


    def alterarFornecedor(self):
        idfornecedor = self.idEntry.get()
        fornecedores = self.FornecedorEntry.get()
        cpf = self.CpfFornecedorEntry.get()
        telefone = self.TelefoneFornecedorEntry.get()
        email = self.EmailFornecedorEntry.get()
        endereco = self.EnderecoFornecedorEntry.get()
        produto = self.ProdutoFornecedorEntry.get()
        quantidade = self.QuantidadeFornecedorEntry.get()

        if "" in [idfornecedor, fornecedores, cpf, telefone, email, endereco, produto, quantidade]:
            messagebox.showerror("Erro de Atualização", "PREENCHA TODOS OS CAMPOS")
        else:
            db = Database()
            db.alterarFornecedor(idfornecedor, fornecedores, cpf, telefone, email, endereco, produto, quantidade)
            messagebox.showinfo("Sucesso", "Fornecedor atualizado com sucesso!")

    def buscaFornecedor(self):
        idfornecedor = self.idEntry.get()
        if idfornecedor == "":
            messagebox.showerror("Erro", "PREENCHA O CAMPO DE ID")
        else:
            db = Database()
            usuario = db.buscar_fornecedor(idfornecedor)
            if usuario:
                self.FornecedorEntry.delete(0, END)
                self.CpfFornecedorEntry.delete(0, END)
                self.TelefoneFornecedorEntry.delete(0, END)
                self.EmailFornecedorEntry.delete(0, END)
                self.EnderecoFornecedorEntry.delete(0, END)
                self.ProdutoFornecedorEntry.delete(0, END)
                self.QuantidadeFornecedorEntry.delete(0, END)
                self.FornecedorEntry.insert(0, usuario[1])
                self.CpfFornecedorEntry.insert(0, usuario[2])
                self.TelefoneFornecedorEntry.insert(0, usuario[3])
                self.EmailFornecedorEntry.insert(0, usuario[4])
                self.EnderecoFornecedorEntry.insert(0, usuario[5])
                self.ProdutoFornecedorEntry.insert(0, usuario[6])
                self.QuantidadeFornecedorEntry.insert(0, usuario[7])
            else:
                messagebox.showerror("Erro", "Fornecedor não encontrado")
                self.LimparCampos()

    def excluirFornecedor(self):
        idfornecedor = self.idEntry.get()
        if idfornecedor == "":
            messagebox.showerror("Erro de Busca", "PREENCHA O CAMPO DE ID")
        else:
            db = Database()
            db.removerFornecedor(idfornecedor)
            messagebox.showinfo("Sucesso", "Fornecedor excluído com sucesso!")
            self.LimparCampos()
        # Criando a combobox
    def buscar_nome_fornecedor(self):
        self.cursor.execute("SELECT fornecedores FROM fornecedor")
        resultados = self.cursor.fetchall()
        return [nome[0] for nome in resultados if nome[0] is not None]



    def LimparCampos(self):
        self.idEntry.delete(0, END)
        self.FornecedorEntry.delete(0, END)
        self.CpfFornecedorEntry.delete(0, END)
        self.TelefoneFornecedorEntry.delete(0, END)
        self.EmailFornecedorEntry.delete(0, END)
        self.EnderecoFornecedorEntry.delete(0, END)
        self.ProdutoFornecedorEntry.delete(0, END)
        self.QuantidadeFornecedorEntry.delete(0, END)

    def voltar_menu(self):
        self.root.destroy()
        from tela_ADM import TeldACASTRO
        root = Tk()
        TeldACASTRO(root)

    def juntar_funcoes(self):
        self.LimparCampos()
        self.voltar_menu()

   

if __name__ == "__main__":
    jan = Tk()
    jan.title("ADM - Leitor Fornecedor")
    jan.geometry("800x400")
    jan.configure(bg="#002333")
    jan.resizable(False, False)
    app = FornecedorADM(jan)
    logo = PhotoImage(file="icon/_SLA_.png") # Carrega a imagem do logo
    LogoLabel = Label(image=logo, bg="#002333") # Cria um label para a imagem do logo
    LogoLabel.place(x=480, y=140) # Posiciona o label no frame esquerdo
    jan.mainloop()

