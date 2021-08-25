from funcs.backCads.backCadTec import *
from Janelas.estiloWidgets.widgets_Glac import *


class Tecnicos(CadTec, Entry):
    def cadtec(self):
        self.janelaTec = Toplevel()
        self.janelaTec.title(self.m_Tecnico)
        self.janelaTec.geometry("625x150+100+170")
        self.janelaTec.configure(background="gray50")
        self.janelaTec.transient(self.janela)
        self.janelaTec.focus_force()
        self.janelaTec.grab_set()
        self.janelaTec.resizable(FALSE, FALSE)

        frame_win = GradientFrame(self.janelaTec).place(relwidth=1, relheight=1)

        ###  Botao Novo Cliente
        botaoAdd = ButtonGlac(self.janelaTec, self.m_Novo, self.add_servT)
        botaoAdd.place(x=25, y=105, width=80, height=35)

        ### Botao Altera dados do Cliente
        botaoMud = ButtonGlac(self.janelaTec, self.m_Alterar, self.mud_servT)
        botaoMud.place(x=125, y=105, width=80, height=35)

        ### Botao deletar dados do Cliente
        botaoDel = ButtonGlac(self.janelaTec, self.m_Apagar, self.del_servT)
        botaoDel.place(x=225, y=105, width=80, height=35)

        ##  Botao limpa
        botaolimpa = ButtonGlac(self.janelaTec, self.m_Limpar, self.limpa_servicoT)
        botaolimpa.place(x=220, y=15, width=90, height=35)

        ###  Botao busca Cabeça
        botaobusca = ButtonGlac(self.janelaTec, '>>', self.busca_servicoT)
        botaobusca.place(x=280, y=50, width=30, height=25)

        ###  Botao busca Carregar
        botaoCarregar = ButtonGlac(self.janelaTec, self.m_Carregar, self.carrega_servicoT)
        botaoCarregar.place(x=130, y=15, width=90, height=35)

        descrCod = LabelGlac(self.janelaTec, self.m_Codigo)
        descrCod.place(x=2, y=20, width=80, height=25)

        self.entradaCod = Entry(self.janelaTec)
        self.entradaCod.place(x=80, y=20, width=40, height=25)

        descrTec = LabelGlac(self.janelaTec, self.m_Tecnico)
        descrTec.place(x=2, y=50, width=80, height=25)

        self.entradaTec = Entry(self.janelaTec)
        self.entradaTec.place(x=80, y=50, width=200, height=25)

        # Widgets - Listar tecnicos
        self.listaServ = ttk.Treeview(self.janelaTec, height=6, column=("col1", "col2"))
        self.listaServ.heading("#0", text="")
        self.listaServ.column("#0", width=0)
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.column("#1", width=55)
        self.listaServ.heading("#2", text=self.m_Tecnico)
        self.listaServ.column("#2", width=220)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.janelaTec, orient='vertical',
                                   command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.place(x=325, y=20, height=122)
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=600, y=21, height=122)
        self.listaServ.bind("<Double-1>", self.OnDoubleClickT)

        self.conecta_Glac()

        lista = self.cursor.execute("SELECT cod, tecnico FROM tecnico  ORDER BY tecnico ASC; ")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        self.janelaTec.mainloop()
