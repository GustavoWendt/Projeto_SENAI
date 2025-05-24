from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database
import tkinter as tk
import smtplib
from email.message import EmailMessage

class TelaGeral:
    def __init__(self, root):
        self.root = root
        self.main_frame = Frame(self.root, bg="#002333")
        self.main_frame.pack(expand=True, fill=BOTH)

        tituloLabel = Label(self.root, text="TELA GERAL FUNCIONÁRIOS", bg="#002333", fg="white")
        tituloLabel.place(x=230, y=10)

        field_bg = "#004455"
        text_fg = "white"

        Label(self.root, text="ID DO FUNCIONARIO(A):", bg="#002333", fg=text_fg).place(x=360, y=40)
        self.ID_funcionarioEntry = ttk.Entry(self.root, width=30)
        self.ID_funcionarioEntry.place(x=500, y=40)

        Label(self.root, text="CPF:", bg="#002333", fg=text_fg).place(x=117, y=40)
        self.cpf_funcionarioEntry = ttk.Entry(self.root, width=30)
        self.cpf_funcionarioEntry.place(x=150, y=40)

        Label(self.root, text="Nome:", bg="#002333", fg=text_fg).place(x=105, y=75)
        self.nome_funcionarioEntry = ttk.Entry(self.root, width=30)
        self.nome_funcionarioEntry.place(x=150, y=75)

        Label(self.root, text="Telefone:", bg="#002333", fg=text_fg).place(x=92, y=110)
        self.telefoneEntry = ttk.Entry(self.root, width=30)
        self.telefoneEntry.place(x=150, y=110)

        Label(self.root, text="E-mail:", bg="#002333", fg=text_fg).place(x=104, y=145)
        self.emailEntry = ttk.Entry(self.root, width=30)
        self.emailEntry.place(x=150, y=145)

        Label(self.root, text="Data de Contratação:", bg="#002333", fg=text_fg).place(x=30, y=180)
        self.data_da_contratacaoEntry = ttk.Entry(self.root, width=30)
        self.data_da_contratacaoEntry.place(x=150, y=180)

        Label(self.root, text="Cargo:", bg="#002333", fg=text_fg).place(x=105, y=215)
        self.cargoEntry = ttk.Entry(self.root, width=30)
        self.cargoEntry.place(x=150, y=215)

        Label(self.root, text="Salário:", bg="#002333", fg=text_fg).place(x=102, y=250)
        self.salarioEntry = ttk.Entry(self.root, width=30)
        self.salarioEntry.place(x=150, y=250)

        Label(self.root, text="Endereço:", bg="#002333", fg=text_fg).place(x=88, y=285)
        self.enderecoEntry = ttk.Entry(self.root, width=30)
        self.enderecoEntry.place(x=150, y=285)

        excluirButton = ttk.Button(self.root, text="EXCLUIR", width=15, command=self.excluirFuncionario)
        excluirButton.place(x=235, y=320)

        alterarButton = ttk.Button(self.root, text="ALTERAR", width=15, command=self.alterarfuncionario)
        alterarButton.place(x=80, y=360)

        BuscarButton = ttk.Button(self.root, text="BUSCAR", width=15, command=self.buscarfuncionario)
        BuscarButton.place(x=500, y=80)

        limparButton = ttk.Button(self.root, text="lIMPAR", width=15, command=self.LimparCampos)
        limparButton.place(x=235, y=360)

        CadastrarButton = ttk.Button(self.root, text="CADASTRAR", width=15, command=self.conect_banco_funcionario)
        CadastrarButton.place(x=80, y=320)

        Button(self.main_frame, text="VOLTAR AO MENU", width=15, command=self.juntar_funcoes).place(x=650, y=80)

    def enviar_email_confirmacao(self, destinatario, nome_funcionario):
        try:
            msg = EmailMessage()
            msg['Subject'] = 'Cadastro Realizado com Sucesso'
            msg['From'] = 'gustavowendt14@gmail.com'  
            msg['To'] = destinatario
            msg.set_content(f"""
Olá {nome_funcionario},

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

    def conect_banco_funcionario(self):
        cpf = self.cpf_funcionarioEntry.get()
        nome = self.nome_funcionarioEntry.get()
        telefone = self.telefoneEntry.get()
        email = self.emailEntry.get()
        dataDeContratacao = self.data_da_contratacaoEntry.get()
        cargo = self.cargoEntry.get()
        salario = self.salarioEntry.get()
        endereco = self.enderecoEntry.get()

        if cpf == "" or nome == "" or telefone == "" or email == "" or dataDeContratacao == "" or cargo == "" or salario == "" or endereco == "":
            messagebox.showerror(title="Erro de cadastro!", message="Todos os campos devem estar preenchidos!")
        else:
            db = Database()
            db.RegistrarNoBancofuncionario(cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco)
            messagebox.showinfo("Sucesso", "Funcionário(a) cadastrado(a) com sucesso!")
            self.enviar_email_confirmacao(email, nome)

    def excluirFuncionario(self):
        idfuncionario = self.ID_funcionarioEntry.get()
        if idfuncionario == "":
            messagebox.showerror(title="Erro de Busca", message="PREENCHA O CAMPO DE ID")
        else:
            db = Database()
            db.removerfuncionario(idfuncionario)
            messagebox.showinfo("Sucesso", "Funcionário excluído com sucesso!")

    def alterarfuncionario(self):
        idfuncionario = self.ID_funcionarioEntry.get()
        cpf = self.cpf_funcionarioEntry.get()
        nome = self.nome_funcionarioEntry.get()
        telefone = self.telefoneEntry.get()
        email = self.emailEntry.get()
        dataDeContratacao = self.data_da_contratacaoEntry.get()
        cargo = self.cargoEntry.get()
        salario = self.salarioEntry.get()
        endereco = self.enderecoEntry.get()

        if idfuncionario == "" or cpf == "" or nome == "" or telefone == "" or email == "" or dataDeContratacao == "" or cargo == "" or salario == "" or endereco == "":
            messagebox.showerror(title="Erro!", message="Todos os campos devem estar preenchidos!")
        else:
            db = Database()
            db.alterarfuncionario(idfuncionario, cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco)
            messagebox.showinfo("Sucesso", "Funcionário(a) alterado(a) com sucesso!")

    def buscarfuncionario(self):
        idfuncionario = self.ID_funcionarioEntry.get()
        if idfuncionario == "":
            messagebox.showerror(title="Erro", message="PREENCHA O CAMPO DE ID")
        else:
            db = Database()
            usuario = db.buscar_funcionario(idfuncionario)
            if usuario:
                self.cpf_funcionarioEntry.delete(0, END)
                self.nome_funcionarioEntry.delete(0, END)
                self.telefoneEntry.delete(0, END)
                self.emailEntry.delete(0, END)
                self.data_da_contratacaoEntry.delete(0, END)
                self.cargoEntry.delete(0, END)
                self.salarioEntry.delete(0, END)
                self.enderecoEntry.delete(0, END)
                self.cpf_funcionarioEntry.insert(0, usuario[1])
                self.nome_funcionarioEntry.insert(0, usuario[2])
                self.telefoneEntry.insert(0, usuario[3])
                self.emailEntry.insert(0, usuario[4])
                self.data_da_contratacaoEntry.insert(0, usuario[5])
                self.cargoEntry.insert(0, usuario[6])
                self.salarioEntry.insert(0, usuario[7])
                self.enderecoEntry.insert(0, usuario[8])
            else:
                messagebox.showerror("Erro", "Funcionário não encontrado")
                self.LimparCampos()

    def LimparCampos(self):
        self.ID_funcionarioEntry.delete(0, END)
        self.cpf_funcionarioEntry.delete(0, END)
        self.nome_funcionarioEntry.delete(0, END)
        self.telefoneEntry.delete(0, END)
        self.emailEntry.delete(0, END)
        self.data_da_contratacaoEntry.delete(0, END)
        self.cargoEntry.delete(0, END)
        self.salarioEntry.delete(0, END)
        self.enderecoEntry.delete(0, END)

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
    jan.title("CADASTRO - Funcionários(a)")
    jan.geometry("800x400")
    jan.configure(background="#002333")
    jan.resizable(width=False, height=False)
    app = TelaGeral(jan)
    logo = PhotoImage(file="icon/_SLA_.png")
    LogoLabel = Label(image=logo, bg="#002333")
    LogoLabel.place(x=480, y=140)
    jan.mainloop()
