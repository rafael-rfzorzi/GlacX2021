from funcs.backUteis import imagensBase64, multilang, validadores, uteis
from funcs.backUteis import colors, conector, license, editItem
from funcs.backUteis import backAba2Front, backSegundoFrame
from Janelas import frontend
from Janelas.frontCads import cadAuto, cadClientes, cadEmpresa, cadMarcaProd
from Janelas.frontCads import cadEstoque, cadFornec, cadServ, cadProd
from Janelas.frontCads import cadPagamento, cadTec, AtMObra, consFinan
from Janelas.estiloWidgets.widgets_Glac import StyleGlac
from multiprocessing.pool import ThreadPool

class Application(uteis.Functions, imagensBase64.ImagensBase64, conector.Conector,
        frontend.Tela, cadAuto.Automoveis, cadClientes.Clientes, multilang.Lang,
        colors.Colors, cadFornec.Fornecedores, cadTec.Tecnicos,
        validadores.Validadores, cadProd.Produtos, cadServ.Servicos,
        license.Data_company, cadMarcaProd.MarcaProdutos, AtMObra.MaodeObra,
        cadEmpresa.Empresa, cadEstoque.Estoque, consFinan.Financeiro,
        cadPagamento.PagamentoOrc, editItem.EditItens, backAba2Front.Aba2,
        backSegundoFrame.SegundoFrame):
    def __init__(self):
        self.cores()
        self.dados()
        self.multiGlacx()
        self.images_base64()
        self.tela()
        # treeview configs
        style = StyleGlac()
        style.theme_use('default')
        style2 = StyleGlac("Treeview", ('Calibri', 9), "gray20", "gray50")
        style3 = StyleGlac("Vertical.TScrollbar", ('Calibri', 10), "#D1D1D1")
        style4 = StyleGlac("TNotebook", ('Arial', 10, 'bold'), "gray40", "gray60", "gray50")
        style5 = StyleGlac("TOptionMenu", ('Arial', 10, 'bold'), "gray40", "gray60", "gray50")
        style2.map('Treeview', background=[('selected', '#7499b8')], foreground=[('selected', "gray20")])
        style4.map('TNotebook', background=[('selected', '#F5B041')], foreground=[('selected', "gray20")])
        style.element_create("plain.field", "from", "clam")
        style6 = StyleGlac("EntryStyle.TEntry", ('Calibri', 10), "gray25", "gray60", "gray25")
        ##
        self.janela.mainloop()

Application()
