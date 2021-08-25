from Janelas.estiloWidgets.widgets_Glac import *
from funcs.backCads.backCadProduto import *


class Produtos(CadProdutos):
    def cadprod(self):
        self.janelaProd = Toplevel()
        self.janelaProd.title(self.m_Produtos)
        self.janelaProd.geometry("860x240+65+180")
        self.janelaProd.configure(background="gray30")
        self.janelaProd.resizable(FALSE, FALSE)
        self.janelaProd.transient(self.janela)
        self.janelaProd.focus_force()
        self.janelaProd.grab_set()

        frame_gradiente = GradientFrame(self.janelaProd)
        frame_gradiente.place(relx=0, rely=0, relwidth=1, relheight=1)

        descrCodprod = LabelGlac(self.janelaProd, self.m_Codigo)
        descrCodprod.place(x=2, y=5, width=80, height=25)

        self.entradaCodprod = Entry(self.janelaProd, bd=1, bg='gray25',
            fg='gray70', font=('Calibri', 10, 'bold'))
        self.entradaCodprod.place(x=80, y=5, width=60, height=25)

        descrProd = LabelGlac(self.janelaProd, self.m_Produtos)
        descrProd.place(x=2, y=33, width=80, height=25)

        self.entradaProd = Entry(self.janelaProd, bd=1, bg='gray25',
            fg='gray70', font=('Calibri', 10, 'bold'))
        self.entradaProd.place(x=80, y=33, width=200, height=25)

        botaoAdd = ButtonGlac(self.janelaProd, self.m_Carregar, self.carrega_produtoP)
        botaoAdd.place(x=150, y=2, width=115, height=31)

        botaolimpa = ButtonGlac(self.janelaProd, self.m_Limpar, self.limpa_produtoP)
        botaolimpa.place(x=285, y=2, width=70, height=31)

        botaolimpa = ButtonGlac(self.janelaProd, self.m_Buscar, self.busca_produtoP)
        botaolimpa.place(x=285, y=32, width=70, height=30)

        descrIdMarcaprod = ButtonGlac(self.janelaProd, self.m_Marca, self.busca_marcaP)
        descrIdMarcaprod.place(x=2, y=60, width=100, height=30)

        self.entradaIdMarcaprod = Entry(self.janelaProd)

        self.entradaMarcaprod = Entry(self.janelaProd, bd=1, bg='gray25',
            fg='gray70', font=('Calibri', 10, 'bold'))
        self.entradaMarcaprod.place(x=105, y=62, width=250, height=25)

        descrIdFornec = ButtonGlac(self.janelaProd, self.m_Fornecedor, self.busca_fornecP)
        descrIdFornec.place(x=2, y=90, width=100, height=30)

        self.entradaIdFornec = Entry(self.janelaProd)

        self.entradaFornec = Entry(self.janelaProd, bd=1, bg='gray25',
            fg='gray70', font=('Calibri', 10, 'bold'))
        self.entradaFornec.place(x=105, y=93, width=250, height=25)

        self.descrCusto = LabelGlac(self.janelaProd, self.m_Custo_R)
        self.descrCusto.place(x=2, y=122, width=80, height=25)

        self.entradaCusto = Entry(self.janelaProd, bd=1, bg='gray25',
            fg='gray70', font=('Calibri', 10, 'bold'))
        self.entradaCusto.configure(validate="key", validatecommand=self.vcmd8float)
        self.entradaCusto.place(x=83, y=122, width=80, height=25)

        descrValor = LabelGlac(self.janelaProd, self.m_Valor_R)
        descrValor.place(x=170, y=122, width=80, height=25)

        self.entradaValor = Entry(self.janelaProd, bd=1, bg='gray25',
            fg='gray70', font=('Calibri', 10, 'bold'))
        self.entradaValor.configure(validate="key", validatecommand=self.vcmd8float)
        self.entradaValor.place(x=250, y=123, width=80, height=25)

        descrDescricao = LabelGlac(self.janelaProd, self.m_Descricao)
        descrDescricao.place(x=2, y=150, width=80, height=25)

        self.entradaDescricao = Entry(self.janelaProd, bd=1, bg='gray25',
            fg='gray70', font=('Calibri', 10, 'bold'))
        self.entradaDescricao.place(x=83, y=153, width=250, height=25)

        botaoAdd = ButtonGlac(self.janelaProd, self.m_Novo, self.add_produtoP)
        botaoAdd.place(x=50, y=190, width=80, height=35)

        botaoMudServ = ButtonGlac(self.janelaProd, self.m_Alterar, self.mud_produtoP)
        botaoMudServ.place(x=150, y=190, width=80, height=35)

        botaoDel = ButtonGlac(self.janelaProd, self.m_Apagar, self.del_produtoP)
        botaoDel.place(x=250, y=190, width=80, height=35)

        ### Widgets - Listar produtos ###
        self.listaServ = ttk.Treeview(self.janelaProd,
            height=10, column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaServ.heading("#0", text="")
        self.listaServ.column("#0", width=0)
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.column("#1", width=60)
        self.listaServ.heading("#2", text=self.m_Produtos)
        self.listaServ.column("#2", width=220)
        self.listaServ.heading("#3", text="")
        self.listaServ.column("#3", width=25)
        self.listaServ.heading("#4", text=self.m_Custo_R)
        self.listaServ.column("#4", width=70)
        self.listaServ.heading("#5", text="")
        self.listaServ.column("#5", width=25)
        self.listaServ.heading("#6", text=self.m_Valor_R)
        self.listaServ.column("#6", width=80)

        self.conecta_Glac()

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.janelaProd, orient='vertical', command=self.listaServ.yview)
        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=840, y=5, height=220)

        lista = self.cursor.execute("""SELECT cod_sp, servprod, "R$", custo, "R$", valor 
            FROM servprod WHERE sp = "P" ORDER BY servprod ASC ; """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.listaServ.place(x=360, y=5)
        self.listaServ.bind("<Double-1>", self.OnDoubleClickP)
        self.desconecta_Glac()
        self.janelaProd.mainloop()
