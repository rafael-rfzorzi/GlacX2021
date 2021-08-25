from funcs.backCads.backCadForn import *
from Janelas.estiloWidgets.widgets_Glac import *


class Fornecedores(CadForn):
    def cadforn(self):
        self.win_for = Toplevel()
        self.win_for.title(self.m_Fornecedores)
        self.win_for.configure(background="gray30")
        self.win_for.geometry("705x270+100+250")
        self.win_for.resizable(FALSE, FALSE)
        self.win_for.transient(self.janela)
        self.win_for.focus_force()
        self.win_for.grab_set()
        self.open_win_cli = "cadfor"

        frame_cad = GradientFrame(self.win_for).place(relwidth=1, relheight=1)

        dscr_cd_for = LabelGlac(self.win_for, self.m_Codigo + self.m_Pontinhos)
        dscr_cd_for.place(relx=0.01, rely=0.03, relwidth=0.1, relheight=0.07)

        self.entr_cd_for = Entry(self.win_for)
        self.entr_cd_for.place(relx=0.11, rely=0.03, relwidth=0.05, relheight=0.07)

        # Fornecedor
        dscr_for = LabelGlac(self.win_for, self.m_Fornecedor)
        dscr_for.place(relx=0.01, rely=0.13, relwidth=0.1, relheight=0.07)

        self.entr_for = Entry(self.win_for)
        self.entr_for.place(relx=0.11, rely=0.13, relwidth=0.27, relheight=0.07)

        # Fone
        dscr_fone = LabelGlac(self.win_for, self.m_Fone + self.m_Pontinhos)
        dscr_fone.place(relx=0.01, rely=0.23, relwidth=0.1, relheight=0.07)

        self.entr_fone = Entry(self.win_for)
        self.entr_fone.place(relx=0.11, rely=0.23, relwidth=0.1, relheight=0.07)

        self.cnpj_mat_str = StringVar()
        self.cnpj_mat_strV = {"CNPJ", "CPF"}
        self.cnpj_mat_str.set("CNPJ")
        self.cnpj_mat_lb = OptionMenu(self.win_for, self.cnpj_mat_str, *self.cnpj_mat_strV)
        self.cnpj_mat_lb.place(relx=0.22, rely=0.23, relwidth=0.1, relheight=0.07)

        self.entr_cnpj = Entry(self.win_for)
        self.entr_cnpj.configure(validate="key")
        self.entr_cnpj.bind("<KeyRelease>", self.format_cpf_cnpj)
        self.entr_cnpj.place(relx=0.32, rely=0.23, relwidth=0.16, relheight=0.07)

        self.entr_cep = Entry(self.win_for)
        self.entr_cep.place(relx=0.11, rely=0.33, relwidth=0.1, relheight=0.07)

        dscr_end = LabelGlac(self.win_for, self.m_Endereco)
        dscr_end.place(relx=0.01, rely=0.43, relwidth=0.1, relheight=0.07)

        self.entr_end = Entry(self.win_for)
        self.entr_end.place(relx=0.11, rely=0.43, relwidth=0.35, relheight=0.07)

        dscr_mun = LabelGlac(self.win_for, self.m_Cidade)
        dscr_mun.place(relx=0.01, rely=0.53, relwidth=0.1, relheight=0.07)

        self.entr_mun = Entry(self.win_for)
        self.entr_mun.place(relx=0.11, rely=0.53, relwidth=0.35, relheight=0.07)

        dscr_obs = LabelGlac(self.win_for, self.m_Observacao)
        dscr_obs.place(relx=0.01, rely=0.63, relwidth=0.15, relheight=0.07)

        self.entr_dscr = Entry(self.win_for)
        self.entr_dscr.place(relx=0.16, rely=0.63, relwidth=0.3, relheight=0.07)

        bt_ld_f = ButtonGlac(self.win_for, self.m_Carregar, self.carrega_fornecedor)
        bt_ld_f.place(relx=0.17, rely=0, relwidth=0.11, relheight=0.13)

        bt_cl_f = ButtonGlac(self.win_for, self.m_Limpar, self.limpa_fornecedor)
        bt_cl_f.place(relx=0.28, rely=0, relwidth=0.11, relheight=0.13)

        bt_busc_for = ButtonGlac(self.win_for, self.m_Buscar, self.busca_fornecedor)
        bt_busc_for.place(relx=0.39, rely=0.11, relwidth=0.11, relheight=0.12)

        bt_cep_for = ButtonGlac(self.win_for, self.m_Cep, self.cepForn)
        bt_cep_for.place(relx=0.01, rely=0.31, relwidth=0.1, relheight=0.11)

        bt_nv_for = ButtonGlac(self.win_for, self.m_Novo, self.add_fornec)
        bt_nv_for.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.13)

        bt_alt_for = ButtonGlac(self.win_for, self.m_Alterar, self.mud_fornec)
        bt_alt_for.place(relx=0.2, rely=0.8, relwidth=0.1, relheight=0.13)

        bt_del_for = ButtonGlac(self.win_for, self.m_Apagar, self.del_fornec)
        bt_del_for.place(relx=0.3, rely=0.8, relwidth=0.1, relheight=0.13)

        # Widgets - Listar
        self.list_g = ttk.Treeview(self.win_for, height=12, column=("col1", "col2", "col3", "col4"))
        self.list_g.heading("#0", text="")
        self.list_g.column("#0", width=0)
        self.list_g.heading("#1", text=self.m_Codigo)
        self.list_g.column("#1", width=40)
        self.list_g.heading("#2", text=self.m_Fornecedores)
        self.list_g.column("#2", width=120)
        self.list_g.heading("#3", text=self.m_Fone)
        self.list_g.column("#3", width=70)
        self.list_g.heading("#4", text=self.m_Cidade)
        self.list_g.column("#4", width=100)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.win_for, orient='vertical', command=self.list_g.yview)

        # Adiciona barra de rolagem
        self.list_g.configure(yscroll=self.barra.set)
        self.barra.place(x=685, y=12, height=245)
        self.list_g.place(x=355, y=12, height=245)
        self.list_g.bind("<Double-1>", self.OnDoubleClickForn)

        self.list_fornec()
