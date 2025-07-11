from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database

class AbrirProduto_adm:
    def __init__(self, root):
        self.root = root
        self.main_frame = Frame(self.root, bg="#002333")
        self.main_frame.pack(expand=True, fill=BOTH)

        Cadastrotitulo = Label(self.main_frame, text="CADASTRO DE PRODUTO | ADM :", bg="#002333", fg="white")
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

        Label(self.main_frame, text="Digite a quantidade que quer sub/somar :", bg="#002333", fg="white").place(x=30, y=400)
        self.ManipularEntry = ttk.Entry(self.main_frame, width=30)
        self.ManipularEntry.place(x=250, y=400)

        Label(self.main_frame, text="Fornecedor:", bg="#002333", fg="white").place(x=400, y=130)
        db = Database()
        fornecedores = db.buscar_nome_fornecedor()
        self.combo_box_forn = ttk.Combobox(self.main_frame, values=fornecedores, state="readonly", width=27)
        self.combo_box_forn.place(x=500, y=130)
        self.combo_box_forn.set("Selecione um fornecedor")

        # Botões
        Button(self.main_frame, text="CADASTRAR", width=15, command=self.RegistrarNoBanco_Produto).place(x=80, y=300)
        Button(self.main_frame, text="LIMPAR", width=15, command=self.LimparCampos).place(x=250, y=300)
        Button(self.main_frame, text="ALTERAR", width=15, command=self.alterarproduto).place(x=80, y=340)
        Button(self.main_frame, text="EXCLUIR", width=15, command=self.excluirproduto).place(x=250, y=340)
        Button(self.main_frame, text="BUSCAR", width=15, command=self.buscarproduto).place(x=500, y=90)
        Button(self.main_frame, text="Voltar ao menu", width=15, command=self.juntar_funcoes).place(x=650, y=90)
        Button(self.main_frame, text="Acresentar", width=15, command=self.acresentar).place(x=230, y=450)
        Button(self.main_frame, text="Reduzir", width=15, command=self.reduzir).place(x=350, y=450)

    def atualizar_quantidade(self, nova_quantidade):
        idproduto = self.IdProdutoEntry.get()
        if idproduto == "":
            messagebox.showerror("Erro", "Informe o ID do produto.")
            return

        try:
            db = Database()
            db.alterar_quantidade_produto(idproduto, nova_quantidade)
            messagebox.showinfo("Sucesso", "Quantidade atualizada com sucesso!")
            self.QuantidadeEntry.delete(0, END)
            self.QuantidadeEntry.insert(0, str(nova_quantidade))
            self.ManipularEntry.delete(0, END)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar quantidade: {str(e)}")

    def acresentar(self):
        try:
            atual = int(self.QuantidadeEntry.get())
            adicionar = int(self.ManipularEntry.get())
            nova_qtde = atual + adicionar
            self.atualizar_quantidade(nova_qtde)
        except ValueError:
            messagebox.showerror("Erro", "Os campos devem conter números inteiros.")

    def reduzir(self):
        try:
            atual = int(self.QuantidadeEntry.get())
            reduzir = int(self.ManipularEntry.get())

            if reduzir > atual:
                messagebox.showerror("Erro", "Não é possível reduzir mais do que o estoque atual.")
                return

            nova_qtde = atual - reduzir
            self.atualizar_quantidade(nova_qtde)
        except ValueError:
            messagebox.showerror("Erro", "Os campos devem conter números inteiros.")


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

        def alterarproduto():
            idproduto = self.IdProdutoEntry.get()
            tipo = self.TipoProdutoEntry.get()
            voltagem = self.VoltagemEntry.get()
            marca = self.MarcaEntry.get()
            quantidade = self.QuantidadeEntry.get()
            preco = self.PrecoEntry.get()
            data = self.DataProdutoEntry.get()
            fornecedor = self.combo_box_forn.get()

            # Dividir a string por espaços
            partes = fornecedor.split()

            # Separar o número e o texto
            numeros = [parte for parte in partes if parte.isdigit()]
            texto_sem_numeros = " ".join([parte for parte in partes if not parte.isdigit()])

            # Exibir os resultados
            print("Números encontrados:", numeros)
            print("Texto sem números:", texto_sem_numeros)

            cod_fornecedor = numeros[0]


            if "" in [idproduto, tipo, voltagem, marca, quantidade, preco, data,cod_fornecedor]:
                messagebox.showerror(title="Erro de Atualização", message="PREENCHA TODOS OS CAMPOS")
            else:
                db = Database()
                db.alterarproduto(idproduto, tipo, voltagem, marca, quantidade, preco, data,cod_fornecedor)
                messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")

        def excluirproduto():
            idproduto = self.IdProdutoEntry.get()
            if idproduto == "":
                messagebox.showerror(title="Erro de Busca", message="PREENCHA O CAMPO DE ID")
            else:
                db = Database()
                db.removerproduto(idproduto)
                messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")

        '''def alterarfuncionario(self):
            idfuncionario = self.ID_funcionarioEntry.get()
            cpf = self.cpf_funcionarioEntry.get()
            nome = self.nome_funcionarioEntry.get()
            telefone = self.telefoneEntry.get()
            email = self.emailEntry.get()
            dataDeContratacao = self.data_da_contratacaoEntry.get()
            cargo = self.cargoEntry.get()
            salario = self.salarioEntry.get()
            endereco = self.enderecoEntry.get()
            
            # Verifica se todos os campos estão preenchidos
            if  idfuncionario == "" or cpf == "" or nome == "" or telefone == "" or email == "" or dataDeContratacao == "" or cargo == "" or salario == "" or endereco == "":
                messagebox.showerror(title="Erro!", message="Todos os campos devem estar preenchidos!")
            else:
                db = Database()  # Cria uma instância do banco de dados
                db.alterarfuncionario(idfuncionario, cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco)  # Registra os dados
                messagebox.showinfo("Sucesso", "Funcionário(a) alterado(a) com sucesso!")'''


        def RegistrarNoBanco_Produto():
            tipo = self.TipoProdutoEntry.get()
            voltagem = self.VoltagemEntry.get()
            marca = self.MarcaEntry.get()
            quantidade = self.QuantidadeEntry.get()
            preco = self.PrecoEntry.get()
            data = self.DataProdutoEntry.get()
            fornecedor = self.combo_box_forn.get()

            if "" in [tipo, voltagem, marca, quantidade, preco, data, fornecedor] or fornecedor == "Selecione um fornecedor":
                messagebox.showerror(title="Erro no Registro", message="PREENCHA TODOS OS CAMPOS")
            else:
                # Extrai o ID do fornecedor da string do Combobox
                partes = fornecedor.split()
                numeros = [parte for parte in partes if parte.isdigit()]
                
                if not numeros:
                    messagebox.showerror("Erro", "Fornecedor inválido selecionado")
                    return
                    
                cod_fornecedor = numeros[0]
                
                db = Database()
                db.RegistrarNoBanco_Produto(tipo, voltagem, marca, quantidade, preco, data, cod_fornecedor)
                messagebox.showinfo("Sucesso", "Produto registrado com sucesso!")
                self.LimparCampos()

        # Botões
        Button(self.main_frame, text="CADASTRAR", width=15, command=RegistrarNoBanco_Produto).place(x=80, y=300)
        Button(self.main_frame, text="LIMPAR", width=15, command=self.LimparCampos).place(x=250, y=300)
        Button(self.main_frame, text="ALTERAR", width=15, command=alterarproduto).place(x=80, y=340)
        Button(self.main_frame, text="EXCLUIR", width=15, command=excluirproduto).place(x=250, y=340)
        Button(self.main_frame, text="BUSCAR", width=15, command=buscarproduto).place(x=500, y=90)
        Button(self.main_frame, text="Voltar ao menu", width=15, command=self.juntar_funcoes).place(x=650, y=90)

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
        from tela_ADM import TeldACASTRO
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
    app = AbrirProduto_adm(jan)
    logo = PhotoImage(file="icon/_SLA_.png") # Carrega a imagem do logo
    LogoLabel = Label(image=logo, bg="#002333") # Cria um label para a imagem do logo
    LogoLabel.place(x=480, y=180) # Posiciona o label no frame esquerdo
    jan.mainloop()
