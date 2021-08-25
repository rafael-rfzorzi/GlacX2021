from tkinter import *


class CadServ:
    def OnDoubleClickS(self, event):
        self.limpa_servicoS()
        self.listaServ.selection()
        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.listaServ.item(n, 'values')
            self.entradaCod.insert(END, col1)
        self.carrega_servicoS()

    def mud_servS(self):
        cod_sp = self.entradaCod.get()
        servprod = self.entradaServ.get()
        hor = self.entradaHor.get()
        custo = self.entradaCustohora.get()
        valor = self.entradaValorhora.get()
        tiposerv = self.entradaTipoServ.get()
        sistemaserv = self.entradaSistemaServ.get()
        descricao = self.entradaDescricao.get()
        veic = self.entradaVeic.get()

        self.conecta_Glac()
        self.cursor.execute("""UPDATE servprod 
        SET servprod = ?, hor = ?, custo = ?, valor = ?, tiposerv = ?, sistemaserv = ?,
        descricao = ?, id_marcaprod = ? 
        WHERE cod_sp = ?""", (servprod, hor, custo, valor, tiposerv, sistemaserv,
                              descricao, veic, cod_sp))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""SELECT cod_sp, servprod, hor, custo , valor, 
        descricao, id_marcaprod, tiposerv, sistemaserv FROM servprod  
        WHERE sp = "S" ORDER BY servprod ASC; """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()

    def limpa_servicoS(self):
        self.entradaCod.delete(0, END)
        self.entradaServ.delete(0, END)
        self.entradaHor.delete(0, END)
        self.entradaCustohora.delete(0, END)
        self.entradaValorhora.delete(0, END)
        self.entradaTipoServ.delete(0, END)
        self.entradaSistemaServ.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaVeic.delete(0, END)

    def del_servS(self):
        self.conecta_Glac()
        cod_sp = self.entradaCod.get()
        self.listaServ.delete(*self.listaServ.get_children())
        self.cursor.execute("""DELETE FROM servprod WHERE cod_sp=?""", (cod_sp,))
        self.conn.commit()
        lista = self.cursor.execute("""SELECT cod_sp, servprod, hor, custo , valor, 
        descricao, tiposerv, sistemaserv FROM servprod  
        WHERE sp = "S" ORDER BY cod_sp DESC;""")
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()

    def carrega_servicoS(self):
        cod_sp = self.entradaCod.get()
        self.conecta_Glac()

        self.entradaServ.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaHor.delete(0, END)
        self.entradaCustohora.delete(0, END)
        self.entradaValorhora.delete(0, END)
        self.entradaTipoServ.delete(0, END)
        self.entradaSistemaServ.delete(0, END)
        self.entradaVeic.delete(0, END)

        self.cursor.execute("""SELECT servprod, hor, custo, valor, tiposerv, sistemaserv,
            descricao, id_marcaprod FROM servprod WHERE cod_sp = '%s'""" % cod_sp)
        consultaserv = self.cursor.fetchall()
        for i in consultaserv:
            self.entradaServ.insert(END, i[0])
            self.entradaHor.insert(END, i[1])
            self.entradaCustohora.insert(END, i[2])
            self.entradaValorhora.insert(END, i[3])
            self.entradaTipoServ.insert(END, i[4])
            self.entradaSistemaServ.insert(END, i[5])
            self.entradaDescricao.insert(END, i[6])
            self.entradaVeic.insert(END, i[7])

            self.desconecta_Glac()

    def busca_serv_veicS(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaVeic.insert(END, '%')
        veic = self.entradaVeic.get()

        self.conecta_Glac()
        self.cursor.execute("""SELECT cod_sp, servprod, hor, custo, valor, descricao, id_marcaprod,
            tiposerv, sistemaserv FROM servprod WHERE id_marcaprod LIKE '%s'  """ % veic)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            self.listaServ.insert("", END, values=i)
        self.entradaVeic.delete(0, END)
        self.desconecta_Glac()

    def busca_servicoS(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaServ.insert(END, '%')
        self.conecta_Glac()

        servprod = self.entradaServ.get()
        self.cursor.execute("""SELECT cod_sp, servprod, hor, custo, valor, descricao,
        id_marcaprod, tiposerv, sistemaserv FROM servprod 
        WHERE servprod LIKE '%s'  """ % servprod)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            self.listaServ.insert("", END, values=i)
        self.entradaServ.delete(0, END)

        self.desconecta_Glac()

    def add_servS(self):
        self.listaServ.delete(*self.listaServ.get_children())
        cod_sp = self.entradaCod.get()
        servprod = self.entradaServ.get()
        hor = self.entradaHor.get()
        custo = self.entradaCustohora.get()
        valor = self.entradaValorhora.get()
        tiposerv = self.entradaTipoServ.get()
        sistemaserv = self.entradaSistemaServ.get()
        descricao = self.entradaDescricao.get()
        veic = self.entradaVeic.get()
        id_marcaprod = self.entradaDescricao.get()

        self.conecta_Glac()
        self.cursor.execute("""INSERT INTO servprod ( servprod, hor, custo, valor, tiposerv, 
        sistemaserv, sp, descricao, id_marcaprod) VALUES ( ?, ?, ?, ?, ?, ?, "S", ?, ?)""",
        (servprod, hor, custo, valor, tiposerv, sistemaserv, descricao, id_marcaprod))
        self.conn.commit()
        lista = self.cursor.execute("""SELECT cod_sp, servprod, hor, custo , valor, 
        descricao , id_marcaprod, tiposerv, sistemaserv FROM servprod  
        WHERE sp = "S" ORDER BY cod_sp DESC; """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()