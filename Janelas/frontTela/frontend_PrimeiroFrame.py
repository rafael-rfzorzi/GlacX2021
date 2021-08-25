import awesometkinter as atk
from Janelas.estiloWidgets.widgets_Glac import *
from Janelas.estiloWidgets.widgets_Glac import ButtonGlac


class PrimeiroFrame:

    def primeiro_frame(self):
        bg_bt = '#333333'
        # Botoes
        self.cadcliBt = self.cadcliBt.subsample(3, 3)
        self.ClientBot = ButtonGlac(self.top, '', self.customer_registration, bg_bt)
        self.ClientBot.configure(image=self.cadcliBt)
        self.ClientBot.place(relx=0.03, rely=0.14, relwidth=0.06, relheight=0.72)

        self.cadfornecBt = self.cadfornecBt.subsample(3, 3)
        self.FornecBot = ButtonGlac(self.top, '', self.cadforn, bg_bt)
        self.FornecBot.configure(image=self.cadfornecBt)
        self.FornecBot.place(relx=0.1, rely=0.14, relwidth=0.06, relheight=0.72)

        self.cadautBt = self.cadautBt.subsample(3, 3)
        self.ModelosBot = ButtonGlac(self.top, '', self.cadaut, bg_bt)
        self.ModelosBot.configure(image=self.cadautBt)
        self.ModelosBot.place(relx=0.17, rely=0.14, relwidth=0.06, height=54)

        self.cadprodBt = self.cadprodBt.subsample(3, 3)
        self.ProdutosBot = ButtonGlac(self.top, '', self.cadprod, bg_bt)
        self.ProdutosBot.configure(image=self.cadprodBt)
        self.ProdutosBot.place(relx=0.24, rely=0.14, relwidth=0.06, height=54)

        self.cadservBt = self.cadservBt.subsample(3, 3)
        self.ServBot = ButtonGlac(self.top, '', self.cadserv, bg_bt)
        self.ServBot.configure(image=self.cadservBt)
        self.ServBot.place(relx=0.31, rely=0.14, relwidth=0.06, height=54)

        bar = atk.RadialProgressbar3d(self.top, fg='cyan', size=64)
        bar.place(relx=0.9, rely=0.1)
        bar.start()

        ## Botao Acesse nossa pagina
        self.acesseface = self.acesseface.subsample(2, 2)
        self.licenciamentoBt = atk.Button3d(self.top, image=self.acesseface, command=self.PaginaRf)
        self.licenciamentoBt.place(relx=0.908, rely=0.22, relwidth=0.048, relheight=0.6)

        #logotipo
        self.glacx_logo = self.glacx_logo.subsample(1, 1)
        self.logoBot = atk.Button3d(self.top, image=self.glacx_logo,
            bg='#4682b4')
        self.logoBot.place(relx=0.44, rely=0.1, width=120, relheight=0.8)



