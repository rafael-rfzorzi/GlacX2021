from Janelas.estiloWidgets.widgets_Glac import *
from funcs.backCads.backConsFinan import *
from datetime import *
from funcs.backUteis.uteis import *

today = date.today()


class Financeiro(ConsFinan):
    def cadfinan(self):
        self.janelaFin = Toplevel()
        self.janelaFin.title(self.m_Financeiro)
        self.janelaFin.geometry("795x270+120+200")
        self.janelaFin.configure(background="gray40")
        self.janelaFin.resizable(FALSE, FALSE)
        self.janelaFin.transient(self.janela)
        self.janelaFin.focus_force()
        self.janelaFin.grab_set()

        ###  A B A S
        self.abas = ttk.Notebook(self.janelaFin)
        self.frame_aba1 = Frame(self.abas)

        self.label1 = Label(self.frame_aba1)
        self.label1.pack(padx=395, pady=120)
        self.abas.add(self.frame_aba1, text=self.m_Receitas)
        self.abas.place(x=0, y=0)

        frameProb = GradientFrame(self.frame_aba1)
        frameProb.place(relx=0, rely=0, relwidth=1, relheight=1)

        descrCodprod = LabelGlac(self.frame_aba1, 'Ano')
        descrCodprod.place(x=5, y=15, width=80, height=25)

        self.sel_lists_tps()

        self.entry5 = StringVar()
        self.entry5.set(today.year)
        self.entry5V = self.rows_ano_dscr

        self.entradaCodReceita = OptionMenu(self.frame_aba1, self.entry5, *self.entry5V)
        self.entradaCodReceita.place(x=85, y=15, width=100, height=25)

        descrMes = LabelGlac(self.frame_aba1, 'Mês')
        descrMes.place(x=5, y=45, width=80, height=25)

        self.entry6 = StringVar()
        mes = today.month - 1
        self.entry6.set(self.rows_meses_dscr[mes])
        self.entry6V = self.rows_meses_dscr

        self.entradaReceita = OptionMenu(self.frame_aba1, self.entry6, *self.entry6V)
        self.entradaReceita.place(x=85, y=45, width=100, height=25)

        ###  Botao Carrega
        botaoAdd = ButtonGlac(self.janelaFin, self.m_Carregar, self.carrega_receita)
        botaoAdd.place(x=35, y=115, width=130, height=35)

        ###  Botao limpa
        botaolimpa = ButtonGlac(self.janelaFin, self.m_Limpar, self.limpa_receita)
        botaolimpa.place(x=35, y=150, width=130, height=35)

        ### Widgets - Listar produtos ###
        self.listaServ = ttk.Treeview(self.frame_aba1, height=10,
            column=("col1", "col2", "col3", "col4"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Placa)
        self.listaServ.heading("#3", text=self.m_Dia)
        self.listaServ.heading("#4", text=self.m_Valor_R)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=70)
        self.listaServ.column("#2", width=140)
        self.listaServ.column("#3", width=130)
        self.listaServ.column("#4", width=60)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.frame_aba1, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=775, y=15, height=222)
        self.listaServ.place(x=220, y=15, width=555)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickFinan)

        self.listaServ2 = ttk.Treeview(self.frame_aba1, height=1, column=("col1", "col2", "col3"))
        self.listaServ2.heading("#0", text="")
        self.listaServ2.heading("#1", text=self.m_Ano)
        self.listaServ2.heading("#2", text=self.m_Mes)
        self.listaServ2.heading("#3", text=self.m_Total)

        self.listaServ2.column("#0", width=0)
        self.listaServ2.column("#1", width=55)
        self.listaServ2.column("#2", width=55)
        self.listaServ2.column("#3", width=90)

        self.listaServ2.place(x=10, y=195)
        self.janelaFin.mainloop()


