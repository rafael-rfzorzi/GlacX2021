from Janelas.estiloWidgets.widgets_Glac import *

class CadMarcaProd:
    def OnDoubleClickMarc(self, event):
        self.limpa_marca_prod()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3 = self.listaServ.item(n, 'values')
            self.entradaCod.insert(END, col1)

        self.carrega_marca_prod()
    def mud_marca_prod(self):
        self.conecta_Glac()

        cod_marca = self.entradaCod.get()
        marca = self.entradaMarca.get()
        descricao = self.entradaDescricao.get()

        self.cursor.execute("""
     		UPDATE marcaprod SET marca = ? WHERE cod_marca = ?""", (marca, cod_marca))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE marcaprod SET descricao = ? WHERE cod_marca = ?""", (descricao, cod_marca))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        listacod = self.cursor.execute("""SELECT cod_marca, marca, descricao FROM marcaprod ORDER BY marca ASC ;
     		""")
        for i in listacod:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def carrega_marca_prod(self):
        cod_marca = self.entradaCod.get()
        self.conecta_Glac()

        marcaprod = self.cursor

        self.entradaMarca.delete(0, END)
        self.entradaDescricao.delete(0, END)

        marcaprod.execute("SELECT marca FROM marcaprod WHERE cod_marca = '%s'" % cod_marca)
        consultamarcaprod = self.cursor.fetchall()
        for i in consultamarcaprod:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaMarca.insert(END, i)

        descricao = self.cursor
        descricao.execute("SELECT descricao FROM marcaprod WHERE cod_marca = '%s'" % cod_marca)
        consultadescricao = self.cursor.fetchall()
        for i in consultadescricao:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaDescricao.insert(END, i)

        self.desconecta_Glac()
    def del_marca_prod(self):

        conn = sqlite3.connect("glac.db")
        cursor = self.conn.cursor()
        cod_marca = self.entradaCod.get()
        self.cursor.execute("""
     		DELETE FROM marcaprod WHERE cod_marca=?""", (cod_marca,))
        conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
     		SELECT cod_marca, marca, descricao FROM marcaprod ORDER BY marca ASC ;
     		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)
        conn.close()
    def limpa_marca_prod(self):
        self.entradaCod.delete(0, END)
        self.entradaMarca.delete(0, END)
        self.entradaDescricao.delete(0, END)
    def add_marca_prod(self):
        self.conecta_Glac()

        cod_marca = self.entradaCod.get()
        marca = self.entradaMarca.get()
        descricao = self.entradaDescricao.get()
        self.listaServ.delete(*self.listaServ.get_children())
        self.cursor.execute("""
     		INSERT INTO marcaprod ( marca, descricao)
     		VALUES ( ?, ?)""",  (marca, descricao))
        self.conn.commit()
        lista = self.cursor.execute("""
             SELECT cod_marca, marca, descricao 
             FROM marcaprod ORDER BY marca ASC ;
     		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def busca_marca_prod(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaMarca.insert(END, '%')
        self.conecta_Glac()
        marca = self.entradaMarca.get()
        marcap = self.cursor

        marcap.execute("SELECT * FROM marcaprod "
                       "WHERE marca LIKE '%s'" % marca)
        buscamarca = self.cursor.fetchall()
        for i in buscamarca:
            self.listaServ.insert("", END, values=i)
        self.entradaMarca.delete(0, END)

        self.desconecta_Glac()
