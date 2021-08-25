from tkinter import Listbox
from Janelas.estiloWidgets.widgets_Glac import *
from tkcalendar import DateEntry
from babel.numbers import *


class SegundoFrame:
    def segundo_frame(self):
        # Label cod
        cdCli = LabelGlac(self.FrameCliente, 'Codigo')
        cdCli.configure(bg='gray20')
        cdCli.place(relx=0.07, rely=0.04, relwidth=0.1, relheight=0.15)

        # Entrada do Codigo do Cliente
        self.entradaCod_cli= Entry(self.FrameCliente)
        self.entradaCod_cli.configure(validate="key", validatecommand=self.vcmd6)
        self.entradaCod_cli.place(relx=0.17, rely=0.06, relwidth=0.13, relheight=0.13)

        # Botão Carrega
        btAdd = ButtonGlac(self.FrameCliente, self.m_Buscar, self.busca_cliente)
        btAdd.place(relx=0.74, rely=0.22, relwidth=0.12, relheight=0.27)

        # Botão Limpa
        btLimp = ButtonGlac(self.FrameCliente, self.m_Limpar, self.limpa_cliente)
        btLimp.place(relx=0.86, rely=0.22, relwidth=0.12, relheight=0.27)

        # Label data
        descrData = LabelGlac(self.FrameCliente, self.m_Data)
        descrData.configure(bg='gray20')
        descrData.place(relx=0.6, rely=0.04, relwidth=0.1, relheight=0.15)

        # Entrada Dia
        self.entradaDataorc = DateEntry(self.FrameCliente, locale="pt_BR")
        self.entradaDataorc.place(relx=0.7, rely=0.04, relwidth=0.22, relheight=0.15)

        # Entrada do nome do cliente
        lbNome = LabelGlac(self.FrameCliente, 'Nome')
        lbNome.configure(bg='gray20')
        lbNome.place(relx=0.08, rely=0.2, relwidth=0.09, relheight=0.15)

        self.listNome = Entry(self.FrameCliente)
        self.listNome.place(relx=0.17, rely=0.21, relwidth=0.55, relheight=0.13)

        # Entrada do Endereço
        lbEndereco = LabelGlac(self.FrameCliente, 'Logradouro')
        lbEndereco.configure(bg='gray20')
        lbEndereco.place(relx=0.01, rely=0.36, relwidth=0.17, relheight=0.15)

        self.listEndereco=Entry(self.FrameCliente)
        self.listEndereco.place(relx=0.17, rely=0.37, relwidth=0.55, relheight=0.13)

        # Entrada Municipio
        lbMun = LabelGlac(self.FrameCliente, 'Municipio')
        lbMun.configure(bg='gray20')
        lbMun.place(relx=0.02, rely=0.52, relwidth=0.15, relheight=0.15)

        self.listMunicipio=Entry(self.FrameCliente)
        self.listMunicipio.place(relx=0.17, rely=0.53, relwidth=0.65, relheight=0.13)

        # Entrada UF
        lbUf = LabelGlac(self.FrameCliente, 'Uf')
        lbUf.configure(bg='gray20')
        lbUf.place(relx=0.83, rely=0.53, relwidth=0.05, relheight=0.13)

        self.listUf=Entry(self.FrameCliente)
        self.listUf.place(relx=0.89, rely=0.52, relwidth=0.08, relheight=0.15)

        # Entrada CPF CNPJ
        lbCpfCnpj = LabelGlac(self.FrameCliente, 'Cpf/Cnpj')
        lbCpfCnpj.configure(bg='gray20')
        lbCpfCnpj.place(relx=0.04, rely=0.68, relwidth=0.13, relheight=0.14)

        self.listCpf=Entry(self.FrameCliente)
        self.listCpf.place(relx=0.17, rely=0.69, relwidth=0.35, relheight=0.13)

        # Entrada Fone
        lbFone = LabelGlac(self.FrameCliente, 'Fone')
        lbFone.configure(bg='gray20')
        lbFone.place(relx=0.52, rely=0.68, relwidth=0.1, relheight=0.14)

        self.listFone=Entry(self.FrameCliente)
        self.listFone.place(relx=0.62, rely=0.69, relwidth=0.35, relheight=0.13)

        # Entrada OBS
        lbObs = LabelGlac(self.FrameCliente, 'Observação')
        lbObs.configure(bg='gray20')
        lbObs.place(relx=0.01, rely=0.84, relwidth=0.17, relheight=0.12)

        self.listObs= Entry(self.FrameCliente)
        self.listObs.place(relx=0.17, rely=0.83, relwidth=0.8, relheight=0.12)

        ####  Lista de placas
        self.entradaCod_aut = Listbox(self.FrameAut2, bg='gray25', width=11,
            fg='gray65', height=9, font=('Verdana', '8', 'bold'))
        self.entradaCod_aut.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        # Binding da listbox da Placa
        self.entradaCod_aut.bind('<Button-1>', self.carrega_automovel)

        # Placa
        lbPlaca = LabelGlac(self.FrameAut, 'Placa')
        lbPlaca.configure(bg='gray20')
        lbPlaca.place(relx=0.01, rely=0.1, relwidth=0.15, relheight=0.15)

        self.placa = Entry(self.FrameAut)
        self.placa.place(relx=0.15, rely=0.11, relwidth=0.4, relheight=0.13)

        ###  Label e Entrada Ano
        lbPlaca = LabelGlac(self.FrameAut, 'Ano')
        lbPlaca.configure(bg='gray20')
        lbPlaca.place(relx=0.56, rely=0.1, relwidth=0.15, relheight=0.15)

        self.listAno = Entry(self.FrameAut)
        self.listAno.config(validate="key", validatecommand=self.vcmd4)
        self.listAno.place(relx=0.72, rely=0.11, relwidth=0.25, relheight=0.13)

        ###  Label e Entrada Veiculo
        lbVeiculo = LabelGlac(self.FrameAut, 'Veiculo')
        lbVeiculo.configure(bg='gray20')
        lbVeiculo.place(relx=0.01, rely=0.26, relwidth=0.25, relheight=0.15)

        self.listAut = Entry(self.FrameAut)
        self.listAut.place(relx=0.25, rely=0.27, relwidth=0.72, relheight=0.13)

        ###  Label e Entrada Marca
        lbMarca = LabelGlac(self.FrameAut, 'Marca')
        lbMarca.configure(bg='gray20')
        lbMarca.place(relx=0.01, rely=0.42, relwidth=0.25, relheight=0.15)

        self.listMarca = Entry(self.FrameAut)
        self.listMarca.place(relx=0.25, rely=0.43, relwidth=0.72, relheight=0.13)

        ###  Label e Entrada Combustivel
        lbFuel = LabelGlac(self.FrameAut, 'Combust')
        lbFuel.configure(bg='gray20')
        lbFuel.place(relx=0.01, rely=0.58, relwidth=0.25, relheight=0.15)

        self.listCombustivel = Entry(self.FrameAut)
        self.listCombustivel.place(relx=0.25, rely=0.59, relwidth=0.72, relheight=0.13)

        ###  Label e Entrada km
        lbKm = LabelGlac(self.FrameAut, 'Km')
        lbKm.configure(bg='gray20')
        lbKm.place(relx=0.01, rely=0.74, relwidth=0.15, relheight=0.15)

        self.entradaObs = Entry(self.FrameAut)
        self.entradaObs.config(validate="key", validatecommand=self.vcmd9float)
        self.entradaObs.place(relx=0.15, rely=0.75, relwidth=0.22, relheight=0.13)

        ###  Label e Entrada Cor
        lbCor = LabelGlac(self.FrameAut, 'Cor')
        lbCor.configure(bg='gray20')
        lbCor.place(relx=0.38, rely=0.75, relwidth=0.15, relheight=0.13)

        self.listCor = Entry(self.FrameAut)
        self.listCor.place(relx=0.53, rely=0.74, relwidth=0.44, relheight=0.15)

