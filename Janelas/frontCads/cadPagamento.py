from tkcalendar import DateEntry
from funcs.backCads.backCadPagamento import *
from Janelas.estiloWidgets.widgets_Glac import *
from datetime import *
today = date.today()


class PagamentoOrc(CadPagamento):
    def consultapag(self):
        self.sel_lists_tps()
        self.janelaPagOrc = Toplevel()
        self.janelaPagOrc.title("GlacX - Consulta de pagamentos")
        self.janelaPagOrc.geometry("790x435+120+130")
        self.janelaPagOrc.configure(background="gray55")
        self.janelaPagOrc.resizable(FALSE, FALSE)
        self.janelaPagOrc.transient(self.janela)
        self.janelaPagOrc.focus_force()
        self.janelaPagOrc.grab_set()

        ###  Frame Moldura
        frame3 = GradientFrame(self.janelaPagOrc).place(relwidth=1, relheight=1)

        #### Frame do Valor a ser inserido
        frameValor2 = GradientFrame(self.janelaPagOrc)
        frameValor2.place(relx=0.02, rely=0.134, relwidth=0.96, height=55)

        #### Frame do Valor a ser inserido
        frameValor3 = GradientFrame(self.janelaPagOrc)
        frameValor3.place(relx=0.02, rely=0.018, relwidth=0.96, height=55)

        ### Lista de pagamentos
        self.listaPag = ttk.Treeview(self.janelaPagOrc, height=10,
            column=("col1", "col2", "col3", "col4", "col5"))
        self.listaPag.heading("#0", text="")
        self.listaPag.column("#0", width=0)
        self.listaPag.heading("#1", text='O.S')
        self.listaPag.column("#1", width=60)
        self.listaPag.heading("#2", text=self.m_Tipo)
        self.listaPag.column("#2", width=220)
        self.listaPag.heading("#3", text=self.m_Valor)
        self.listaPag.column("#3", width=120)
        self.listaPag.heading("#4", text="Data")
        self.listaPag.column("#4", width=180)
        self.listaPag.heading("#5", text=self.m_Pago)
        self.listaPag.column("#5", width=110)

        self.listaPag.place(relx=0.02, rely=0.3, relwidth=0.94)

        # Cria barra de rolagem
        self.barraMov = ttk.Scrollbar(self.janelaPagOrc, orient='vertical', command=self.listaPag.yview)
        self.barraMov.place(relx=0.96, rely=0.305, relwidth=0.02, height=221)

        self.listaPag.bind("<Double-1>" , self.OnDoubleClickpag)
        self.listaPag.configure(yscroll=self.barraMov.set)

        #### Frame do Valor a ser inserido
        frameValor = GradientFrame(self.janelaPagOrc)
        frameValor.place(x=590, y=370, width=175, height=52)

        ### Label do saldo a ser pago
        labelValor = LabelGlac(self.janelaPagOrc, self.m_Valor + ' ' + self.m_Total)
        labelValor.place(x=600, y=375, width=150)

        labelCifrao = LabelGlac(self.janelaPagOrc, self.m_Reais)
        labelCifrao.place(x=600, y=395, width=75)

        #### Entry do saldo a ser pago
        self.entryValorDevido = Entry(self.janelaPagOrc)
        self.entryValorDevido.configure(validate="key")
        self.entryValorDevido.place(x=675, y=395, width=75)

        #### Listbox do tipo de pagamento
        self.listtipopag = StringVar()
        self.listtipopag.set(self.tipos_pag[0])
        self.popupMenu = OptionMenu(self.janelaPagOrc, self.listtipopag, *self.tipos_pag)
        self.popupMenu.place(relx=0.04, rely=0.08, relwidth=0.15, height=20)

        tipoPag = LabelGlac(self.janelaPagOrc, self.m_Tipo + ' ' + self.m_Pagamento)
        tipoPag.place(relx=0.04, rely=0.03, relwidth=0.15, height=20)

        #### Entry data
        meslabel = LabelGlac(self.janelaPagOrc, 'Mês')
        meslabel.place(relx=0.2, rely=0.03, relwidth=0.12, height=20)
        self.mesvar = StringVar()
        self.mesesV = self.rows_meses_dscr
        mes = today.month - 1
        self.mesvar.set(self.rows_meses_dscr[mes])
        self.popupMenu = OptionMenu(self.janelaPagOrc, self.mesvar, *self.mesesV)
        self.popupMenu.place(relx=0.2, rely=0.08, relwidth=0.12, height=20)

        anolabel = LabelGlac(self.janelaPagOrc, 'Ano')
        anolabel.place(relx=0.33, rely=0.03, relwidth=0.08, height=20)
        self.anovar = StringVar()
        self.anosV = self.rows_ano_dscr
        self.anovar.set(today.year)
        self.popupMenu = OptionMenu(self.janelaPagOrc, self.anovar, *self.anosV)
        self.popupMenu.place(relx=0.33, rely=0.08, relwidth=0.08, height=20)

        ### Pago?
        pagolabel = LabelGlac(self.janelaPagOrc, self.m_Pago)
        pagolabel.place(relx=0.43, rely=0.03, width=80, height=20)
        self.entry7 = StringVar()
        self.entry7V = {self.m_Sim, self.m_Nao}
        self.entry7V = sorted(self.entry7V)
        self.entry7.set(self.m_Sim)

        self.popupMenu = OptionMenu(self.janelaPagOrc, self.entry7, *self.entry7V)
        self.popupMenu.place(relx=0.43, rely=0.08, width=80, height=20)

        #### Button Inserir Registro
        btinserir1 = ButtonGlac(self.janelaPagOrc,
            "Consulta competência/Tipo/Pago? ", self.carregaConsulta)
        btinserir1.place(relx=0.57, rely=0.04, width=300, height=35)

        #### Entry data
        self.mesvar2 = StringVar()
        self.mesesV2 = self.rows_meses_dscr
        mes = today.month - 1
        self.mesvar2.set(self.rows_meses_dscr[mes])
        self.popupMenu2 = OptionMenu(self.janelaPagOrc, self.mesvar2, *self.mesesV2)
        self.popupMenu2.place(relx=0.04, rely=0.2, relwidth=0.15, height=20)
        mesValor2Label = LabelGlac(self.janelaPagOrc, 'Mês')
        mesValor2Label.place(relx=0.04, rely=0.15, relwidth=0.15, height=20)

        self.anovar2 = StringVar()
        self.anovar2.set(today.year)
        self.popupMenu2 = OptionMenu(self.janelaPagOrc, self.anovar2, *self.rows_ano_dscr)
        self.popupMenu2.place(relx=0.2, rely=0.2, relwidth=0.12, height=20)
        anoValor2label= LabelGlac(self.janelaPagOrc, self.m_Ano)
        anoValor2label.place(relx=0.2, rely=0.15, relwidth=0.12, height=20)

        # Pago?
        self.entry72 = StringVar()
        self.entry72.set(self.sim_nao[1])
        self.popupMenu2 = OptionMenu(self.janelaPagOrc, self.entry72, *self.sim_nao)
        self.popupMenu2.place(relx=0.33, rely=0.2, relwidth=0.08, height=20)

        pagoValor2 = LabelGlac(self.janelaPagOrc, self.m_Pago)
        pagoValor2.place(relx=0.33, rely=0.15, relwidth=0.08, height=20)

        #### Button Inserir Registro
        btinserir = ButtonGlac(self.janelaPagOrc, self.m_Consulta + ' ' +
            self.m_Competência + self.m_barra + self.m_Pago, self.carregaConsulta2)
        btinserir.place(relx=0.57, rely=0.16, width=300, height=35)

        self.janelaPagOrc.mainloop()

    def pagaOrdem(self):
        self.sel_lists_tps()
        self.janelaPagOrc = Toplevel()
        self.janelaPagOrc.title("GlacX - Formas de Pagamento")
        self.janelaPagOrc.geometry("800x420+100+150")
        self.janelaPagOrc.resizable(FALSE, FALSE)
        self.janelaPagOrc.transient(self.janela)
        self.janelaPagOrc.focus_force()
        self.janelaPagOrc.grab_set()

        ###  Frame Moldura
        frame3 = GradientFrame(self.janelaPagOrc)
        frame3.configure(background='gray50')
        frame3.place(relwidth=1, relheight=1)

        # Label do numero de atendimento
        labelNumAtend = LabelGlac(self.janelaPagOrc, self.m_NumAtend)
        labelNumAtend.place(relx=0.03, rely=0.01, relwidth=0.17, height=20)

        # Entry do numero de atendimento
        self.entryNumAtend = Listbox(self.janelaPagOrc, height=1)
        self.entryNumAtend.configure(bg='lightgray', font=('Verdana', '8', 'bold'))
        self.entryNumAtend.place(relx=0.17, rely=0.01, width=80, height=20)

        # Label do valor total
        labelValorTotal = LabelGlac(frame3, self.m_Valor + ' ' + self.m_Total)
        labelValorTotal.place(relx=0.03, rely=0.06, relwidth=0.17, height=20)

        # Entry do valor total
        self.text = self.entradatotal.get()
        self.text = self.text.replace("R$","").replace("(","").replace(")","")
        self.text = float(self.text)
        self.text = f'{self.text:.2f}'
        self.entryValorTotal = Entry(frame3)
        self.entryValorTotal.place(relx=0.17, rely=0.06, width=80, height=20)
        self.entryValorTotal.insert(END, self.text)

        ### Label do valor a ser inserido
        labelValor = LabelGlac(frame3, self.m_Valor)
        labelValor.place(relx=0.475, rely=0.01, width=80, height=20)
        labelCifrao = LabelGlac(frame3, self.m_Reais)
        labelCifrao.place(relx=0.475, rely=0.05, width=20, height=25)

        #### Entry do valor a ser inserido
        self.entryValor = Entry(frame3)
        self.entryValor.configure(validate='key')
        self.entryValor.place(relx=0.5, rely=0.06, width=60, height=20)
        self.entryValor.insert(END, f'{00.00:.2f}')

        # Listbox do tipo de pagamento
        self.listtipopag = StringVar()
        self.listtipopag.set(self.m_Dinheiro)

        self.popupMenu = OptionMenu(frame3, self.listtipopag, *self.tipos_pag)
        self.popupMenu.place(relx=0.588, rely=0.06, width=100, height=22)

        tipopaglabel = LabelGlac(frame3, self.m_Tipo + ' ' + self.m_Pagamento)
        tipopaglabel.place(relx=0.588, rely=0.01, width=100, height=20)

        #### Data frame
        framedata = LabelGlac(frame3, 'Data')
        framedata.place(relx=0.72, rely=0.01, width=100, height=20)
        self.data_forma_pag = DateEntry(frame3, locale='pt_BR')
        self.data_forma_pag.place(relx=0.72, rely=0.06, width=100, height=22)

        #### Button Inserir Registro
        btinserir3 = ButtonGlac(frame3, self.m_Inserir, self.add_pag)
        btinserir3.place(relx=0.86, rely=0.04, width=90, height=35)

        ### Lista de pagamentos
        self.listaPag = ttk.Treeview(frame3, height=14,
            column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        self.listaPag.heading("#0", text="")
        self.listaPag.column("#0", width=0)
        self.listaPag.heading("#1", text='O.S')
        self.listaPag.column("#1", width=50)
        self.listaPag.heading("#2", text=self.m_Tipo)
        self.listaPag.column("#2", width=130)
        self.listaPag.heading("#3", text=self.m_Valor + ' ' + self.m_Pagamento)
        self.listaPag.column("#3", width=160)
        self.listaPag.heading("#4", text=self.m_ValorDeduzir)
        self.listaPag.column("#4", width=140)
        self.listaPag.heading("#5", text="Data")
        self.listaPag.column("#5", width=100)
        self.listaPag.heading("#6", text=self.m_Pago)
        self.listaPag.column("#6", width=78)
        self.listaPag.heading("#7", text="")
        self.listaPag.column("#7", width=78)
        self.listaPag.place(relx=0.03, rely=0.12)

        # Cria barra de rolagem
        self.barraMov = ttk.Scrollbar(frame3, orient='vertical', command=self.listaPag.yview)
        self.barraMov.place(relx=0.952, rely=0.124, width=20, height=300)

        self.listaPag.bind("<Double-1>", self.OnDoubleClickpag)
        self.listaPag.configure(yscroll=self.barraMov.set)

        ### Label do saldo a ser pago
        labelValor = LabelGlac(frame3, self.m_ValorDevido)
        labelValor.place(x=640, y=365, width=100, height=25)
        labelCifrao = LabelGlac(frame3, "R$")
        labelCifrao.place(x=640, y=385, width=30, height=25)

        #### Entry do saldo a ser pago
        self.entryValorDevido = Entry(frame3)
        self.entryValorDevido.configure(validate="key")
        self.entryValorDevido.place(x=670, y=385, width=70, height=25)

        ### Label do saldo ja pago
        labelValor2 = LabelGlac(frame3, "Valor Pago")
        labelValor2.place(x=500, y=365, width=100, height=25)
        labelCifrao2 = LabelGlac(frame3, self.m_Reais)
        labelCifrao2.place(x=500, y=385, width=30, height=25)

        #### Entry do saldo ja pago
        self.entryValorInform = Entry(frame3)
        self.entryValorInform.configure(validate="key")
        self.entryValorInform.place(x=530, y=385, width=70, height=25)
        self.sel_pag_ordem()

        self.janelaPagOrc.mainloop()

    def OnDoubleClickpag(self, event):
        self.listaPag.selection()
        self.janPag2 = Toplevel()
        self.janPag2.title("GlacX")
        self.janPag2.geometry("590x60+170+300")
        self.janPag2.configure(background='gray55')
        self.janPag2.resizable(FALSE, FALSE)
        self.janPag2.transient(self.janelaPagOrc)
        self.janPag2.focus_force()
        self.janPag2.grab_set()

        ###  Frame Moldura
        frame3 = GradientFrame(self.janPag2).place(relwidth=1, relheight=1)

        ## Entry NUm Atend
        label1 = LabelGlac(self.janPag2, "Nº O.S")
        label1.place(x=5, y=8, width=50, height=25)

        self.entry1 = Listbox(self.janPag2, width=8, height=1)
        self.entry1.place(x=5, y=30, width=50, height=25)

        #### Listbox do tipo de pagamento
        labelTipopag2 = LabelGlac(self.janPag2, self.m_Tipo + ' ' + self.m_Pagamento)
        labelTipopag2.place(x=65, y=8, width=130, height=25)

        self.entry2 = StringVar()
        self.entry2V = {self.m_Debito, self.m_Credito, self.m_Dinheiro, self.m_Boleto,
            self.m_ChequePre, self.m_ChequeVista, self.m_Crediario, self.m_Promissoria,
            self.m_Desconto, self.m_Avista}
        self.entry2V = sorted(self.entry2V)
        self.popupMenu = OptionMenu(self.janPag2, self.entry2, *self.entry2V)
        self.popupMenu.place(x=65, y=30, width=130, height=25)

        #### Valor da parcela
        label1 = LabelGlac(self.janPag2, self.m_Valor_R)
        label1.place(x=205, y=8, width=80, height=25)

        self.entry3 = Entry(self.janPag2)
        self.entry3.place(x=205, y=30, width=80, height=25)

        ### dia
        label1 = LabelGlac(self.janPag2, "Data/Pagam")
        label1.place(x=295, y=8, width=120, height=25)

        self.entry4 = DateEntry(self.janPag2, locale='pt_BR')
        self.entry4.place(x=295, y=30, width=120, height=25)

        ### Pago?
        label1 = LabelGlac(self.janPag2, self.m_Pago)
        label1.place(x=425, y=8, width=65, height=25)

        self.entry7 = StringVar()
        self.entry7V = {self.m_Sim, self.m_Nao}
        self.entry7V = sorted(self.entry7V)
        self.entry7.set("Sim")
        self.popupMenu = OptionMenu(self.janPag2, self.entry7, *self.entry7V)
        self.popupMenu.place(x=425, y=30, width=65, height=25)

        ### Alterar registro
        button5 = ButtonGlac(self.janPag2, self.m_Alterar, self.mud_pag)
        button5.place(x=500, y=25, height=33)

        self.entry9 = Entry(self.janPag2)

        for n in self.listaPag.selection():
            col1, col2, col3, col4, col5, col6, col7 = self.listaPag.item(n, 'values')
            self.entry1.insert(END, col1)
            self.entry2.set(col2)
            self.entry3.insert(END, col4)
            self.entry4.delete(0, END)
            self.entry4.insert(END, col5)
            self.entry7.set(col6)
            self.entry9.insert(END, col7)

        self.janPag2.mainloop()