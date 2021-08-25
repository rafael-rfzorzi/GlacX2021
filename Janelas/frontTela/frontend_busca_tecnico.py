from tkinter import *
from tkinter import ttk
from Janelas.estiloWidgets.widgets_Glac import GradientFrame


class BuscaTecnico:
    def busca_tecnico(self):
        self.conecta_Glac()

        self.entradaTecnico.delete(0, END)
        self.listatec = Toplevel()
        self.listatec.title(" GLAC  ")
        self.listatec.geometry("350x150+150+400")
        self.listatec.resizable(TRUE, TRUE)
        self.listatec.transient(self.janela)
        self.listatec.focus_force()
        self.listatec.grab_set()

        frame_win = GradientFrame(self.listatec)
        frame_win.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.listaServ = ttk.Treeview(self.listatec, height=6, column=("col1", "col2"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Tecnico)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=40)
        self.listaServ.column("#2", width=280)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.listatec, orient='vertical',
                               command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=327, y=5, height=142)

        self.listaServ.place(x=5, y=5)
        self.cursor.execute("""SELECT cod, tecnico FROM tecnico ORDER BY cod ASC; """)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        # Binding da listbox
        self.listaServ.bind('<Double-1>', self.add_tecnicobind)
        self.desconecta_Glac()
