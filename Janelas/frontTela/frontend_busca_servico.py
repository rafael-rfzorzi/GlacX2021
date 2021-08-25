from Janelas.estiloWidgets.widgets_Glac import *


class Busca_Serv:
    def busca_servico(self):
        self.listaServP1 = Toplevel()
        self.listaServP1.title(self.m_PesquisaServProd)
        self.listaServP1.geometry("940x270+20+250")
        self.listaServP1.configure(background='gray50')
        self.listaServP1.resizable(FALSE, FALSE)
        self.listaServP1.transient(self.janela)
        self.listaServP1.focus_force()
        self.listaServP1.grab_set()

        frame_win = GradientFrame(self.listaServP1)
        frame_win.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.barra12 = ttk.Scrollbar(self.listaServP1, orient='vertical', command=self.OnVsb_S1)
        self.barra12.place(x=920, y=41, height=220)

        self.listaServ1 = ttk.Treeview(self.listaServP1, height=10, yscrollcommand=self.barra12.set,
            column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))

        self.listaServ1.heading("#0", text="")
        self.listaServ1.column("#0", width=1)
        self.listaServ1.heading("#1", text=self.m_Codigo)
        self.listaServ1.column("#1", width=45)
        self.listaServ1.heading("#2", text=self.m_Serviços + self.m_barra + self.m_Produtos)
        self.listaServ1.column("#2", width=250)
        self.listaServ1.heading("#3", text=self.m_Tipo)
        self.listaServ1.column("#3", width=120)
        self.listaServ1.heading("#4", text=self.m_Quant)
        self.listaServ1.column("#4", width=50)
        self.listaServ1.heading("#5", text=self.m_Marca)
        self.listaServ1.column("#5", width=90)
        self.listaServ1.heading("#6", text=self.m_Automovel)
        self.listaServ1.column("#6", width=140)
        self.listaServ1.heading("#7", text=self.m_Sistema)
        self.listaServ1.column("#7", width=140)
        self.listaServ1.heading("#8", text=self.m_Valor)
        self.listaServ1.column("#8", width=70)

        self.listaServ1.place(x=15, y=40)
        self.listaServ1.configure(yscroll=self.barra12.set)
        self.listaServ1.delete(*self.listaServ1.get_children())

        descrCod_cli = LabelGlac(self.listaServP1, self.m_Pesquisa + ':')
        descrCod_cli.place(x=20, y=7, height=30)

        self.listaServicos1 = Entry(self.listaServP1)
        self.listaServicos1.place(x=75, y=7, width=200, height=30)

        btBuscaServ1 = ButtonGlac(self.listaServP1, self.m_BuscaServProd, self.busca_serv)
        btBuscaServ1.place(x=280, y=2, width=180, height=37)

        btBuscaServ2 = ButtonGlac(self.listaServP1, self.m_BuscaVeiculos, self.busca_serv_veic)
        btBuscaServ2.place(x=462, y=2, width=140, height=37)
        servprod = self.listaServicos1.get()

        self.conecta_Glac()

        self.cursor.execute("""SELECT cod_sp, servprod, tiposerv, hor, descricao, id_marcaprod, 
            sistemaserv, valor * hor FROM servprod ORDER BY cod_sp ASC""")
        buscaservico12 = self.cursor.fetchall()
        for i in buscaservico12:
            self.listaServ1.insert("", END, values=(i))
        self.desconecta_Glac()
