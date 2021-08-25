from Janelas.estiloWidgets.widgets_Glac import *
from pycep_correios import get_address_from_cep, WebService, exceptions


class CadForn:
    def list_fornec(self):
        self.conecta_Glac()
        lista = self.cursor.execute("""SELECT cod_forn, fornecedor, fone, municipio 
                FROM fornecedores ORDER BY fornecedor ASC;""")

        rows = self.cursor.fetchall()
        for row in rows:
            self.list_g.insert("", END, values=row)

        self.desconecta_Glac()

    def var_fornec(self):
        self.cod_forn = self.entr_cd_for.get()
        self.fornecedor = self.entr_for.get()
        self.fone = self.entr_fone.get()
        self.cnpj = self.entr_cnpj.get()
        self.cep = self.entr_cep.get()
        self.endereco = self.entr_end.get()
        self.municipio = self.entr_mun.get()
        self.descricao = self.entr_dscr.get()

    def OnDoubleClickForn(self, event):
        self.limpa_fornecedor()
        self.list_g.selection()

        for n in self.list_g.selection():
            col1, col2, col3, col4 = self.list_g.item(n, 'values')
            self.entr_cd_for.insert(END, col1)
        self.carrega_fornecedor()

    def mud_fornec(self):
        self.var_fornec()
        self.conecta_Glac()
        self.cursor.execute("""UPDATE fornecedores SET 
        fornecedor = ?, fone = ?, cnpj = ?, cep = ?, endereco = ?, municipio = ?,
        descricao = ? WHERE cod_forn = ?""",
        (self.fornecedor, self.fone, self.cnpj, self.cep, self.endereco, self.municipio,
         self.descricao, self.cod_forn))
        self.conn.commit()
        self.list_g.delete(*self.list_g.get_children())
        self.desconecta_Glac()

        self.list_fornec()
        msg = "Dados do fornecedor alterados com sucesso"
        messagebox.showinfo("GLAC ", msg)

    def limpa_fornecedor(self):
        self.entr_cd_for.delete(0, END)
        self.entr_for.delete(0, END)
        self.entr_fone.delete(0, END)
        self.entr_cnpj.delete(0, END)
        self.entr_cep.delete(0, END)
        self.entr_end.delete(0, END)
        self.entr_mun.delete(0, END)
        self.entr_dscr.delete(0, END)

    def del_fornec(self):
        self.conecta_Glac()

        cod_forn = self.entr_cd_for.get()
        self.cursor.execute("""DELETE FROM fornecedores WHERE cod_forn=?""", (cod_forn,))
        self.conn.commit()
        self.list_g.delete(*self.list_g.get_children())
        self.desconecta_Glac()

        self.list_fornec()
        msg = "Fornecedor excluido com sucesso.  :("
        messagebox.showinfo("GLAC ", msg)

    def carrega_fornecedor(self):
        self.conecta_Glac()
        cod_forn = self.entr_cd_for.get()

        self.limpa_fornecedor()
        self.cursor.execute("""SELECT fornecedor, fone, cnpj, cep, endereco, municipio, descricao 
            FROM fornecedores WHERE cod_forn = '%s'""" % cod_forn)
        consultafornec = self.cursor.fetchall()
        for i in consultafornec:
            self.entr_cd_for.insert(END, cod_forn)
            self.entr_for.insert(END, i[0])
            self.entr_fone.insert(END, i[1])
            self.entr_cnpj.insert(END, i[2])
            self.entr_cep.insert(END, i[3])
            self.entr_end.insert(END, i[4])
            self.entr_mun.insert(END, i[5])
            self.entr_dscr.insert(END, i[6])
        self.desconecta_Glac()

    def cepForn(self):
        self.entr_end.delete(0, END)
        self.entr_mun.delete(0, END)
        try:
            self.cep = self.entr_cep.get()
            endereco = get_address_from_cep(self.cep, webservice=WebService.APICEP)

            self.entr_end.insert(END, endereco['logradouro'])
            self.entr_end.insert(END, ' - ')
            self.entr_end.insert(END, endereco['bairro'])

            self.entr_mun.insert(END, endereco['cidade'])
            self.entr_mun.insert(END, ' - ')
            self.entr_mun.insert(END, endereco['uf'])
        except:
            msg = "Cep não encontrado"
            messagebox.showinfo("GLAC ", msg)

    def busca_fornecedor(self):
        self.conecta_Glac()

        self.entr_for.insert(END, '%')
        self.list_g.delete(*self.list_g.get_children())
        fornecedor = self.entr_for.get()

        lista = self.cursor.execute("""SELECT cod_forn, fornecedor, fone, municipio 
        FROM fornecedores WHERE fornecedor LIKE '%s' ORDER BY fornecedor ASC;""" % fornecedor)
        rows = self.cursor.fetchall()
        for row in rows:
            self.list_g.insert("", END, values=row)
            self.entr_for.delete(0, END)
        self.desconecta_Glac()

    def add_fornec(self):
        self.conecta_Glac()
        self.list_g.delete(*self.list_g.get_children())
        self.var_fornec()

        self.cursor.execute("""INSERT INTO fornecedores 
        (fornecedor, fone, cnpj, cep, endereco, municipio, descricao)
        VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
        (self.fornecedor, self.fone, self.cnpj, self.cep, self.endereco,
         self.municipio, self.descricao))
        self.conn.commit()
        self.desconecta_Glac()

        self.list_fornec()
        msg = "Novo fornecedor incluido com sucesso"
        messagebox.showinfo("GLAC ", msg)
