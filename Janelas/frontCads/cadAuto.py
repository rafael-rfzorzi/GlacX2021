from funcs.backCads.backCadAuto import *
from Janelas.estiloWidgets.widgets_Glac import *


class Automoveis(CadAuto):
    def cadaut(self):
        self.janelaAut = Toplevel()
        self.janelaAut.title('Glac - Cadastro de Veiculos')
        self.janelaAut.geometry("780x240+100+200")
        self.janelaAut.configure(background="gray30")
        self.janelaAut.resizable(FALSE, FALSE)
        self.janelaAut.transient(self.janela)
        self.janelaAut.focus_force()
        self.janelaAut.grab_set()

        frameCadAuto = GradientFrame(self.janelaAut)
        frameCadAuto.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Label do codigo
        descrCod_aut = LabelGlac(self.janelaAut, self.m_Codigo)
        descrCod_aut.place(relx=0.01, rely=0.1, relwidth=0.1, relheight=0.1)

        #### entrada do codigo
        self.entradaCod_autA = Entry(self.janelaAut)
        self.entradaCod_autA.configure(validate="key", validatecommand=self.vcmd4)
        self.entradaCod_autA.place(relx=0.1, rely=0.1, relwidth=0.05, relheight=0.1)

        # descrição do veiculo
        descrAut = LabelGlac(self.janelaAut, self.m_Automovel)
        descrAut.place(relx=0.01, rely=0.3, relwidth=0.1, relheight=0.1)

        self.entradaAutA = Entry(self.janelaAut)
        self.entradaAutA.place(relx=0.1, rely=0.3, relwidth=0.25, relheight=0.1)

        # entry da marca
        self.entradaMarcaA = Entry(self.janelaAut)
        self.entradaMarcaA.place(relx=0.1, rely=0.5, relwidth=0.25, relheight=0.1)

        self.entradaMarca2A = Entry()

        # botão busca
        botaoBuscaAut = ButtonGlac(self.janelaAut, self.m_Buscar, self.busca_automovelA)
        botaoBuscaAut.place(relx=0.35, rely=0.28, relwidth=0.1, relheight=0.14)

        # botao limpa
        botaoLimpaAut = ButtonGlac(self.janelaAut, self.m_Limpar, self.limpa_automovelA)
        botaoLimpaAut.place(relx=0.35, rely=0.08, relwidth=0.1, relheight=0.14)

        # botao marca
        botaoMarcaAut = ButtonGlac(self.janelaAut, self.m_Marca, self.busca_autoA)
        botaoMarcaAut.place(relx=0.01, rely=0.48, relwidth=0.09, relheight=0.14)

        #
        botaoNovoAut = ButtonGlac(self.janelaAut, self.m_Novo, self.add_automovelA)
        botaoNovoAut.place(x=30, y=180, width=80, relheight=0.14)
        #
        botaoAlterarAut = ButtonGlac(self.janelaAut, self.m_Alterar, self.mud_automovelA)
        botaoAlterarAut.place(x=130, y=180, width=80, relheight=0.14)
        #
        botaoApagarAut = ButtonGlac(self.janelaAut, self.m_Apagar, self.del_automovelA)
        botaoApagarAut.place(x=230, y=180, width=80, relheight=0.14)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.janelaAut, orient='vertical', command=self.OnVsbA)

        # Widgets - Listar veiculos
        self.listaServ = ttk.Treeview(self.janelaAut, height=8, column=("col1", "col2", "col3"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Automovel)
        self.listaServ.heading("#3", text=self.m_Marca)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=45)
        self.listaServ.column("#2", width=180)
        self.listaServ.column("#3", width=170)
        self.listaServ.configure(yscroll=self.barra.set)
        self.listaServ.place(x=365, y=5, height=225)

        # Adiciona barra de rolagem
        self.barra.place(x=760, y=5, height=225)
        self.busca_automovelA()
        self.listaServ.bind("<Double-1>", self.OnDoubleClickA)
        self.janelaAut.mainloop()

    def busca_autoA(self):
        # Widgets -
        self.entradaMarcaA.insert(0, '%')
        veicAuto = self.entradaMarcaA.get()

        self.listatec = Toplevel()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("320x220+100+100")
        self.listatec.resizable(FALSE, FALSE)
        self.listatec.transient(self.janelaAut)
        self.listatec.focus_force()
        self.listatec.grab_set()

        ### Widgets -
        self.listaTec1 = ttk.Treeview(self.listatec, height=5, column=("col1", "col2"))
        self.listaTec1.heading("#0", text="")
        self.listaTec1.heading("#1", text=self.m_Codigo)
        self.listaTec1.heading("#2", text='Marca')

        self.listaTec1.column("#0", width=0)
        self.listaTec1.column("#1", width=60)
        self.listaTec1.column("#2", width=200)

        # Adiciona barra de rolagem
        self.listaTec1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        # Binding da listbox
        self.listaTec1.bind('<Double-1>', self.add_autobindA)
        self.conecta_Glac()

        buscaservico = self.cursor.execute("""SELECT cod, marca FROM montadora 
            WHERE marca LIKE '%s' ORDER BY marca ASC""" % veicAuto)

        for i in buscaservico:
            self.listaTec1.insert("", END, values=i)
        self.entradaMarcaA.delete('0', 'end')
        self.entradaMarca2A.delete('0', 'end')
        self.desconecta_Glac()
