from Janelas.estiloWidgets.widgets_Glac import *


class BuscaCliente:

    def busca_cliente(self):
        self.listacliente = Toplevel()
        self.listacliente.title("  GLAC  ")
        self.listacliente.geometry("332x390+200+200")
        self.listacliente.resizable(FALSE, FALSE)
        self.listacliente.configure(background='gray55')
        self.listacliente.transient(self.janela)
        self.listacliente.focus_force()
        self.listacliente.grab_set()

        frame1 = GradientFrame(self.listacliente).place(relwidth=1, relheight=1)

        LabelCliente = LabelGlac(self.listacliente, self.m_BuscaCliMsg1)
        LabelCliente.place(relx=0.04, rely=0.01, relwidth=0.9, relheight=0.06)

        LabelCliente2 = LabelGlac(self.listacliente, self.m_BuscaCliMsg2)
        LabelCliente2.place(relx=0.04, rely=0.05, relwidth=0.9, relheight=0.05)

        LabelCliente2 = LabelGlac(self.listacliente, self.m_Pesquisa + self.m_Pontinhos)
        LabelCliente2.place(x=10, y=46)

        self.EntryCliente2 = Entry(self.listacliente)
        self.EntryCliente2.place(x=80, y=45)

        ButtonCliente2 = ButtonGlac(self.listacliente, self.m_Buscar, self.buscaCli)
        ButtonCliente2.place(x=225, y=40, height=30)

        self.listaServ = ttk.Treeview(self.listacliente, height=12, column=("col1", "col2"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Nome)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=60)
        self.listaServ.column("#2", width=245)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.listacliente, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=310, y=70, height=260)

        self.listaServ.place(x=7, y=70)
        self.listaServ.bind("<Double-1>", self.carrega_cliente2)

        ButtonClienteNovo = ButtonGlac(self.listacliente, "Novo", self.customer_registration)
        ButtonClienteNovo.place(relx=0.7, y=345, height=35)

        LabelCliente2 = LabelGlac(self.listacliente, self.m_BuscaCliMsg3)
        LabelCliente2.place(relx=0.02, rely=0.88, relwidth=0.68, relheight=0.05)
        LabelCliente2 = LabelGlac(self.listacliente, self.m_BuscaCliMsg4)
        LabelCliente2.place(relx=0.02, rely=0.93, relwidth=0.68, relheight=0.05)

        self.conecta_Glac()

        nome = self.listNome.get()

        self.cursor.execute("""SELECT cod_cli, nome FROM clientes """ )
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)
        self.desconecta_Glac()

        def busca_cliente_a(event):
            event.busca_cliente()
