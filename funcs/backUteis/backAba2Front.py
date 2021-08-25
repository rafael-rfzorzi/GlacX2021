from tkinter import *
from tkinter import messagebox


class Aba2:
    def add_servico1(self):
        self.codVazio = self.codServ1.get()
        if self.codVazio == '':
            self.capturaCod = self.listaCol2a.get()
            capcod = str(self.capturaCod).replace("(", " ").replace("'", " ").replace("*", " ")
            capcod2 = capcod[0:7].strip()
            self.codServ1.insert(END, capcod2)
            self.listaCol2a.delete(0, END)
            self.listaCol4a.delete(0, END)
            self.conecta_Glac()
            cod_sp = self.codServ1.get()
            addserv2 = self.cursor
            addserv2.execute("""SELECT UPPER(servprod), ' - ', UPPER(tiposerv), ' - ' , UPPER(id_marcaprod), '##' 
                FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
            addservico2 = self.cursor.fetchall()
            for i in addservico2:
                i = str(i)
                i = i.replace('(', '')
                i = i.replace(')', '')
                i = i.replace("'", "")
                i = i.replace(',', '')
                self.listaCol2a.insert(END, i)

            self.listaCol3a.delete(0, END)
            self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
            addservico3 = self.cursor.fetchall()
            for i in addservico3:
                self.listaCol3a.insert(END, i)

            self.cursor.execute("""SELECT  valor  FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
            addservico4 = self.cursor.fetchall()
            for i in addservico4:
                self.listaCol4a.insert(END, i)

            quant1 = float(self.listaCol3a.get())
            valor1 = float(self.listaCol4a.get())
            self.total1 = quant1 * valor1
            self.total1 = float(self.total1)

            self.listaCol5a.delete(0, END)
            self.listaCol5a.insert(END, self.total1)

            self.desconecta_Glac()
            self.listaServP1.destroy()
            print(capcod[0:7])
        else:
            self.listaCol2a.delete(0, END)
            self.listaCol4a.delete(0, END)

            self.conecta_Glac()

            cod_sp = self.codServ1.get()

            addserv2 = self.cursor
            addserv2.execute("""SELECT UPPER(servprod), ' - ', UPPER(tiposerv), ' - ' , UPPER(id_marcaprod), '##' 
                FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
            addservico2 = self.cursor.fetchall()
            for i in addservico2:
                i = str(i);
                i = i.replace('(', '');
                i = i.replace(')', '');
                i = i.replace("'", "");
                i = i.replace(',', '')
                self.listaCol2a.insert(END, i)

            self.listaCol3a.delete(0, END)
            self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
            addservico3 = self.cursor.fetchall()
            for i in addservico3:
                self.listaCol3a.insert(END, i)

            addserv4 = self.cursor
            addserv4.execute("""SELECT  valor  FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
            addservico4 = self.cursor.fetchall()
            for i in addservico4:
                self.listaCol4a.insert(END, i)

            quant1 = self.listaCol3a.get()
            quant1 = float(quant1)
            valor1 = self.listaCol4a.get()
            valor1 = float(valor1)
            self.total1 = quant1 * valor1
            self.total1 = float(self.total1)

            self.listaCol5a.delete(0, END)
            self.listaCol5a.insert(END, self.total1)

            self.desconecta_Glac()

    def busca_servico1(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico1bind)

    def add_itens_orc(self):
        id_orc = self.listaNumOrc.get()
        cod_item1 = self.codServ1.get()
        desc_item1 = self.listaCol2a.get()
        valor1 = self.listaCol4a.get()
        quant1 = self.listaCol3a.get()
        total1 = self.listaCol5a.get()

        if id_orc == '':
            msg = 'Para Inserir um item é necessário que um orçamento ou O.S ' \
                  'esteja aberta!!! Clique em ' \
                  'gravar para abrir novo chamado ou buscar para editar um já ' \
                  'existente.'
            messagebox.showerror("GLAC ", msg)
            self.codServ1.delete('0', 'end')
            self.listaCol2a.delete('0', 'end')
            self.listaCol4a.delete('0', 'end')
            self.listaCol3a.delete('0', 'end')
            self.listaCol5a.delete('0', 'end')
        else:
            self.conecta_Glac()

            numeroItemOrc = self.cursor
            numeroItemOrc.execute("""SELECT MAX(ordem_item) 
                FROM orcamento2 WHERE id_orc2 = '%s'""" % id_orc)
            buscaNumItem = self.cursor.fetchall()
            for i in buscaNumItem:
                i = str(i);
                i = i.replace('(', '');
                i = i.replace(')', '');
                i = i.replace("'", "");
                i = i.replace(',', '')
                print(i)
                if i == 'None':
                    total1 = total1.replace('(', '')
                    total1 = total1.replace(')', '')
                    total1 = total1.replace("'", "")
                    total1 = total1.replace(',', '.')
                    total1 = total1.replace('R$', '')
                    i = int(1)
                    self.cursor.execute("""	
                        INSERT INTO orcamento2 ( id_orc2, cod_item, 
                        desc_item, valor, quant, total, ordem_item) 
                        VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                            (id_orc, cod_item1, desc_item1,
                             valor1, quant1, total1, i))
                    self.conn.commit()
                else:
                    total1 = total1.replace('(', '')
                    total1 = total1.replace(')', '')
                    total1 = total1.replace("'", "")
                    total1 = total1.replace(',', '.')
                    total1 = total1.replace('R$', '')
                    i = int(i)
                    tItem = int(i + 1)
                    self.cursor.execute("""	
                        INSERT INTO orcamento2 ( id_orc2, cod_item, 
                        desc_item, valor, quant, total, ordem_item) 
                        VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                            (id_orc, cod_item1, desc_item1, valor1,
                             quant1, total1, tItem))
                    self.conn.commit()

            #################
            self.listaServProd.delete(*self.listaServProd.get_children())
            lista = self.cursor.execute("""
                SELECT ordem_item, desc_item, cod_item, 
                valor, quant, total 
                FROM orcamento2 WHERE id_orc2 = '%s' """ % id_orc)
            rows = self.cursor.fetchall()
            for row in rows:
                self.listaServProd.insert("", END, values=row)
            self.desconecta_Glac()
            self.codServ1.delete('0', 'end')
            self.listaCol2a.delete('0', 'end')
            self.listaCol4a.delete('0', 'end')
            self.listaCol3a.delete('0', 'end')
            self.listaCol5a.delete('0', 'end')
            self.total_orc()

    def OnVsb_Orc2(self, *args):
        self.listaServProd.yview(*args)

    def altera_itens_orc_deletabt2(self, event):
        numorc = self.listaNumOrc.get();
        self.listaServProd.selection()
        for n in self.listaServProd.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServProd.item(n,
                'values')
            self.conecta_Glac()
            self.cursor.execute("""DELETE FROM orcamento2 
            WHERE ordem_item = ? AND id_orc2 = ?""", (col1, numorc,))

            self.conn.commit()

            self.desconecta_Glac()
            self.atualiza_listaServProd()
            self.total_orc()