#Importar as biblotecas
from tkinter import * #IMporta todos os modulos do tkinter
from tkinter import messagebox #importa o modulo de caixas de de mensagens do tkinter 
from tkinter import ttk #Importa a classe Database do modulo DataBase
from DataBase import Database

class Procura_Fornecedor():
    def __init__(self,root):
        self.root = root  # Referência à janela principal

        # Frame principal
        self.main_frame = Frame(self.root, bg="#002333")  # Frame para agrupar widgets
        self.main_frame.pack(expand=True, fill=BOTH)


        tituloLabel = Label(self.main_frame, text="FORNECEDORES | USUARIO :",bg="#002333", fg="white") #Coloca um titulo para a janela
        tituloLabel.place(x=160,y=10)

        infoLabel = Label(self.main_frame, text="Digite o ID do fornecedor para procurar:",bg="#002333", fg="white") #Coloca um titulo para a janela
        infoLabel.place(x=40,y=40)

        alterarLabel = Label(self.main_frame, text="Dados do forncedor procurado:",bg="#002333", fg="white") #Coloca um label
        alterarLabel.place(x=40,y=110)

        idLabel = Label(self.main_frame, text="ID do Fornecedor:",bg="#002333", fg="white") #Cria label do ID
        idLabel.place(x=10,y=80)
        idEntry=ttk.Entry(self.main_frame, width=30) #Cria um campo do ID
        idEntry.place(x=150,y=80)   

        FornecedorLabel = Label(self.main_frame, text="Nome do Fornecedor:",bg="#002333", fg="white") #Cria label do fornecedor
        FornecedorLabel.place(x=10,y=150)
        FornecedorEntry=ttk.Entry(self.main_frame, width=30) #Cria um campo do forncedor
        FornecedorEntry.place(x=150,y=150)   

        CpfFornecedorLabel = Label(self.main_frame, text="CPF do Fornecedor:",bg="#002333", fg="white") #Cria label do Cpf
        CpfFornecedorLabel.place(x=10,y=190)
        CpfFornecedorEntry = ttk.Entry(self.main_frame, width=30) #Cria um campo do cpf
        CpfFornecedorEntry.place(x=150,y=190)

        TelefoneFornecedorLabel = Label(self.main_frame, text="Telefone do fornecedor:",bg="#002333", fg="white") #Cria label do Telefone
        TelefoneFornecedorLabel.place(x=10,y=230)
        TelefoneFornecedorEntry = ttk.Entry(self.main_frame, width=30) #Cria um campo do telefone
        TelefoneFornecedorEntry.place(x=150,y=230)

        EmailFornecedorLabel = Label(self.main_frame, text="Email do Fornecedor:",bg="#002333", fg="white") #Cria label do email
        EmailFornecedorLabel.place(x=10,y=270)
        EmailFornecedorEntry = ttk.Entry(self.main_frame, width=30) #Cria um campo do email
        EmailFornecedorEntry.place(x=150,y=270)

        EnderecoFornecedorLabel = Label(self.main_frame, text="Endereço do Fornecedor:",bg="#002333", fg="white") #Cria label do endereço
        EnderecoFornecedorLabel.place(x=10,y=310)
        EnderecoFornecedorEntry = ttk.Entry(self.main_frame, width=30) #Cria um campo do endereço
        EnderecoFornecedorEntry.place(x=150,y=310)

        ProdutoFornecedorLabel = Label(self.main_frame, text="Produto Fornecido:",bg="#002333", fg="white") #Cria label do produto
        ProdutoFornecedorLabel.place(x=10,y=350)
        ProdutoFornecedorEntry = ttk.Entry(self.main_frame, width=30) #Cria um campo do produto
        ProdutoFornecedorEntry.place(x=150,y=350)

        QuantidadeFornecedorLabel = Label(self.main_frame, text="Quantia de Produto:",bg="#002333", fg="white") #Cria label da quantidade de produto fornecido 
        QuantidadeFornecedorLabel.place(x=10,y=390)
        QuantidadeFornecedorEntry = ttk.Entry(self.main_frame, width=30) #Cria um campo para colocar a quantidade de produto fornecido
        QuantidadeFornecedorEntry.place(x=150,y=390)
        # Botão "Voltar ao Menu" - Ajustando o uso do ttk.Button
        VoltarMenu = ttk.Button(self.root, text="Voltar ao menu", width=15, command=self.juntar_funcoes)
        VoltarMenu.place(x=370,y=150)  # Ajuste a posição conforme necessário
        def LimparCampos():
                    FornecedorEntry.delete(0,END) #Limpa o campo de entrada do fornecedor
                    CpfFornecedorEntry.delete(0,END) #Limpa o campo de entrada do cpf
                    TelefoneFornecedorEntry.delete(0,END) #Limpa o campo de entrada do telefone
                    EmailFornecedorEntry.delete(0,END) #Limpa o campo de entrada do email
                    EnderecoFornecedorEntry.delete(0,END) #Limpa o campo de entrada do endereço
                    ProdutoFornecedorEntry.delete(0,END) #Limpa o campo de entrada do produto
                    QuantidadeFornecedorEntry.delete(0,END) #Limpa o campo de entrada da quantidade de produto
                    idEntry.delete(0,END)
        
        def buscaFornecedor():
            idfornecedor = idEntry.get()
            if idfornecedor == "":
                messagebox.showerror(title="Erro", message="PREENCHA O CAMPO DE ID")
            else:
                db = Database()  # Crie uma instância do banco de dados
                usuario = db.buscar_fornecedor(idfornecedor)  # Supondo que exista um método para buscar por id
                if usuario:
                    FornecedorEntry.delete(0,END) #Limpa o campo de entrada do fornecedor
                    CpfFornecedorEntry.delete(0,END) #Limpa o campo de entrada do cpf
                    TelefoneFornecedorEntry.delete(0,END) #Limpa o campo de entrada do telefone
                    EmailFornecedorEntry.delete(0,END) #Limpa o campo de entrada do email
                    EnderecoFornecedorEntry.delete(0,END) #Limpa o campo de entrada do endereço
                    ProdutoFornecedorEntry.delete(0,END) #Limpa o campo de entrada do produto
                    QuantidadeFornecedorEntry.delete(0,END) #Limpa o campo de entrada da quantidade de produto
                    #Coloca os dados obtidos no campo de texto
                    FornecedorEntry.insert(0, usuario[1])
                    CpfFornecedorEntry.insert(0, usuario[2])
                    TelefoneFornecedorEntry.insert(0, usuario[3])
                    EmailFornecedorEntry.insert(0, usuario[4])
                    EnderecoFornecedorEntry.insert(0, usuario[5])
                    ProdutoFornecedorEntry.insert(0, usuario[6])
                    QuantidadeFornecedorEntry.insert(0, usuario[7])
                    
                else:
                    messagebox.showerror("Erro", "Fornecedor não encontrado")
                    LimparCampos()


        pesquisaButton =  ttk.Button(self.main_frame, text="BUSCAR",width=15,command=buscaFornecedor) #Cria o botão de alterar
        pesquisaButton.place(x=370,y=80)
        limparButton =  ttk.Button(self.main_frame, text="LIMPAR",width=15,command=LimparCampos) #Cria o botão de alterar
        limparButton.place(x=500,y=80)

        limparButton =  ttk.Button(self.main_frame, text="Voltar ao menu",width=15,command=self.voltar_menu) #Cria o botão de alterar
        limparButton.place(x=370,y=150)

        

        # def voltar_menu():
            
        #     jan.quit()
        #     jan.destroy()  # Fecha a tela atual (tela de busca de produto)
        #     root = Tk()  # Cria uma nova instância da janela principal
        #     from tela_usuario import TeldACASTRO  # Importa a tela principal
        #     root.quit
        #     TeldACASTRO(root)  # Chama a tela principal
        #     root.destroy()
        #     root.deiconify()

        # Função que junta as funcionalidades de voltar e limpar
    def voltar_menu(self):
            self.root.destroy()  # Fecha a tela atual (tela de busca de produto)
            root = Tk()  # Cria uma nova instância da janela principal
            from tela_de_usuario import TeldACASTRO  # Importa a tela principal
            TeldACASTRO(root)  # Chama a tela principal

        # Função que junta as funcionalidades de voltar e limpar
    def juntar_funcoes(self):
       
        self.voltar_menu()
  # Volta ao menu e destrói a tela anterior

        # Botões

        # Botão de Voltar ao Menu

    def voltar_menu(self):
        self.root.destroy()
        from tela_de_usuario import TeldACASTRO
        root = Tk()
        TeldACASTRO(root)





if __name__=="__main__":
    root=Tk() # Cria uma instancia da janela principal
    root.title("ADM - Leitor Fornecedor") #Define o titulo da janela
    root .geometry("700x500") #Define o tamanho da janela
    root.configure(background="#002333") #Configura a cor de fundo da janela
    root.resizable(width=False,height=False) #Impede que a janela seja redimensionad
    logo = PhotoImage(file="icon/_SLA_.png") # Carrega a imagem do logo
    LogoLabel = Label(image=logo, bg="#002333") # Cria um label para a imagem do logo
    LogoLabel.place(x=390, y=180) # Posiciona a imagem
    app=Procura_Fornecedor(root)
    root.mainloop()