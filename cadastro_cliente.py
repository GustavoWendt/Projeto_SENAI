from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database

class Abrir_Cliente:
    def __init__(self, root):
        self.root = root
        self.root.title("ADM - Clientes")
        self.root.geometry("800x400")
        self.root.configure(bg="#002333")
        self.root.resizable(width=False, height=False)

        try:
            self.logo = PhotoImage(file="icon/_SLA_.png")
            LogoLabel = Label(self.root, image=self.logo, bg="#002333")
            LogoLabel.place(x=440, y=180)
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")

        self.criar_widgets()

    def criar_widgets(self):
        Label(self.root, text="CADASTRO DE CLIENTE | ADM:", bg="#002333", fg="white", font=("Arial", 14)).place(x=160, y=10)

        Label(self.root, text="Nome do Cliente:", bg="#002333", fg="white").place(x=10, y=80)
        self.ClienteEntry = ttk.Entry(self.root, width=30)
        self.ClienteEntry.place(x=150, y=80)

        Label(self.root, text="CPF do Cliente:", bg="#002333", fg="white").place(x=10, y=120)
        self.CpfClienteEntry = ttk.Entry(self.root, width=30)
        self.CpfClienteEntry.place(x=150, y=120)

        Label(self.root, text="Telefone do Cliente:", bg="#002333", fg="white").place(x=10, y=160)
        self.TelefoneClienteEntry = ttk.Entry(self.root, width=30)
        self.TelefoneClienteEntry.place(x=150, y=160)

        Label(self.root, text="Endereço do Cliente:", bg="#002333", fg="white").place(x=10, y=200)
        self.EnderecoClienteEntry = ttk.Entry(self.root, width=30)
        self.EnderecoClienteEntry.place(x=150, y=200)

        Label(self.root, text="ID do Cliente :", bg="#002333", fg="white").place(x=420, y=80)
        self.idclienteEntry = ttk.Entry(self.root, width=10)
        self.idclienteEntry.place(x=500, y=80)

        # Botões do CRUD
        ttk.Button(self.root, text="Cadastrar", width=15, command=self.registrar_cliente).place(x=50, y=250)
        ttk.Button(self.root, text="Buscar", width=15, command=self.buscar_cliente).place(x=440, y=120)
        ttk.Button(self.root, text="Alterar", width=15, command=self.alterar_cliente).place(x=200, y=300)
        ttk.Button(self.root, text="Excluir", width=15, command=self.excluir_cliente).place(x=50, y=300)
        ttk.Button(self.root, text="Limpar", width=15, command=self.limpar_campos).place(x=200, y=250)
        ttk.Button(self.root, text="Voltar ao menu", width=15, command=self.voltar_menu).place(x=580, y=120)

    def registrar_cliente(self):
        nome = self.ClienteEntry.get()
        cpf = self.CpfClienteEntry.get()
        telefone = self.TelefoneClienteEntry.get()
        endereco = self.EnderecoClienteEntry.get()
        idcliente = self.idclienteEntry.get()

        if "" in [nome, cpf, telefone, endereco, idcliente]:
            messagebox.showerror("Erro", "PREENCHA TODOS OS CAMPOS")
        else:
            db = Database()
            db.RegistrarNoBancoCliente(nome, cpf, telefone, endereco, idcliente)
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            self.limpar_campos()

    def buscar_cliente(self):
        idcliente = self.idclienteEntry.get()
        if idcliente == "":
            messagebox.showerror("Erro", "PREENCHA O CAMPO DE ID")
        else:
            db = Database()
            usuario = db.buscar_cliente(idcliente)
            if usuario:
                self.ClienteEntry.delete(0, END)
                self.CpfClienteEntry.delete(0, END)
                self.TelefoneClienteEntry.delete(0, END)
                self.EnderecoClienteEntry.delete(0, END)
                self.idclienteEntry.delete(0, END)

                self.ClienteEntry.insert(0, usuario[1])
                self.CpfClienteEntry.insert(0, usuario[2])
                self.TelefoneClienteEntry.insert(0, usuario[3])
                self.EnderecoClienteEntry.insert(0, usuario[4])
                self.idclienteEntry.insert(0, usuario[0])  # ID costuma estar na posição 0
            else:
                messagebox.showerror("Erro", "Cliente não encontrado")
                self.limpar_campos()

    def alterar_cliente(self):
        nome = self.ClienteEntry.get()
        cpf = self.CpfClienteEntry.get()
        telefone = self.TelefoneClienteEntry.get()
        endereco = self.EnderecoClienteEntry.get()
        idcliente = self.idclienteEntry.get()

        if "" in [nome, cpf, telefone, endereco, idcliente]:
            messagebox.showerror("Erro", "PREENCHA TODOS OS CAMPOS")
        else:
            db = Database()
            db.alterarCliente(nome, cpf, telefone, endereco, idcliente)
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
            self.limpar_campos()

    def excluir_cliente(self):
        idcliente = self.idclienteEntry.get()
        if idcliente == "":
            messagebox.showerror("Erro", "Informe o ID para exclusão")
        else:
            confirm = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir?")
            if confirm:
                db = Database()
                db.excluirCliente(idcliente)
                messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
                self.limpar_campos()

    def limpar_campos(self):
        self.ClienteEntry.delete(0, END)
        self.CpfClienteEntry.delete(0, END)
        self.TelefoneClienteEntry.delete(0, END)
        self.EnderecoClienteEntry.delete(0, END)
        self.idclienteEntry.delete(0, END)

    def voltar_menu(self):
        self.root.destroy()
        from tela_ADM import TeldACASTRO
        root = Tk()
        TeldACASTRO(root)

# Execução
if __name__ == "__main__":
    root = Tk()
    app = Abrir_Cliente(root)
    root.mainloop()
