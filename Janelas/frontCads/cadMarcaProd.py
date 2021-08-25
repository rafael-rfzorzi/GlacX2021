from tkinter import *
from funcs.backCads.backCadMarcaProd import *
from Janelas.estiloWidgets.widgets_Glac import *


class MarcaProdutos(CadMarcaProd):
    def cadmarcaprod(self):
        self.janelaM = Toplevel()
        self.janelaM.title(self.m_Marca + ' ' + self.m_Produtos)
        self.janelaM.geometry("870x200+30+250")
        self.janelaM.configure(background="gray30")
        self.janelaM.resizable(FALSE, FALSE)
        self.janelaM.transient(self.janela)
        self.janelaM.focus_force()
        self.janelaM.grab_set()

        frame_win = GradientFrame(self.janelaM).place(relwidth=1, relheight=1)

        descrCod = LabelGlac(self.janelaM, self.m_Codigo)
        descrCod.place(x=5, y=20, width=80, height=25)

        self.entradaCod = Entry(self.janelaM)
        self.entradaCod.place(x=85, y=20, width=50, height=25)

        ###  Botao Carrega marca
        botaoAdd = ButtonGlac(self.janelaM, self.m_Carregar, self.carrega_marca_prod)
        botaoAdd.place(x=145, y=15, width=130, height=30)

        ###  Botao limpa automovel
        botaolimpa = ButtonGlac(self.janelaM, self.m_Limpar, self.limpa_marca_prod)
        botaolimpa.place(x=275, y=15, width=80, height=30)

        descrMarca = LabelGlac(self.janelaM, self.m_Marca)
        descrMarca.place(x=5, y=50, width=80, height=25)

        self.entradaMarca = Entry(self.janelaM)
        self.entradaMarca.place(x=85, y=50, width=200, height=25)

        ###  Botao busca automovel
        botaobusca = ButtonGlac(self.janelaM, self.m_Buscar, self.busca_marca_prod)
        botaobusca.place(x=285, y=45, width=70, height=30)

        descrDescricao = LabelGlac(self.janelaM, self.m_Descricao)
        descrDescricao.place(x=5, y=90, width=80, height=25)

        self.entradaDescricao = Entry(self.janelaM)
        self.entradaDescricao.place(x=85, y=90, width=250, height=25)

        # Botao adicionar
        botaoAdd = ButtonGlac(self.janelaM, self.m_Novo, self.add_marca_prod)
        botaoAdd.place(x=45, y=150, width=85, height=30)

        # botao mudar
        botaoMud = ButtonGlac(self.janelaM, self.m_Alterar, self.mud_marca_prod)
        botaoMud.place(x=130, y=150, width=85, height=30)

        # botao deletar
        botaoDel = ButtonGlac(self.janelaM, " Apagar ", self.del_marca_prod)
        botaoDel.place(x=215, y=150, width=85, height=30)

        ### Widgets - Listar produtos ###
        self.listaServ = ttk.Treeview(self.janelaM, height=7,
                                      column=("col1", "col2", "col3"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Marca)
        self.listaServ.heading("#3", text=self.m_Descricao)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=65)
        self.listaServ.column("#2", width=200)
        self.listaServ.column("#3", width=220)
        self.listaServ.place(x=360, y=20)

        self.conecta_Glac()

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.janelaM, orient='vertical', command=self.listaServ.yview)
        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=845, y=20, width=20, height=160)

        lista = self.cursor.execute("""SELECT cod_marca, marca, descricao 
        FROM marcaprod ORDER BY marca ASC ;""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickMarc)
        self.desconecta_Glac()
        self.janelaM.mainloop()
