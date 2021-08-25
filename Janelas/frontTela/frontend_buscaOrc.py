from Janelas.estiloWidgets.widgets_Glac import *


class BuscaOrc:
    def busca_orc(self):
        self.listaOrc = Toplevel()
        self.listaOrc.title(" GLAC  ")
        self.listaOrc.geometry("615x320+180+200")
        self.listaOrc.configure(background="gray40")
        self.listaOrc.resizable(FALSE, FALSE)
        self.listaOrc.transient(self.janela)
        self.listaOrc.focus_force()
        self.listaOrc.grab_set()

        frame_win = GradientFrame(self.listaOrc).place(relwidth=1, relheight=1)

        self.listaNomeO = Entry(self.listaOrc)
        self.listaNomeO.place(x=10, y=7, width=120, height=25)

        botaoBuscaNome = ButtonGlac(self.listaOrc, "Buscar Nome", self.buscanomeorc)
        botaoBuscaNome.place(x=132, y=5, width=110, height=30)

        self.listaPlaca = Entry(self.listaOrc)
        self.listaPlaca.place(x=250, y=7, width=120, height=25)

        botaoBuscaPlaca = ButtonGlac(self.listaOrc, 'Buscar Placa', self.buscaplacaorc)
        botaoBuscaPlaca.place(x=372, y=5, width=110, height=30)

        ### Widgets - Listar veiculos ###
        self.listaServ = ttk.Treeview(self.listaOrc, height=12,
            column=("col1", "col2", "col3", "col4", "col5"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Orcamento)
        self.listaServ.heading("#2", text=self.m_Nome)
        self.listaServ.heading("#3", text=self.m_Dia)
        self.listaServ.heading("#4", text=self.m_Placa)
        self.listaServ.heading("#5", text=self.m_Tipo)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=80)
        self.listaServ.column("#2", width=190)
        self.listaServ.column("#3", width=100)
        self.listaServ.column("#4", width=80)
        self.listaServ.column("#5", width=137)
        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.listaOrc, orient='vertical',
                                   command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=593, y=50, height=260)

        self.listaServ.place(x=10, y=50)
        self.listaServ.bind("<Double-1>", self.carrega_orc)

        self.conecta_Glac()
        self.cursor.execute("""SELECT id_orc1, clientes.nome, dia , placa_orc, tipoOrc 
        FROM orcamento1, clientes WHERE cod_cli = cliente_orc ORDER BY id_orc1 DESC; """)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)
        self.desconecta_Glac()

        def busca_orc_a(event):
            busca_orc()

