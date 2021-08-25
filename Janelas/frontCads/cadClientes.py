import time

from Janelas.estiloWidgets.widgets_Glac import *
from tkcalendar import DateEntry
from funcs.backCads.backCadCli import *


class Clientes(CadCli):

    def customer_registration(self):
        self.open_win_cli = "cadcli"
        self.janelaCli = Toplevel(self.janela)
        self.janelaCli.title("Cadastro de Clientes")
        self.janelaCli.configure(background="gray50")
        self.janelaCli.geometry("870x670+70+30")
        self.janelaCli.resizable(FALSE, FALSE)
        self.janelaCli.minsize(width=820, height=650)
        self.janelaCli.transient(self.janela)
        self.janelaCli.focus_force()
        self.janelaCli.grab_set()

        tit_cli = LabelGlac(self.janelaCli, self.m_Clientes)
        tit_cli.place(relx=0, rely=0.01, relwidth=1, relheight=0.03)

        framecli = GradientFrame(self.janelaCli)
        framecli.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.93)

        tituloVeiculos = LabelGlac(self.janelaCli, self.m_Automoveis)
        tituloVeiculos.place(relx=0, rely=0.55, relwidth=0.98, relheight=0.05)

        # 'Label Codigo'
        codPeLabel = LabelGlac(self.janelaCli, self.m_Codigo, "gray30")
        codPeLabel.place(relx=0.02, rely=0.065, relwidth=0.05, relheight=0.026)

        # 'Entry Código'
        self.codPeEntry = Entry(self.janelaCli)
        self.codPeEntry.configure(validate="key", validatecommand=self.vcmd8)
        self.codPeEntry.place(relx=0.02, rely=0.092, relwidth=0.05, relheight=0.025)

        # 'Label Data de Nascimento'
        nascPeLabel = LabelGlac(self.janelaCli, self.m_Nasc, "gray30")
        nascPeLabel.place(relx=0.38, rely=0.125, relwidth=0.1, relheight=0.02)

        # 'Entry Dia'
        self.nascDiaPeEntry = DateEntry(self.janelaCli, locale="pt_BR", fg='gray45')
        self.nascDiaPeEntry.place(relx=0.38, rely=0.145, relwidth=0.1, relheight=0.03)

        # 'Label Nome do Cliente'
        nomePeLabel = LabelGlac(self.janelaCli, self.m_Nome, "gray30")
        nomePeLabel.place(relx=0.02, rely=0.125, relwidth=0.35, relheight=0.025)

        # 'Entry Nome Do Cliente'
        self.nomePeEntry = Entry(self.janelaCli)
        self.nomePeEntry.place(relx=0.02, rely=0.15, relwidth=0.35, relheight=0.026)

        # 'Label Logradouro'
        logradPeLabel = LabelGlac(self.janelaCli, self.m_Endereco, "gray30")
        logradPeLabel.place(relx=0.02, rely=0.176, relwidth=0.35, relheight=0.024)

        # 'Entry Logradouro'
        self.logradPeEntry = Entry(self.janelaCli)
        self.logradPeEntry.place(relx=0.02, rely=0.2, relwidth=0.35, relheight=0.026)

        # 'Label Numero'
        numPeLabel = LabelGlac(self.janelaCli, self.m_Numero, "gray30")
        numPeLabel.place(relx=0.38, rely=0.18, relwidth=0.1, relheight=0.02)

        # 'Entry Numero'
        self.numPeEntry = Entry(self.janelaCli)
        self.numPeEntry.place(relx=0.38, rely=0.2, relwidth=0.1, relheight=0.026)

        # 'Label Complemento'
        complemPeLabel = LabelGlac(self.janelaCli, self.m_Complemento, "gray30")
        complemPeLabel.place(relx=0.02, rely=0.226, relwidth=0.23, relheight=0.024)

        # 'Entry Complemento'
        self.complemPeEntry = Entry(self.janelaCli)
        self.complemPeEntry.place(relx=0.02, rely=0.25, relwidth=0.22, relheight=0.026)

        # 'Label Bairro'
        bairroPeLabel = LabelGlac(self.janelaCli, self.m_Bairro, "gray30")
        bairroPeLabel.place(relx=0.25, rely=0.226, relwidth=0.23, relheight=0.024)

        # 'Entry Bairro'
        self.bairroPeEntry = Entry(self.janelaCli)
        self.bairroPeEntry.place(relx=0.25, rely=0.25, relwidth=0.23, relheight=0.026)

        # 'Label Municipio'
        cidadePeLabel = LabelGlac(self.janelaCli, self.m_Cidade, "gray30")
        cidadePeLabel.place(relx=0.02, rely=0.276, relwidth=0.41, relheight=0.024)

        # 'Entry Municipio'
        self.cidadePeEntry = Entry(self.janelaCli)
        self.cidadePeEntry.place(relx=0.02, rely=0.3, relwidth=0.41, relheight=0.026)

        # 'Label UF'
        ufPeLabel = LabelGlac(self.janelaCli, self.m_Uf, "gray30")
        ufPeLabel.place(relx=0.44, rely=0.276, relwidth=0.04, relheight=0.024)

        # 'Entry UF'
        self.ufPeEntry = Entry(self.janelaCli)
        self.ufPeEntry.place(relx=0.44, rely=0.3, relwidth=0.04, relheight=0.026)

        # 'Label Fone'
        fone1Pelabel = LabelGlac(self.janelaCli, 'Fone 1:', "gray30")
        fone1Pelabel.place(relx=0.02, rely=0.35, relwidth=0.21, relheight=0.02)

        # 'Entry Fone 1'
        self.fone1PeEntry = Entry(self.janelaCli)
        self.fone1PeEntry.configure(validatecommand=self.vcmd2, validate="key")
        self.fone1PeEntry.place(relx=0.02, rely=0.37, relwidth=0.05, relheight=0.026)

        self.fone1PeEntry2 = Entry(self.janelaCli)
        self.fone1PeEntry2.configure(validatecommand=self.vcmd12, validate="key")
        self.fone1PeEntry2.place(relx=0.08, rely=0.37, relwidth=0.15, relheight=0.026)

        # 'Label Fone 2'
        fone2Pelabel = LabelGlac(self.janelaCli, 'Fone 2', "gray30")
        fone2Pelabel.place(relx=0.27, rely=0.35, relwidth=0.21, relheight=0.02)

        # 'Entry Fone 2'
        self.fone2PeEntry = Entry(self.janelaCli)
        self.fone2PeEntry.configure(validate="key", validatecommand=self.vcmd2)
        self.fone2PeEntry.place(relx=0.27, rely=0.37, relwidth=0.05, relheight=0.026)

        self.fone2PeEntry2 = Entry(self.janelaCli)
        self.fone2PeEntry2.configure(validate="key", validatecommand=self.vcmd12)
        self.fone2PeEntry2.place(relx=0.33, rely=0.37, relwidth=0.15, relheight=0.026)

        # 'Label Cpf'
        self.cnpj_mat_str = StringVar()
        self.cnpj_mat_strV = {"CNPJ", "CPF"}
        self.cnpj_mat_str.set("CNPJ")
        self.cnpj_mat_lb = OptionMenu(self.janelaCli, self.cnpj_mat_str, *self.cnpj_mat_strV)
        self.cnpj_mat_lb.place(relx=0.14, rely=0.42, relwidth=0.1, relheight=0.026)

        self.cnpj_mat_ent = Entry(self.janelaCli)
        self.cnpj_mat_ent.configure(validate="key")
        self.cnpj_mat_ent.bind("<KeyRelease>", self.format_cpf_cnpj)
        self.cnpj_mat_ent.place(relx=0.25, rely=0.42, relwidth=0.23, relheight=0.026)

        # 'Label CNPJ'
        cnpjPeLabel = LabelGlac(self.janelaCli, "Cnpj / Cpf", "gray30")
        cnpjPeLabel.place(relx=0.14, rely=0.4, relwidth=0.34, relheight=0.02)

        # 'Entry RG'
        self.rgPeEntry = Entry(self.janelaCli)

        # 'Label Obs'
        obsPeLabel = LabelGlac(self.janelaCli, self.m_Obs, "gray30")
        obsPeLabel.place(relx=0.02, rely=0.446, relwidth=0.22, relheight=0.024)

        # 'Entry Obs'
        self.obsPeEntry = Entry(self.janelaCli)
        self.obsPeEntry.place(relx=0.02, rely=0.47, relwidth=0.22, relheight=0.026)

        # 'Label E-mail'
        emailPeLabel = LabelGlac(self.janelaCli, 'E-mail', "gray30")
        emailPeLabel.place(relx=0.25, rely=0.446, relwidth=0.23, relheight=0.024)

        # 'Entry E-mail'
        self.emailPeEntry = Entry(self.janelaCli)
        self.emailPeEntry.place(relx=0.25, rely=0.47, relwidth=0.23, relheight=0.026)

        # 'Label Cep'
        cepPeLabel = LabelGlac(self.janelaCli, self.m_Cep, "gray30")
        cepPeLabel.place(relx=0.02, rely=0.4, relwidth=0.11, relheight=0.02)

        # 'Botao Cep'
        cepPeBt = ButtonGlac(self.janelaCli, '>>', self.cep)
        cepPeBt.place(relx=0.02, rely=0.42, relwidth=0.03, relheight=0.026)

        # 'Entry Cep'
        self.cepPeEntry = Entry(self.janelaCli)
        self.cepPeEntry.configure(validate="key", validatecommand=self.vcmd8)
        self.cepPeEntry.place(relx=0.05, rely=0.42, relwidth=0.08, relheight=0.026)

        # 'Botao Novo Cliente'
        botaoAdd = ButtonGlac(self.janelaCli, self.m_Novo, self.add_clienteC)
        botaoAdd.place(relx=0.2, rely=0, width=70, height=34)

        # Botao Altera dados do Cliente
        botaoMud = ButtonGlac(self.janelaCli, self.m_Alterar, self.mud_clienteC)
        botaoMud.place(relx=0.28, rely=0, width=70, height=34)

        # Botao deletar dados do Cliente
        botaoDel = ButtonGlac(self.janelaCli, self.m_Apagar, self.deletar_window_c)
        botaoDel.place(relx=0.36, rely=0, width=70, height=34)

        #  Botao limpa
        botaolimpa = ButtonGlac(self.janelaCli, self.m_Limpar, self.limpa_clienteC)
        botaolimpa.place(relx=0.12, rely=0, width=70, height=34)

        #  Botao busca Cabeça
        botaobusca = ButtonGlac(self.janelaCli, '', self.busca_clienteC)
        botaobusca.place(relx=0.34, rely=0.146, relwidth=0.03, relheight=0.03)

        self.barracliente = ttk.Scrollbar(self.janelaCli, orient='vertical', command=self.OnVsbC)
        self.listaServ = ttk.Treeview(self.janelaCli, height=6,
            yscrollcommand=self.barracliente.set, column=("col1", "col2", "col3", "col4"))

        self.listaServ.heading("#0", text="")
        self.listaServ.column("#0", width=1)
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.column("#1", width=40)
        self.listaServ.heading("#2", text=self.m_Nome)
        self.listaServ.column("#2", width=185)
        self.listaServ.heading("#3", text='')
        self.listaServ.column("#3", width=30)
        self.listaServ.heading("#4", text=self.m_Fone)
        self.listaServ.column("#4", width=105)

        self.listaServ.place(relx=0.5, rely=0.06, relwidth=0.465, relheight=0.48)
        self.listaServ.configure(yscroll=self.barracliente.set)
        self.barracliente.place(relx=0.965, rely=0.06, relheight=0.48)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickC)
        self.list_cadcli()

        # Moldura veiculos
        self.entradaVeiculo2 = Entry(self.janelaCli)
        self.entradaMontadora2 = Entry(self.janelaCli)
        self.codEquipEntry = Entry(self.janelaCli)
        self.fabrModeloEquipEntry = Entry(self.janelaCli)
        self.nomeIdEquipEntry = Entry(self.janelaCli)

        serialEquipLabel = LabelGlac(self.janelaCli, self.m_Placa, "gray30")
        serialEquipLabel.place(relx=0.05, rely=0.61, relwidth=0.11, relheight=0.05)

        self.serialEquipEntry = Entry(self.janelaCli)
        self.serialEquipEntry.place(relx=0.05, rely=0.66, relwidth=0.11, relheight=0.03)

        corEquipLabel = LabelGlac(self.janelaCli, self.m_Cor, "gray30")
        corEquipLabel.place(relx=0.57, rely=0.61, relwidth=0.13, relheight=0.04)

        self.corvar = StringVar(self.janelaCli)
        self.coresV = {self.m_Branco, self.m_Amarelo, self.m_Verde,
                       self.m_Bege, self.m_Azul, self.m_Laranja,
                       self.m_Vermelho, self.m_Verde, self.m_Cinza,
                       self.m_Preto, self.m_Marrom, self.m_Bordo,
                       self.m_Prata, self.m_Grafite, self.m_Dourado,
                       self.m_Outro}

        self.corvar.set(self.m_Branco)

        self.popupMenu = OptionMenu(self.janelaCli, self.corvar, *self.coresV)
        self.popupMenu.place(relx=0.57, rely=0.65, relwidth=0.13, relheight=0.04)

        combEquipLabel = LabelGlac(self.janelaCli, self.m_Combustivel, "gray30")
        combEquipLabel.place(relx=0.71, rely=0.61, relwidth=0.13, relheight=0.04)

        self.combvar = StringVar()
        self.combV = {self.m_Gasolina, self.m_Alcool, self.m_Diesel,
                      self.m_Flex, self.m_Gasolina_e_Gas, self.m_Alcool_e_Gas,
                      self.m_Flex_e_Gas}
        self.combvar.set(self.m_Gasolina)

        self.popupMenu = OptionMenu(self.janelaCli, self.combvar, *self.combV)
        self.popupMenu.place(relx=0.71, rely=0.65, relwidth=0.13, relheight=0.04)

        marcaEquipLabel = LabelGlac(self.janelaCli, self.m_Marca, "gray30")
        marcaEquipLabel.place(relx=0.34, rely=0.61, relwidth=0.21, relheight=0.05)

        self.marcaEquipEntry = Entry(self.janelaCli)
        self.marcaIdEquipEntry = Entry(self.janelaCli)
        self.marcaEquipEntry.place(relx=0.34, rely=0.66, relwidth=0.21, relheight=0.03)

        ##### Veiculo
        descrVeiculo = ButtonGlac(self.janelaCli, self.m_Veiculo, self.busca_auto_c)
        descrVeiculo.place(relx=0.17, rely=0.61, relwidth=0.16, relheight=0.05)
        self.nomeEquipEntry = Entry(self.janelaCli)
        self.nomeEquipEntry.place(relx=0.17, rely=0.66, relwidth=0.16, relheight=0.03)

        # Label Ano
        fab_ano_eq_lb = LabelGlac(self.janelaCli, self.m_Ano, "gray30")
        fab_ano_eq_lb.place(relx=0.85, rely=0.61, relwidth=0.11, relheight=0.05)
        # Entry Ano
        self.fabrAnoEquipEntry = Entry(self.janelaCli)
        self.fabrAnoEquipEntry.place(relx=0.85, rely=0.66, relwidth=0.11, relheight=0.03)

        #  Botoes automoveis
        botaoAdd2 = ButtonGlac(self.janelaCli, self.m_Novo, self.add_veiculoC)
        botaoAdd2.place(relx=0.15, rely=0.55, relwidth=0.08, relheight=0.05)

        botaoMud2 = ButtonGlac(self.janelaCli, self.m_Alterar, self.mud_autoC)
        botaoMud2.place(relx=0.23, rely=0.55, relwidth=0.08, relheight=0.05)

        botaoDel2 = ButtonGlac(self.janelaCli, self.m_Apagar, self.deletar_window_placa_c)
        botaoDel2.place(relx=0.31, rely=0.55, relwidth=0.08, relheight=0.05)

        self.listaPlaca = ttk.Treeview(self.janelaCli, height=5,
            column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaPlaca.heading("#0", text="")
        self.listaPlaca.column("#0", width=0)
        self.listaPlaca.heading("#1", text=self.m_Placa)
        self.listaPlaca.column("#1", width=80)
        self.listaPlaca.heading("#2", text=self.m_Veiculo)
        self.listaPlaca.column("#2", width=120)
        self.listaPlaca.heading("#3", text=self.m_Montadora)
        self.listaPlaca.column("#3", width=170)
        self.listaPlaca.heading("#4", text=self.m_Cor)
        self.listaPlaca.column("#4", width=100)
        self.listaPlaca.heading("#5", text=self.m_Combustivel)
        self.listaPlaca.column("#5", width=100)
        self.listaPlaca.heading("#6", text=self.m_Ano)
        self.listaPlaca.column("#6", width=80)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.janelaCli, orient='vertical', command=self.listaPlaca.yview)
        # Adiciona barra de rolagem
        self.listaPlaca.configure(yscroll=self.barra.set)
        self.barra.place(relx=0.96, rely=0.703, relwidth=0.02, relheight=0.27)

        self.listaPlaca.place(relx=0.02, rely=0.7, relwidth=0.94, relheight=0.27)
        #    Binding da listbox
        self.listaPlaca.bind('<Double-1>', self.bind_autoC)

        self.janelaCli.mainloop()
