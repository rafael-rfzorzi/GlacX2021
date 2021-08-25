from Janelas.estiloWidgets.widgets_Glac import *
from funcs.backCads.backCadServ import *
from Janelas.estiloWidgets.widgets_Glac import *


class Servicos(CadServ):
    def cadserv(self):
        self.janelaServ = Toplevel()
        self.janelaServ.title(self.m_Serviços)
        self.janelaServ.geometry("960x380+10+130")
        self.janelaServ.configure(background='gray30')
        self.janelaServ.resizable(FALSE, FALSE)
        self.janelaServ.transient(self.janela)
        self.janelaServ.focus_force()
        self.janelaServ.grab_set()

        frame_gradiente = GradientFrame(self.janelaServ)
        frame_gradiente.place(relx=0, rely=0, relwidth=1, relheight=1)

        descrCod = LabelGlac(self.janelaServ, self.m_Codigo + self.m_Pontinhos)
        descrCod.place(x=6, y=15, width=80, height=25)

        self.entradaCod = Entry(self.janelaServ)
        self.entradaCod.place(x=80, y=15, width=40, height=25)

        ###  Botao Carrega servico
        botaoAdd = ButtonGlac(self.janelaServ, self.m_Carregar, self.carrega_servicoS)
        botaoAdd.place(x=145, y=15, width=130, height=35)

        ###  Botao limpa servico
        botaolimpa = ButtonGlac(self.janelaServ, self.m_Limpar, self.limpa_servicoS)
        botaolimpa.place(x=275, y=15, width=70, height=35)

        descrServ = LabelGlac(self.janelaServ, self.m_Serviços)
        descrServ.place(x=6, y=60, width=80, height=25)

        self.entradaServ = Entry(self.janelaServ)
        self.entradaServ.place(x=80, y=60, width=350, height=25)

        ###  Botao busca SERVICO
        botaolimpa = ButtonGlac(self.janelaServ, self.m_Buscar, self.busca_servicoS)
        botaolimpa.place(x=345, y=15, width=70, height=35)

        descrHor = LabelGlac(self.janelaServ, self.m_Horas)
        descrHor.place(x=6, y=110, width=80, height=25)

        self.entradaHor = Entry(self.janelaServ)
        self.entradaHor.place(x=80, y=110, width=40, height=25)

        descrCustohora = LabelGlac(self.janelaServ, self.m_Custo_R)
        descrCustohora.place(x=140, y=110, width=70, height=25)

        self.entradaCustohora = Entry(self.janelaServ)
        self.entradaCustohora.place(x=210, y=110,  width=40, height=25)

        descrValorhora = LabelGlac(self.janelaServ, self.m_Valor_R)
        descrValorhora.place(x=270, y=110, width=70, height=25)

        self.entradaValorhora = Entry(self.janelaServ)
        self.entradaValorhora.place(x=335, y=110, width=40, height=25)

        descrTipoServ = LabelGlac(self.janelaServ, self.m_Tipo)
        descrTipoServ.place(x=445, y=15, width=80, height=25)

        self.entradaTipoServ = Entry(self.janelaServ)
        self.entradaTipoServ.place(x=525, y=15, width=200, height=25)

        descrSistemaServ = LabelGlac(self.janelaServ, self.m_Sistema)
        descrSistemaServ.place(x=445, y=45, width=80, height=25)

        self.entradaSistemaServ = Entry(self.janelaServ)
        self.entradaSistemaServ.place(x=525, y=45, width=200, height=25)

        descrDescricao = LabelGlac(self.janelaServ, self.m_Marca)
        descrDescricao.place(x=445, y=75, width=80, height=25)

        self.entradaDescricao = Entry(self.janelaServ)
        self.entradaDescricao.place(x=525, y=75, width=200, height=25)

        descrVeic = ButtonGlac(self.janelaServ, self.m_Veiculo, self.busca_serv_veicS)
        descrVeic.place(x=445, y=105, width=80, height=35)

        self.entradaVeic = Entry(self.janelaServ)
        self.entradaVeic.place(x=525, y=105, width=200, height=25)

        botaoAdd = ButtonGlac(self.janelaServ, self.m_Novo, self.add_servS)
        botaoAdd.place(x=800, y=20, width=90, height=35)

        botaoMudServ = ButtonGlac(self.janelaServ, self.m_Alterar, self.mud_servS)
        botaoMudServ.place(x=800, y=55, width=90, height=35)

        botaoDel = ButtonGlac(self.janelaServ, self.m_Apagar, self.del_servS)
        botaoDel.place(x=800, y=90, width=90, height=35)

        ### Widgets - Listar veiculos
        self.listaServ = ttk.Treeview(self.janelaServ, height=10,
            column=("col1", "col2", "col3", "col4", "col5", "col6",
                    "col7", "col8", "col9"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Serviços)
        self.listaServ.heading("#3", text=self.m_Horas)
        self.listaServ.heading("#4", text=self.m_Custo_R)
        self.listaServ.heading("#5", text=self.m_Valor)
        self.listaServ.heading("#6", text=self.m_Marca)
        self.listaServ.heading("#7", text=self.m_Veiculo)
        self.listaServ.heading("#8", text=self.m_Tipo)
        self.listaServ.heading("#9", text=self.m_Sistema)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=60)
        self.listaServ.column("#2", width=230)
        self.listaServ.column("#3", width=45)
        self.listaServ.column("#4", width=57)
        self.listaServ.column("#5", width=55)
        self.listaServ.column("#6", width=100)
        self.listaServ.column("#7", width=145)
        self.listaServ.column("#8", width=110)
        self.listaServ.column("#9", width=145)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.janelaServ, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=935, y=150, height=225)

        self.conecta_Glac()

        lista = self.cursor.execute("""SELECT cod_sp, servprod, hor, custo , valor, 
        descricao, id_marcaprod, tiposerv, sistemaserv FROM servprod  
        WHERE sp = "s" ORDER BY servprod ASC; """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.listaServ.place(x=-10, y=150)
        self.listaServ.bind("<Double-1>", self.OnDoubleClickS)
        self.desconecta_Glac()

        self.janelaServ.mainloop()
