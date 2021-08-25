from Janelas.estiloWidgets.widgets_Glac import *


class MaodeObra:
    def procedServ(self):
        ### Widgets - Listar Orçamentos ###
        self.listaOrc = Toplevel()
        self.listaOrc.title(" GLAC  ")
        self.listaOrc.geometry("300x100+110+100")
        self.listaOrc.configure(background="gray50")
        self.listaOrc.resizable(FALSE, FALSE)
        self.listaOrc.transient(self.janela)
        self.listaOrc.focus_force()
        self.listaOrc.grab_set()

        frame_win = GradientFrame(self.listaOrc).place(relwidth=1, relheight=1)

        MensLabel = LabelGlac(self.listaOrc, self.m_AtualizaMsg)
        MensLabel.place(relx=0.1, rely=0.1, relwidt=0.8)

        self.listaNomeO = Entry(self.listaOrc)
        self.listaNomeO.place(relx=0.2, rely=0.6, width=80, height=27)

        botaoBuscaNome = ButtonGlac(self.listaOrc, self.m_Atualizar, self.procedServF)
        botaoBuscaNome.place(relx=0.5, rely=0.6, height=35)

    def procedServF(self):
        valorServ = self.listaNomeO.get()
        Serv = 's'
        self.conecta_Glac()
        self.cursor.execute("""UPDATE servprod SET valor = ? WHERE sp = ?""", (valorServ, Serv))
        self.conn.commit()

        self.desconecta_Glac()
        msg = "Valor atualizado com sucesso.\n "
        messagebox.showinfo("GLAC", msg)
        self.listaOrc.destroy()
