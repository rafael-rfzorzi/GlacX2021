from Janelas.estiloWidgets.widgets_Glac import *
from funcs.backCads.backCadEmpresa import *


class Empresa(CadEmpresa):
    def cademp(self):
        self.janelaEmp = Toplevel()
        self.janelaEmp.title('Glacx' + self.m_Empresa)
        self.janelaEmp.configure(background="gray20")
        self.janelaEmp.geometry("410x250+250+250")
        self.janelaEmp.resizable(FALSE, FALSE)
        self.janelaEmp.transient(self.janela)
        self.janelaEmp.focus_force()
        self.janelaEmp.grab_set()

        descrNomeServ = LabelGlac(self.janelaEmp, self.m_Estab)
        descrNomeServ.place(relx=0.2, rely=0.05, relwidth=0.6)

        self.entradaCod_emp = Entry(self.janelaEmp)

        #  Descrição e Entrada Nome
        descrNome = LabelGlac(self.janelaEmp, self.m_Nome)
        descrNome.place(x=10, y=53, width=80)

        self.entradaNome_emp = Listbox(self.janelaEmp, height=1)
        self.entradaNome_emp.place(x=85, y=53, width=300)

        #  Descrição e Entrada Enedereco
        descrEndereco = LabelGlac(self.janelaEmp, self.m_Endereco)
        descrEndereco.place(x=10, y=83, width=80)

        self.entradaEndereco_emp = Listbox(self.janelaEmp, height=1)
        self.entradaEndereco_emp.place(x=85, y=83, width=300)

        #  Descrição e Entrada Bairro
        descrBairro = LabelGlac(self.janelaEmp, self.m_Bairro )
        descrBairro.place(x=10, y=103, width=80)

        self.entradaBairro_emp = Listbox(self.janelaEmp, height=1)
        self.entradaBairro_emp.place(x=85, y=103, width=300)

        #  Descrição e Entrada Municipio
        descrMunicipio = LabelGlac(self.janelaEmp, self.m_Cidade)
        descrMunicipio.place(x=10, y=123, width=80)

        self.entradaMunicipio_emp = Listbox(self.janelaEmp, height=1)
        self.entradaMunicipio_emp.place(x=85, y=123, width=220)

        #  Descrição e Entrada UF
        descrUf = LabelGlac(self.janelaEmp, self.m_Uf)
        descrUf.place(x=315, y=123, width=30)

        self.entradaUf_emp = Listbox(self.janelaEmp, height=1)
        self.entradaUf_emp.place(x=350, y=123, width=30)

        #  Descrição e Entrada Fone
        descrFone = LabelGlac(self.janelaEmp, self.m_Fone)
        descrFone.place(x=10, y=143, width=80)

        self.entradaFone_emp = Listbox(self.janelaEmp, height=1)
        self.entradaFone_emp.place(x=85, y=143, width=140)

        #  Descrição e Entrada Cep
        descrCep = LabelGlac(self.janelaEmp, self.m_Cep)
        descrCep.place(x=230, y=143, width=40)

        self.entradaCep_emp = Listbox(self.janelaEmp, height=1)
        self.entradaCep_emp.place(x=270, y=143, width=115)

        #  Descrição e Entrada Cpf
        descrCpf = LabelGlac(self.janelaEmp, self.m_Cnpj)
        descrCpf.place(x=10, y=163, width=80)

        self.entradaCpf_emp = Listbox(self.janelaEmp, height=1)
        self.entradaCpf_emp.place(x=85, y=163, width=140)

        #  Descrição e Entrada Rg
        descrRg = LabelGlac(self.janelaEmp, self.m_Cpf)
        descrRg.place(x=230, y=163, width=40)

        self.entradaRg_emp = Listbox(self.janelaEmp, height=1)
        self.entradaRg_emp.place(x=270, y=163, width=115)

        #  Descrição e Entrada Obs
        descrObs = LabelGlac(self.janelaEmp, self.m_Obs)
        descrObs.place(x=10, y=193, width=80)

        self.entradaObs_emp = Listbox(self.janelaEmp, height=1)
        self.entradaObs_emp.place(x=85, y=193, width=300)

        self.conecta_Glac()

        lista = self.cursor.execute("""SELECT cod_emp FROM empresa; """)
        for i in lista:
            self.entradaCod_emp.insert(i, END)

        self.desconecta_Glac()

        self.carrega_empresa()
        self.janelaEmp.mainloop()

