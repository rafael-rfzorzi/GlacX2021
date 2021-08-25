from tkinter import *


class CadTec:
    def add_tecnicobind(self, event):
        self.codServ1.delete(0, END)

        self.listaServ.selection()
        for n in self.listaServ.selection():
            col1, col2 = self.listaServ.item(n, 'values')
            self.entradaTecnico.insert(END, col2)

        self.listatec.destroy()

    def OnTec(self, *args):
        self.listaServ.yview(*args)

    def limpa_servicoT(self):
        self.entradaCod.delete(0, END)
        self.entradaTec.delete(0, END)

    def mud_servT(self):
        self.conecta_Glac()

        cod_sp = self.entradaCod.get()
        servprod = self.entradaTec.get()

        self.cursor.execute("""
            UPDATE tecnico SET tecnico = ? WHERE cod = ?""", (servprod, cod_sp))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
        SELECT * FROM tecnico ORDER BY tecnico ASC;
        """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()

    def OnDoubleClickT(self, event):
        self.limpa_servicoT()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2 = self.listaServ.item(n, 'values')
            self.entradaCod.insert(END, col1)

        self.carrega_servicoT()

    def del_servT(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        cod_sp = self.entradaCod.get()
        self.cursor.execute("""
        DELETE FROM tecnico WHERE cod = ? """, (cod_sp,))
        self.conn.commit()

        lista = self.cursor.execute("""
        SELECT cod, tecnico FROM tecnico ORDER BY tecnico ASC;
        """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.entradaCod.delete(0, END)
        self.entradaTec.delete(0, END)

        self.desconecta_Glac()

    def carrega_servicoT(self):
        cod_sp = self.entradaCod.get()
        self.conecta_Glac()

        sp = self.cursor

        self.entradaTec.delete(0, END)

        sp.execute("SELECT tecnico FROM tecnico WHERE cod = '%s'" % cod_sp)
        consultaserv = self.cursor.fetchall()
        for i in consultaserv:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaTec.insert(END, i)

        self.desconecta_Glac()

    def busca_servicoT(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())

        self.entradaTec.insert(END, '%')
        servprod = self.entradaTec.get()
        servico = self.cursor

        servico.execute("""SELECT cod, tecnico FROM tecnico WHERE tecnico LIKE '%s'  """ % servprod)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            self.listaServ.insert("", END, values=i)
        self.entradaCod.delete(0, END)
        self.entradaTec.delete(0, END)

        self.desconecta_Glac()

    def add_servT(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        codinf = self.cursor.execute("""select MAX(cod) + 1 from tecnico """)
        for i in codinf:
            self.entradaCod.insert(END, i)

        servprod = self.entradaTec.get()
        cod_sp = self.entradaCod.get()

        self.cursor.execute("""
    		INSERT INTO tecnico (cod, tecnico) VALUES (?, ?)""", (cod_sp, servprod))
        self.conn.commit()

        lista = self.cursor.execute("""
        SELECT * FROM tecnico ORDER BY tecnico ASC;
        """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.entradaCod.delete(0, END)
        self.entradaTec.delete(0, END)

        self.desconecta_Glac()