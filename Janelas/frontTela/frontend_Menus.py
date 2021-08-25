from tkinter import Menu
from tkinter import messagebox

class MenusClass:

    def menus(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        filemenu3 = Menu(menubar)
        filemenu4 = Menu(menubar)
        filemenu5 = Menu(menubar)

        def quit():
            self.janela.destroy()

        def helpme():
            msg = self.m_Ajuda
            msg += ""
            messagebox.showinfo("GLAC ", msg)

        def sobre():
            msg = "GlacX -        rafaelserafim.rfzorzi@gmail.com           \n "
            msg += "RfZorzi - https://www.facebook.com/rfzorzi/ - Brazil"
            messagebox.showinfo("GLAC ", msg)

        menubar.add_cascade(label=self.m_Cadastros, menu=filemenu)
        menubar.add_cascade(label=self.m_Consulta, menu=filemenu2)
        menubar.add_cascade(label=self.m_Relatorios, menu=filemenu3)
        menubar.add_cascade(label=self.m_Procedimentos, menu=filemenu4)
        menubar.add_cascade(label=self.m_Ajuda, menu=filemenu5)
        filemenu.add_command(label=self.m_Automoveis, command=self.cadaut)
        filemenu.add_command(label=self.m_Clientes, command=self.customer_registration)
        filemenu.add_command(label=self.m_Fornecedores, command=self.cadforn)
        filemenu.add_command(label=self.m_Produtos, command=self.cadprod)
        filemenu.add_command(label=self.m_Marca + self.m_Produtos, command=self.cadmarcaprod)
        filemenu.add_command(label=self.m_Serviços, command=self.cadserv)
        filemenu.add_command(label=self.m_Tecnico, command=self.cadtec)
        filemenu.add_command(label=self.m_Estab, command=self.cademp)
        filemenu.add_command(label=self.m_Copia, command=self.backup)
        filemenu.add_command(label=self.m_Sair, command=quit)
        filemenu2.add_command(label=self.m_Cons_Rec, command=self.cadfinan)
        filemenu2.add_command(label=self.m_Cons_Pag, command=self.consultapag)
        filemenu3.add_command(label=self.m_Orcamento, command=self.PrintOrc)
        filemenu3.add_command(label=self.m_ImprimirVistoria, command=self.PrintVist)
        filemenu4.add_command(label=self.m_Proced_Lanc, command=self.cadest)
        filemenu4.add_command(label=self.m_Proced_Atual, command=self.procedServ)
        filemenu5.add_command(label=self.m_Sobre, command=sobre)
