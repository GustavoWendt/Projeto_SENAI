from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database

class AbrirProduto_cliente:
    def __init__(self, root):
        self.root = root
        self.root.configure(background="#002333")
        
        # Título
        Cadastrotitulo = Label(root, text="CONSULTA DE PRODUTO | CLIENTE :", 
                              bg="#002333", fg="white", font=("Helvetica", 14, "bold"))
        Cadastrotitulo.place(x=230, y=10)

        # Linha 1
        TipoProdutoLabel = Label(root, text="TIPO DA BATERIA:", bg="#002333", fg="white")
        TipoProdutoLabel.place(x=55, y=50)
        self.TipoProdutoEntry = ttk.Entry(root, width=30)
        self.TipoProdutoEntry.place(x=170, y=50)

        IdProdutoLabel = Label(root, text="ID DO USUARIO:", bg="#002333", fg="white")
        IdProdutoLabel.place(x=400, y=50)
        self.IdProdutoEntry = ttk.Entry(root, width=30)
        self.IdProdutoEntry.place(x=500, y=50)

        # Linha 2
        VoltagemLabel = Label(root, text="VOLTAGEM DA BATERIA:", bg="#002333", fg="white")
        VoltagemLabel.place(x=20, y=90)
        self.VoltagemEntry = ttk.Entry(root, width=30)
        self.VoltagemEntry.place(x=170, y=90)

        self.buscarbotao = Button(root, text="BUSCAR", width=15, command=self.buscarproduto)
        self.buscarbotao.place(x=500, y=90)

        self.limparbotao = Button(root, text="Limpar campos", width=15, command=self.LimparCampos)
        self.limparbotao.place(x=650, y=90)

        self.limparbotao = Button(root, text="Voltar ao menu", width=15, command=self.voltar_menu)
        self.limparbotao.place(x=650, y=150)

        # Linha 3
        MarcaLabel = Label(root, text="MARCA DA BATERIA:", bg="#002333", fg="white")
        MarcaLabel.place(x=40, y=130)
        self.MarcaEntry = ttk.Entry(root, width=30)
        self.MarcaEntry.place(x=170, y=130)

        QuantidadeLabel = Label(root, text="QUANTIDADE DA BATERIA:", bg="#002333", fg="white")
        QuantidadeLabel.place(x=8, y=170)
        self.QuantidadeEntry = ttk.Entry(root, width=30)
        self.QuantidadeEntry.place(x=170, y=170)

        # Linha 4
        PrecoLabel = Label(root, text="PREÇO DA BATERIA:", bg="#002333", fg="white")
        PrecoLabel.place(x=45, y=210)
        self.PrecoEntry = ttk.Entry(root, width=30)
        self.PrecoEntry.place(x=170, y=210)

        DataProdutoLabel = Label(root, text="DATA DE VALIDADE:", bg="#002333", fg="white")
        DataProdutoLabel.place(x=45, y=250)
        self.DataProdutoEntry = ttk.Entry(root, width=30)
        self.DataProdutoEntry.place(x=170, y=250)

    def LimparCampos(self):
        self.TipoProdutoEntry.delete(0, END)
        self.VoltagemEntry.delete(0, END)
        self.MarcaEntry.delete(0, END)
        self.QuantidadeEntry.delete(0, END)
        self.PrecoEntry.delete(0, END)
        self.DataProdutoEntry.delete(0, END)
        self.IdProdutoEntry.delete(0, END)

    def buscarproduto(self):
        idproduto = self.IdProdutoEntry.get()
        if idproduto == "":
            messagebox.showerror(title="Erro", message="PREENCHA O CAMPO DE ID")
        else:
            db = Database()
            usuario = db.buscar_produto(idproduto)
            if usuario:
                self.TipoProdutoEntry.insert(0, usuario[1])
                self.VoltagemEntry.insert(0, usuario[2])
                self.MarcaEntry.insert(0, usuario[3])
                self.QuantidadeEntry.insert(0, usuario[4])
                self.PrecoEntry.insert(0, usuario[5])
                self.DataProdutoEntry.insert(0, usuario[6])
            else:
                messagebox.showerror("Erro", "Produto não encontrado")
                self.LimparCampos()
    def voltar_menu(self):
        self.root.destroy()
        from tela_de_usuario import TeldACASTRO
        root = Tk()
        TeldACASTRO(root)

if __name__ == "__main__":
    root = Tk()
    root.title("USUARIO - PRODUTO - CLIENTE")
    root.geometry("800x400")
    root.configure(background="#002333")
    root.resizable(width=False, height=False)
    app = AbrirProduto_cliente(root)
    root.mainloop()