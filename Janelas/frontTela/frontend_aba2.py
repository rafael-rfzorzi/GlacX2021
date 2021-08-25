from Janelas.estiloWidgets.widgets_Glac import *
from tkinter import ttk

class Aba2:
    def aba2(self):
        # Label Servicos Peças
        descrCol2 = LabelGlac(self.frame_aba2, 'Serviços / Produtos')
        descrCol2.configure(bg='gray20')
        descrCol2.place(relx=0.07, rely=0.02, relwidth=0.455, relheight=0.09)

        # Label codigo
        descrCodI = LabelGlac(self.frame_aba2, 'Código')
        descrCodI.configure(bg='gray20')
        descrCodI.place(relx=0.57, rely=0.02, relwidth=0.05, relheight=0.09)

        # Label Valor
        descrCol3 = LabelGlac(self.frame_aba2, self.m_ValorUnit)
        descrCol3.configure(bg='gray20')
        descrCol3.place(relx=0.66, rely=0.02, relwidth=0.09, relheight=0.09)

        # Quantidade
        descrQuant = ButtonGlac(self.frame_aba2, self.m_Quant, self.altera_itens_orc_quant2)
        descrQuant.place(relx=0.76, rely=0.01, relwidth=0.08, relheight=0.11)

        # Total Item
        descrTotalItem = LabelGlac(self.frame_aba2, self.m_Total + ' ' + self.m_Item)
        descrTotalItem.place(relx=0.85, rely=0.02, relwidth=0.12, relheight=0.09)

        # Widgets - Listar item 1 ###
        self.listaCol2a = AutocompleteEntrySP(self.frame_aba2)
        self.listaCol2a.place(relx=0.07, rely=0.11, relwidth=0.455, relheight=0.1)

        # Botao Busca Item
        botaoBuscaSP1 = Button(self.frame_aba2)
        botaoBuscaSP1.configure(text=u'\u2668', command=self.busca_servico1,
            bg='#385679', fg='#4DA5FF', font=('Arial', '18', 'bold'), activebackground='#6495ED',
            activeforeground="lightgray")
        botaoBuscaSP1.place(relx=0.524, rely=0.11, relwidth=0.04, relheight=0.1)

        # Codigo do Item
        self.codServ1 = Entry(self.frame_aba2)
        self.codServ1.configure(validate="key", justify='center', validatecommand=self.vcmd6)
        self.codServ1.place(relx=0.57, rely=0.11, relwidth=0.05, relheight=0.1)

        botaoAddServicos1 = ButtonGlac(self.frame_aba2, '>', self.add_servico1)
        botaoAddServicos1.place(relx=0.62, rely=0.09, relwidth=0.04, relheight=0.14)

        # Coluna Quantidade
        self.listaCol3a = Entry(self.frame_aba2)
        self.listaCol3a.configure(validate="key", validatecommand=self.vcmd4float,
            justify='center')
        self.listaCol3a.place(relx=0.76, rely=0.11, relwidth=0.08, relheight=0.1)

        # Coluna Valor
        self.listaCol4a = Entry(self.frame_aba2)
        self.listaCol4a.configure(validate="key", justify='right')
        self.listaCol4a.place(relx=0.66, rely=0.11, relwidth=0.09, relheight=0.1)

        # Coluna Total Unitario
        self.listaCol5a = Entry(self.frame_aba2)
        self.listaCol5a.configure(validate="key")
        self.listaCol5a.place(relx=0.85, rely=0.11, relwidth=0.1, relheight=0.1)

        # ADD
        botaoAddServicos2 = ButtonGlac(self.frame_aba2, "Add", self.add_itens_orc)
        botaoAddServicos2.place(relx=0.935, rely=0.1, relwidth=0.05, relheight=0.13)

        self.barraServProd = ttk.Scrollbar(self.frame_aba2, orient='vertical', command=self.OnVsb_Orc2)
        self.listaServProd = ttk.Treeview(self.frame_aba2, height=10, yscrollcommand=self.barraServProd.set,
                column=("col1", "col2", "col3", "col4", "col5", "col6"))

        self.listaServProd.heading("#0", text="")
        self.listaServProd.heading("#1", text=self.m_Item)
        self.listaServProd.heading("#2", text=self.m_Serviços)
        self.listaServProd.heading("#3", text=self.m_Codigo)
        self.listaServProd.heading("#4", text=self.m_Valor)
        self.listaServProd.heading("#5", text=self.m_Quant)
        self.listaServProd.heading("#6", text=self.m_Valor + ' ' + self.m_Total)

        self.listaServProd.column("#0", width=1)
        self.listaServProd.column("#1", width=10)
        self.listaServProd.column("#2", width=450)
        self.listaServProd.column("#3", width=45)
        self.listaServProd.column("#4", width=60)
        self.listaServProd.column("#5", width=45)
        self.listaServProd.column("#6", width=60)

        self.listaServProd.place(relx=0.01, rely=0.24, relwidth=0.96, relheight=0.72)
        self.listaServProd.configure(yscroll=self.barraServProd.set)
        self.barraServProd.place(relx=0.97, rely=0.24, relheight=0.72)

        self.listaServProd.bind('<Double-1>', self.altera_itens_orc)
        self.listaServProd.bind('<Return>', self.altera_itens_orc)
        self.listaServProd.bind('<Delete>', self.altera_itens_orc_deletabt2)