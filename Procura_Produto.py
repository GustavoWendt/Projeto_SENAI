from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database

class AbrirProduto_cliente:
    def __init__(self, root):
        self.root = root
        self.main_frame = Frame(self.root, bg="#002333")
        self.main_frame.pack(expand=True, fill=BOTH)

        Cadastrotitulo = Label(self.main_frame, text="PROCURA DE PRODUTO | CLIENTE :", bg="#002333", fg="white")
        Cadastrotitulo.place(x=230, y=10)

        # Labels e Entradas
        Label(self.main_frame, text="TIPO DA BATERIA :", bg="#002333", fg="white").place(x=55, y=50)
        self.TipoProdutoEntry = ttk.Entry(self.main_frame, width=30)
        self.TipoProdutoEntry.place(x=170, y=50)

        Label(self.main_frame, text="VOLTAGEM DA BATERIA :", bg="#002333", fg="white").place(x=20, y=90)
        self.VoltagemEntry = ttk.Entry(self.main_frame, width=30)
        self.VoltagemEntry.place(x=170, y=90)

        Label(self.main_frame, text="MARCA DA BATERIA :", bg="#002333", fg="white").place(x=40, y=130)
        self.MarcaEntry = ttk.Entry(self.main_frame, width=30)
        self.MarcaEntry.place(x=170, y=130)

        Label(self.main_frame, text="QUANTIDADE DA BATERIA :", bg="#002333", fg="white").place(x=8, y=170)
        self.QuantidadeEntry = ttk.Entry(self.main_frame, width=30)
        self.QuantidadeEntry.place(x=170, y=170)

        Label(self.main_frame, text="PREÇO DA BATERIA :", bg="#002333", fg="white").place(x=45, y=210)
        self.PrecoEntry = ttk.Entry(self.main_frame, width=30)
        self.PrecoEntry.place(x=170, y=210)

        Label(self.main_frame, text="DATA DE VALIDADE :", bg="#002333", fg="white").place(x=45, y=250)
        self.DataProdutoEntry = ttk.Entry(self.main_frame, width=30)
        self.DataProdutoEntry.place(x=170, y=250)

        Label(self.main_frame, text="ID DO USUARIO :", bg="#002333", fg="white").place(x=400, y=50)
        self.IdProdutoEntry = ttk.Entry(self.main_frame, width=30)
        self.IdProdutoEntry.place(x=500, y=50)

        # Label da ComboBox
        Label(self.main_frame, text="Fornecedor:", bg="#002333", fg="white").place(x=400, y=130)

        # Buscar os fornecedores do banco
        db = Database()
        fornecedores = db.buscar_nome_fornecedor()

        # Cria a ComboBox de fornecedores
        self.combo_box_forn = ttk.Combobox(self.main_frame, values=fornecedores, state="readonly", width=27)
        self.combo_box_forn.place(x=500, y=130)
        self.combo_box_forn.set("Selecione um fornecedor")

        def buscarproduto():
            idproduto = self.IdProdutoEntry.get()
            if idproduto == "":
                messagebox.showerror(title="Erro", message="PREENCHA O CAMPO DE ID")
            else:
                db = Database()
                usuario = db.buscar_produto(idproduto)
                if usuario:
                    self.TipoProdutoEntry.delete(0, END)
                    self.VoltagemEntry.delete(0, END)
                    self.MarcaEntry.delete(0, END)
                    self.QuantidadeEntry.delete(0, END)
                    self.PrecoEntry.delete(0, END)
                    self.DataProdutoEntry.delete(0, END)
                    # Assumindo que a consulta retorna os campos na seguinte ordem:
                    # produto: [tipo, voltagem, marca, quantidade, preco, data, idfornecedor]
                    # fornecedor: [nome_fornecedor]
                    tipo_produto = usuario[2]  # Produto: tipo
                    voltagem = usuario[3]  # Produto: voltagem
                    marca = usuario[4]  # Produto: marca
                    quantidade = usuario[5]  # Produto: quantidade
                    preco = usuario[6]  # Produto: preco
                    data = usuario[7]  # Produto: data
                     # Fornecedor: idfornecedor
                    nome_fornecedor = usuario[9]  # Fornecedor: nome do fornecedor

                    # Preenchendo os campos com os dados encontrados
                    self.TipoProdutoEntry.insert(0, tipo_produto)
                    self.VoltagemEntry.insert(0, voltagem)
                    self.MarcaEntry.insert(0, marca)
                    self.QuantidadeEntry.insert(0, quantidade)
                    self.PrecoEntry.insert(0, preco)
                    self.DataProdutoEntry.insert(0, data)
                    self.combo_box_forn.set(nome_fornecedor)  # Nome do fornecedor
                else:
                    messagebox.showerror("Erro", "Produto não encontrado")
                    self.LimparCampos()


        # Botões
        Button(self.main_frame, text="LIMPAR",bg="#0078D7", fg="white", activebackground="#0063B1",
                                 activeforeground="white", borderwidth=0, width=15, command=self.LimparCampos).place(x=80, y=300)
        Button(self.main_frame, text="BUSCAR", bg="#0078D7", fg="white", activebackground="#0063B1",
                                 activeforeground="white", borderwidth=0, width=15, command=buscarproduto).place(x=500, y=90)
        Button(self.main_frame, text="VOLTAR AO MENU", bg="#0078D7", fg="white", activebackground="#0063B1",
                                 activeforeground="white", borderwidth=0, width=17, command=self.juntar_funcoes).place(x=650, y=90)

    def LimparCampos(self):
        self.TipoProdutoEntry.delete(0, END)
        self.VoltagemEntry.delete(0, END)
        self.MarcaEntry.delete(0, END)
        self.QuantidadeEntry.delete(0, END)
        self.PrecoEntry.delete(0, END)
        self.DataProdutoEntry.delete(0, END)
        self.IdProdutoEntry.delete(0, END)
        self.combo_box_forn.set("Selecione um fornecedor")

    def voltar_menu(self):
        self.root.destroy()
        from tela_de_usuario import TeldACASTRO
        root = Tk()
        TeldACASTRO(root)

    def juntar_funcoes(self):
        self.LimparCampos()
        self.voltar_menu()

if __name__ == "__main__":
    jan = Tk()
    jan.title("USUARIO - PRODUTO")
    jan.geometry("800x400")
    jan.configure(background="#002333")
    jan.resizable(width=False, height=False)
    app = AbrirProduto_cliente(jan)
    logo = PhotoImage(file="icon/_SLA_.png") # Carrega a imagem do logo
    LogoLabel = Label(image=logo, bg="#002333") # Cria um label para a imagem do logo
    LogoLabel.place(x=480, y=180) # Posiciona o label no frame esquerdo
    jan.mainloop()
