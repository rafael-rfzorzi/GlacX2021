from funcs.backUteis.imagensBase64 import *
from funcs.backUteis.ValidaEntradas import *
from Janelas.frontTela.frontend_Containers import *
from Janelas.frontTela.frontend_Molduras import *
from Janelas.frontTela.frontend_PrimeiroFrame import *
from Janelas.frontTela.frontend_SegundoFrame import *
from Janelas.frontTela.frontend_TerceiroFrame import *
from Janelas.frontTela.frontend_QuartoFrame import *
from Janelas.frontTela.frontend_QuintoFrame import *
from Janelas.frontTela.frontend_aba1 import *
from Janelas.frontTela.frontend_aba2 import *
from Janelas.frontTela.frontend_aba4 import *
from Janelas.frontTela.frontend_Menus import *
from Janelas.frontTela.frontend_buscaOrc import *
from Janelas.frontTela.frontend_busca_tecnico import *
from Janelas.frontTela.frontend_busca_servico import *
from Janelas.frontTela.frontend_busca_cliente import *
from funcs.backUteis.relatorios import *
from tkinter import ttk

janela = Tk()
s = ttk.Style()
s.theme_use('default')

class Tela(PrintRel, BuscaOrc, BuscaTecnico, Busca_Serv, BuscaCliente):

    def alteracao(self):
        if self.numero < 1:
            self.numero = self.numero + 0.01
            self.janela.attributes("-alpha", self.numero)
            self.janela.after(40, self.alteracao)

    def tela(self):
        self.numero = 0.01
        self.janela = janela
        self.janela.title("Orçamento e Ordem de Serviço - Glac")
        self.janela.configure(background="#303030")
        self.janela.geometry("950x670+0+0")
        self.janela.resizable(TRUE, TRUE)
        self.janela.minsize(width=900, height=650)
        #self.alteracao()
        #self.janela.attributes("-alpha", self.numero)

        ImagensBase64.var_imag_64(self)
        ValidaEntradas.validaEntradas(self)
        Containers.containers(self)
        Molduras.molduras(self)
        PrimeiroFrame.primeiro_frame(self)
        SegundoFrame.segundo_frame(self)
        TerceiroFrame.terceiro_frame(self)
        QuartoFrame.quarto_frame(self)
        QuintoFrame.quinto_frame(self)

        Aba1.aba1(self)
        Aba2.aba2(self)
        Aba4.aba4(self)

        MenusClass.menus(self)



    def altera_itens_orc(self, *args):
        self.altOrcW = Toplevel()
        self.altOrcW.title('Edição de Item')
        self.altOrcW.geometry("840x100+100+300")
        self.altOrcW.configure(background='gray50')
        self.altOrcW.resizable(False, False)
        self.altOrcW.transient(self.janela)
        self.altOrcW.focus_force()
        self.altOrcW.grab_set()

        frame_win = GradientFrame(self.altOrcW)
        frame_win.place(relwidth=1, relheight=1)

        ordemItemL = LabelGlac(self.altOrcW, 'Ordem')
        ordemItemL.place(x=5, y=8, width=60, height=24)

        self.ordemItem = Entry(self.altOrcW)
        self.ordemItem.place(x=5, y=30, width=60, height=24)

        descrItemL = LabelGlac(self.altOrcW, 'Descrição')
        descrItemL.place(x=70, y=8, height=24)

        self.descrItem = Entry(self.altOrcW)
        self.descrItem.place(x=70, y=30, width=450, height=24)

        codigoItemL = LabelGlac(self.altOrcW, 'Código')
        codigoItemL.place(x=560, y=8, width=60, height=24)

        self.codigoItem = Entry(self.altOrcW)
        self.codigoItem.place(x=560, y=30, width=60, height=24)

        valorItemL = LabelGlac(self.altOrcW, 'R$ Valor')
        valorItemL.place(x=630, y=8,  width=60, height=24)

        self.valorItem = Entry(self.altOrcW)
        self.valorItem.place(x=630, y=30,  width=60, height=24)

        quantItemL = ButtonGlac(self.altOrcW, 'Quant', self.altera_itens_orc_quant)
        quantItemL.place(x=700, y=2,  width=60, height=30)

        self.quantItem = Entry(self.altOrcW)
        self.quantItem.place(x=700, y=30, width=60, height=24)

        totalItemL = LabelGlac(self.altOrcW, 'R$ Total')
        totalItemL.place(x=770, y=8, width=60, height=24)

        self.totalItem = Entry(self.altOrcW)
        self.totalItem.place(x=770, y=30, width=60, height=24)

        altera_itenBt = ButtonGlac(self.altOrcW, 'Alterar Registro', self.altera_itens_orc_alterabt)
        altera_itenBt.place(x=540, y=60, height=35)

        deleta_itenBt = ButtonGlac(self.altOrcW, 'Excluir Registro', self.altera_itens_orc_deletabt)
        deleta_itenBt.place(x=690, y=60, height=35)

        self.listaServProd.selection()
        for n in self.listaServProd.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServProd.item(n, 'values')
            self.ordemItem.insert(END, col1)
            self.descrItem.insert(END, col2)
            self.codigoItem.insert(END, col3)
            self.valorItem.insert(END, col4)
            self.quantItem.insert(END, col5)
            self.totalItem.insert(END, col6)
