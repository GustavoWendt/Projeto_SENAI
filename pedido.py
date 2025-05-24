from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database

class AbrirPedido_adm:
    def __init__(self, root):
        self.root = root
        self.root.title("USUÁRIO - PRODUTO")
        self.root.geometry("800x400")
        self.root.configure(background="#002333")
        self.root.resizable(width=False, height=False)

        self.main_frame = Frame(self.root, bg="#002333")
        self.main_frame.pack(expand=True, fill=BOTH)

        # Widgets da interface
        Cadastrotitulo = Label(self.main_frame, text="COMPRA DE PRODUTO | ADM :", bg="#002333", fg="white")
        Cadastrotitulo.place(x=230, y=10)

        # Labels
        Label(self.main_frame, text="CLIENTE :", bg="#002333", fg="white").place(x=20, y=50)
        Label(self.main_frame, text="PRODUTO :", bg="#002333", fg="white").place(x=20, y=100)
        Label(self.main_frame, text="FUNCIONÁRIO :", bg="#002333", fg="white").place(x=20, y=150)
        Label(self.main_frame, text="QUANTIDADE :", bg="#002333", fg="white").place(x=20, y=250)
        Label(self.main_frame, text="ID DA COMPRA :", bg="#002333", fg="white").place(x=400, y=50)
        Label(self.main_frame, text="FORNECEDOR :", bg="#002333", fg="white").place(x=20, y=200)

        # Entradas
        self.QtdeEntry = ttk.Entry(self.main_frame, width=30)
        self.QtdeEntry.place(x=120, y=250)

        self.IdProdutoEntry = ttk.Entry(self.main_frame, width=30)
        self.IdProdutoEntry.place(x=500, y=50)

        # Instancia o banco e atualiza os comboboxes
        self.db = Database()
        self.atualizar_comboboxes()

        # Botões
        Button(self.main_frame, text="CADASTRAR", width=15, command=self.RegistrarNoBanco_Pedido).place(x=80, y=300)
        Button(self.main_frame, text="LIMPAR", width=15, command=self.LimparCampos).place(x=250, y=300)
        Button(self.main_frame, text="ALTERAR", width=15, command=self.alterarproduto).place(x=80, y=340)
        Button(self.main_frame, text="EXCLUIR", width=15, command=self.excluirproduto).place(x=250, y=340)
        Button(self.main_frame, text="BUSCAR", width=15, command=self.buscarproduto).place(x=500, y=90)
        Button(self.main_frame, text="VOLTAR AO MENU", width=15, command=self.juntar_funcoes).place(x=650, y=90)

        # Logo
        try:
            self.logo = PhotoImage(file="icon/_SLA_.png")
            LogoLabel = Label(self.main_frame, image=self.logo, bg="#002333")
            LogoLabel.place(x=480, y=180)
        except Exception as e:
            print("Erro ao carregar a logo:", e)

    def atualizar_comboboxes(self):
        fornecedores = self.db.buscar_nome_fornecedor()
        produto = self.db.buscar_nome_produto()
        cliente = self.db.buscar_nome_cliente()
        funcionario = self.db.buscar_nome_funcionario()

        self.combo_box_forn = ttk.Combobox(self.main_frame, values=fornecedores, state="readonly", width=27)
        self.combo_box_forn.place(x=110, y=200)
        self.combo_box_forn.set("Selecione um fornecedor")

        self.combo_box_prod = ttk.Combobox(self.main_frame, values=produto, state="readonly", width=40)
        self.combo_box_prod.place(x=100, y=100)
        self.combo_box_prod.set("Selecione um produto")

        self.combo_box_cliente = ttk.Combobox(self.main_frame, values=cliente, state="readonly", width=27)
        self.combo_box_cliente.place(x=80, y=50)
        self.combo_box_cliente.set("Selecione um cliente")

        self.combo_box_func = ttk.Combobox(self.main_frame, values=funcionario, state="readonly", width=27)
        self.combo_box_func.place(x=120, y=150)
        self.combo_box_func.set("Selecione um funcionário")

    def buscarproduto(self):
        id_pedido = self.IdProdutoEntry.get()

        if not id_pedido:
            messagebox.showerror("Erro", "Por favor, insira um ID para buscar.")
            return

        try:
            dados = self.db.buscar_pedido_por_id(id_pedido)

            if not dados:
                messagebox.showinfo("Informação", "Nenhum pedido encontrado com este ID.")
                return

            self.combo_box_cliente.set(self.formatar_combobox(dados[1], dados[0]))
            self.combo_box_prod.set(self.formatar_combobox(dados[3], dados[2]))
            self.combo_box_func.set(self.formatar_combobox(dados[5], dados[4]))
            self.combo_box_forn.set(self.formatar_combobox(dados[7], dados[6]))

            self.QtdeEntry.delete(0, END)
            self.QtdeEntry.insert(0, str(dados[8]))

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar pedido: {str(e)}")

    def formatar_combobox(self, nome, id_item):
        return f"{nome} (ID: {id_item})"

    def extrair_id_combobox(self, texto_combobox):
        try:
            inicio = texto_combobox.find("(ID: ") + 5
            fim = texto_combobox.find(")", inicio)
            if inicio > 4 and fim > inicio:
                return int(texto_combobox[inicio:fim])
            return None
        except:
            return None

    def alterarproduto(self):
        id_pedido = self.IdProdutoEntry.get()
        cliente = self.combo_box_cliente.get()
        produto = self.combo_box_prod.get()
        funcionario = self.combo_box_func.get()
        quantidade = self.QtdeEntry.get()
        fornecedor = self.combo_box_forn.get()

        if "" in [id_pedido, cliente, produto, funcionario, quantidade, fornecedor]:
            messagebox.showerror("Erro no Registro", "PREENCHA TODOS OS CAMPOS")
            return

        cod_cliente = self.extrair_id_combobox(cliente)
        cod_produto = self.extrair_id_combobox(produto)
        cod_funcionario = self.extrair_id_combobox(funcionario)
        cod_fornecedor = self.extrair_id_combobox(fornecedor)

        if None in [cod_cliente, cod_produto, cod_funcionario, cod_fornecedor]:
            messagebox.showerror("Erro", "Um ou mais campos possuem valores inválidos.")
            return

        try:
            self.db.alterar_pedido(id_pedido, cod_cliente, cod_produto, cod_funcionario, quantidade, cod_fornecedor)
            messagebox.showinfo("Sucesso", "Pedido alterado com sucesso!")
            self.LimparCampos()
            self.atualizar_comboboxes()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao alterar pedido: {str(e)}")

    def excluirproduto(self):
        id_pedido = self.IdProdutoEntry.get()

        if not id_pedido:
            messagebox.showerror("Erro", "Por favor, insira um ID para excluir.")
            return

        if messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este pedido?"):
            try:
                self.db.excluir_pedido(id_pedido)
                messagebox.showinfo("Sucesso", "Pedido excluído com sucesso!")
                self.LimparCampos()
                self.atualizar_comboboxes()
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao excluir pedido: {str(e)}")

    def RegistrarNoBanco_Pedido(self):
        cliente = self.combo_box_cliente.get()
        produto = self.combo_box_prod.get()
        funcionario = self.combo_box_func.get()
        quantidade = self.QtdeEntry.get()
        fornecedor = self.combo_box_forn.get()

        if "" in [cliente, produto, funcionario, quantidade, fornecedor]:
            messagebox.showerror(title="Erro no Registro", message="PREENCHA TODOS OS CAMPOS")
            return

        def extrair_id(texto):
            partes = texto.split()
            for parte in reversed(partes):
                if parte.isdigit():
                    return int(parte)
            return None

        cod_cliente = extrair_id(cliente)
        cod_produto = extrair_id(produto)
        cod_funcionario = extrair_id(funcionario)
        cod_fornecedor = extrair_id(fornecedor)

        if None in [cod_cliente, cod_produto, cod_funcionario, cod_fornecedor]:
            messagebox.showerror("Erro", "Um ou mais campos possuem valores inválidos.")
            return

        db = Database()
        db.RegistrarNoBanco_Pedido(cod_cliente, cod_produto, cod_funcionario, quantidade, cod_fornecedor)
        messagebox.showinfo("Sucesso", "Pedido registrado com sucesso!")
        self.LimparCampos()

    def LimparCampos(self):
        self.IdProdutoEntry.delete(0, END)
        self.QtdeEntry.delete(0, END)
        self.combo_box_forn.set("Selecione um fornecedor")
        self.combo_box_prod.set("Selecione um produto")
        self.combo_box_cliente.set("Selecione um cliente")
        self.combo_box_func.set("Selecione um funcionário")

    def voltar_menu(self):
        self.root.destroy()
        from tela_ADM import TeldACASTRO
        novo_root = Tk()
        TeldACASTRO(novo_root)

    def juntar_funcoes(self):
        self.LimparCampos()
        self.voltar_menu()

if __name__ == "__main__":
    jan = Tk()
    app = AbrirPedido_adm(jan)
    jan.mainloop()
