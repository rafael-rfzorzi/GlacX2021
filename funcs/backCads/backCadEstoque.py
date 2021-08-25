from Janelas.estiloWidgets.widgets_Glac import *


class CadEstoque:
    def add_movE(self):
        self.conecta_Glac()

        cod2 = self.codproduto2.get()
        prod2 = self.produto_aba2.get()
        dia = self.dia_aba2.get()
        lote = self.lote_aba2.get()
        diaV = self.diaV_aba2.get()
        quant = self.quant_aba2.get()
        custo = self.custo_aba2.get()
        fornecedor = self.entradaIdFornec.get()
        saida = self.saida_aba2.get()
        self.listaMov.delete(*self.listaMov.get_children())

        self.cursor.execute("""INSERT INTO movim_prod ( cod_p, entrada, custo, dia, 
        lote, diaV, fornecedor, saida) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)""",
        (cod2, quant, custo, dia, lote, diaV, fornecedor, saida))
        self.conn.commit()

        msg = "Movimentação realizada.\n "
        msg += ""
        messagebox.showinfo("GLAC - Estoque", msg)

        lista1 = self.cursor.execute("""SELECT lote, entrada, saida, custo, dia, 
            fornecedores.fornecedor, diaV FROM movim_prod, fornecedores	
    	    WHERE cod_p = '%s' and movim_prod.fornecedor = fornecedores.cod_forn 
    	    ORDER BY id ASC; """ % cod2)
        for i in lista1:
            self.listaMov.insert("", END, values=i)

        self.quantest.delete(0, END)

        lista2 = self.cursor.execute("""select Sum(entrada) - Sum(saida) 
            from movim_prod where cod_p = '%s'""" % cod2)
        consultalista2 = self.cursor.fetchall()
        for i in consultalista2:
            self.quantest.insert(END, i)

        self.desconecta_Glac()

    def add_produtoE(self):
        self.conecta_Glac()
        cod_sp = self.entradaCodprod.get()
        servprod = self.entradaProd.get()
        id_marcaprod = self.entradaIdMarcaprod.get()
        id_fornec = self.entradaIdFornec.get()
        custo = self.entradaCusto.get()
        valor = self.entradaValor.get()
        descricao = self.entradaDescricao.get()

        self.cursor.execute("""
            INSERT INTO servprod ( servprod, id_marcaprod, id_fornec, custo, valor, sp, descricao)
        	VALUES ( ?, ?, ?, ?, ?, "P", ?)""",
                       (servprod, id_marcaprod, id_fornec, custo, valor, descricao))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
        	SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
        	WHERE sp = "P" AND  servprod LIKE '%s' ORDER BY servprod ASC;
        	""" % servprod)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()

    def OnDoubleClickE(self, event):
        self.limpa_produtoE()
        self.listaServ.selection()
        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServ.item(n, 'values')
            self.entradaCodprod.insert(END, col1)
        self.carrega_produtoE()

    def mud_produtoE(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        servprod = self.entradaProd.get()
        id_marcaprod = self.entradaIdMarcaprod.get()
        id_fornec = self.entradaIdFornec.get()
        custo = self.entradaCusto.get()
        valor = self.entradaValor.get()
        descricao = self.entradaDescricao.get()
        self.cursor.execute("""UPDATE servprod SET servprod = ?, id_marcaprod = ?, 
        id_fornec = ?, custo = ?, valor = ?, descricao = ? WHERE cod_sp = ?""",
        (servprod, id_marcaprod, id_fornec, custo, valor, descricao, cod_sp))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""SELECT cod_sp, servprod, "R$", custo, "R$", valor 
        FROM servprod WHERE sp = "P" ORDER BY servprod ASC; """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()

    def limpa_produtoE(self):
        self.entradaProd.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaCusto.delete(0, END)
        self.entradaValor.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaFornec.delete(0, END)
        self.entradaCodprod.delete(0, END)
        self.codproduto2.delete(0, END)
        self.produto_aba2.delete(0, END)
        self.custo_aba2.delete(0, END)

    def del_produtoE(self):
        self.conecta_Glac()
        cod_sp = self.entradaCodprod.get()
        self.cursor.execute("""DELETE FROM servprod WHERE cod_sp=?""", (cod_sp,))
        conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""SELECT cod_sp, servprod, "R$", custo, "R$", valor
        FROM servprod WHERE sp = "P" ORDER BY servprod ASC;	""")
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()

    def carrega_produtoE(self):
        self.conecta_Glac()
        cod_sp = self.entradaCodprod.get()
        prod = self.cursor
        cod2 = self.codproduto2.get()

        self.entradaProd.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaCusto.delete(0, END)
        self.entradaValor.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaMarcaprod.delete(0, END)
        self.entradaFornec.delete(0, END)
        self.codproduto2.delete(0, END)
        self.produto_aba2.delete(0, END)
        self.custo_aba2.delete(0, END)
        self.quantest.delete(0, END)
        self.listaMov.delete(*self.listaMov.get_children())

        self.codproduto2.insert(END, cod_sp)
        self.cursor.execute("""SELECT servprod, id_marcaprod, marca, id_fornec, custo,
        valor, servprod.descricao
        FROM servprod, marcaprod WHERE cod_marca = id_marcaprod AND cod_sp = '%s'""" % cod_sp)
        consultaprod = self.cursor.fetchall()
        for i in consultaprod:
            self.entradaProd.insert(END, i[0])
            self.produto_aba2.insert(END, i[0])
            self.entradaIdMarcaprod.insert(END, i[1])
            self.entradaMarcaprod.insert(END, i[2])
            self.entradaIdFornec.insert(END, i[3])
            self.entradaCusto.insert(END, i[4])
            self.custo_aba2.insert(END, i[4])
            self.entradaValor.insert(END, i[5])
            self.entradaDescricao.insert(END, i[6])

        ff = self.entradaIdFornec.get()
        self.cursor.execute("SELECT fornecedor FROM fornecedores WHERE cod_forn = '%s'" % ff)
        consultaidfornec = self.cursor.fetchall()
        for i in consultaidfornec:
            self.entradaFornec.insert(END, i[0])

        self.cursor.execute("""SELECT lote, entrada, saida, custo, dia, 
        fornecedor, diaV FROM movim_prod WHERE cod_p = '%s' ORDER BY id ASC; """ % cod_sp)
        listam = self.cursor.fetchall()
        for i in listam:
            self.listaMov.insert("", END, values=i)

        lista2 = self.cursor.execute("""select Sum(entrada) - Sum(saida) 
        from movim_prod where cod_p = '%s'""" % cod_sp)
        consultalista2 = self.cursor.fetchall()
        for i in consultalista2:
            self.quantest.insert(END, i)

    def busca_produtoE(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaProd.insert(END, '%')
        servprod = self.entradaProd.get()

        self.conecta_Glac()

        lista = self.cursor.execute("""
       		SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
       		WHERE sp = "P" AND  servprod LIKE '%s' ORDER BY servprod ASC;
       		""" % servprod)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.entradaProd.delete(0, END)

        self.desconecta_Glac()

    def add_movF(self):
        self.conecta_Glac()
        cursor = self.conn.cursor()
        cod2 = self.codproduto2.get()
        prod2 = self.produto_aba2.get()
        dia = self.dia_aba2.get()
        lote = self.lote_aba2.get()
        diaV = self.diaV_aba2.get()
        quant = self.quant_aba2.get()
        custo = self.custo_aba2.get()
        fornecedor = self.entradaIdFornec.get()
        saida = self.saida_aba2.get()
        self.listaMov.delete(*self.listaMov.get_children())

        self.cursor.execute("""INSERT INTO movim_prod ( cod_p, entrada, custo, dia,	
        lote, diaV, fornecedor, saida) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)""",
        (cod2, quant, custo, dia, lote, diaV, fornecedor, saida))
        conn.commit()

        msg = "Movimentação realizada.\n "
        msg += ""
        messagebox.showinfo("GLAC - Estoque", msg)

        lista1 = self.cursor.execute("""SELECT  lote, entrada, saida, custo, dia, 
        fornecedores.fornecedor, diaV, mesV, anoV 
        FROM movim_prod WHERE cod_p = '%s' 
        INNER JOIN movim_prod.fornecedor = fornecedores.cod_forn ORDER BY id ASC; """ % cod2)
        for i in lista1:
            self.listaMov.insert("", END, values=i)

        self.quantest.delete(0, END)

        self.cursor.execute("""select Sum(entrada) - Sum(saida) 
        from movim_prod where cod_p = '%s'""" % cod2)
        consultalista2 = cursor.fetchall()
        for i in consultalista2:
            self.quantest.insert(END, i)
        self.desconecta_Glac()

    def add_autobind(self, event):
        self.listatec1.selection()

        for n in self.listatec1.selection():
            col1, col2 = self.listatec1.item(n, 'values')
            self.entradaFornec.insert(END, col2)
            self.entradaIdFornec.insert(END, col1)

        self.listatec.destroy()

    def OnTec(self, *args):
        self.listatec1.yview(*args)

    def add_autobind2(self, event):
        self.listatec1.selection()
        for n in self.listatec1.selection():
            col1, col2 = self.listatec1.item(n, 'values')
            self.entradaMarcaprod.insert(END, col2)
            self.entradaIdMarcaprod.insert(END, col1)

        self.listatec.destroy()
