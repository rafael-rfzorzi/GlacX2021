from tkinter import *
from tkinter import messagebox
import webbrowser



class Functions:

    def var_orc(self):
        self.id_orc = self.listaNumOrc.get()
        self.cod_item1 = self.codServ1.get()
        self.desc_item1 = self.listaCol2a.get()
        self.valor1 = self.listaCol4a.get()
        self.quant1 = self.listaCol3a.get()
        self.total1 = self.listaCol5a.get()

        self.cliente_orc = self.entradaCod_cli.get()
        self.placa_orc = self.placa.get()
        self.dia = self.entradaDataorc.get()
        self.descp1 = self.area1.get()
        self.descp2 = self.area2.get()
        self.descp3 = self.area3.get()
        self.descp4 = self.area4.get()
        self.totalizador = self.entradatotal.get()
        self.km = self.entradaObs.get()
        self.tecnico = self.entradaTecnico.get()
        self.tipoOrc = self.Tipvar.get()
        self.comp1 = self.listInicio.get()
        self.comp2 = self.listFim.get()

        self.tanque = self.are1.get()
        self.odometro = self.are2.get()
        self.radio = self.are3.get()
        self.calota = self.are4.get()
        self.triangulo = self.are5.get()
        self.macaco = self.are6.get()
        self.estepe = self.are7.get()
        self.obs1 = self.are8.get()
        self.obs2 = self.are9.get()

    def atualiza_listaServProd(self):
        self.var_orc()
        self.conecta_Glac()
        self.listaServProd.delete(*self.listaServProd.get_children())
        lista = self.cursor.execute("""SELECT ordem_item, desc_item, cod_item, valor, 
        quant, total FROM orcamento2 WHERE id_orc2 = '%s' """ % self.id_orc)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServProd.insert("", END, values=row)
        self.desconecta_Glac()

    def altera_itens_orc_quant2(self):
        valor = self.listaCol3a.get()
        quant = self.listaCol4a.get()
        total = self.listaCol5a.get()
        valor = float(valor)
        quant = float(quant)
        self.listaCol5a.delete('0', 'end')
        soma = valor * quant
        soma = float(f'{soma:>8.2f}')
        self.listaCol5a.insert(END, soma)

    def total_orc(self):
        self.var_orc()
        self.entradatotal.delete('0', 'end')
        totalizador = self.entradatotal.get()

        if self.id_orc == '':
            msg = 'Não é possivel calcular o Valor Total se nenhum '
            msg+= 'Orçamento ou Ordem de Serviço estiver selecionada.'
            messagebox.showerror("GLAC ", msg)
        else:
            self.conecta_Glac()
            self.cursor.execute("""SELECT SUM(total) FROM orcamento2 
                WHERE id_orc2 = '%s'""" % self.id_orc)
            buscaNumItem = self.cursor.fetchall()
            for i in buscaNumItem:
                if i == "":
                    self.entradatotal.insert(END, "00.00")
                else:
                    soma = float(i[0])
                    self.entradatotal.insert(END, f'{soma:.2f}')
            self.desconecta_Glac()

    def abre_orc(self):
        self.listaNumOrc.delete('0', 'end')
        self.var_orc()

        self.conecta_Glac()
        self.cursor.execute("""	INSERT INTO orcamento1 ( cliente_orc, placa_orc, descp1, 
        descp2, descp3, descp4, dia, tecnico, totalizador, tipoOrc, km, comp1, comp2)
    	VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (self.cliente_orc, self.placa_orc, self.descp1, self.descp2, self.descp3,
         self.descp4, self.dia, self.tecnico, self.totalizador, self.tipoOrc,
         self.km, self.comp1, self.comp2))

        self.conn.commit()

        self.cursor.execute("""INSERT INTO vistoria ( vist1, vist2, vist3, vist4, 
            vist5, vist6, vist7, vist8, vist9) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (self.tanque, self.radio, self.odometro, self.calota,
             self.triangulo, self.macaco, self.estepe, self.obs1, self.obs2))

        self.conn.commit()
        self.cursor.execute("""SELECT MAX(id_orc1) FROM orcamento1""")
        buscanomecli = self.cursor.fetchall()
        for i in buscanomecli:
            self.listaNumOrc.insert(0, i)

        self.desconecta_Glac()
        self.total_orc()
        msg = "Orçamento gravado com sucesso."
        messagebox.showinfo("GLAC - Orçamento", msg)

    def altera_orc(self):
        self.var_orc()
        self.conecta_Glac()
        self.cursor.execute("""
            UPDATE orcamento1 SET id_orc1 = ?, cliente_orc = ?, placa_orc = ?, dia = ?,
    		descp1 = ?, descp2 = ?, descp3 = ?, descp4 = ?, totalizador = ?, km = ?,
    		tecnico = ?, tipoOrc = ? , comp1 = ?, comp2 = ? WHERE id_orc1 = ?""",
            (self.id_orc, self.cliente_orc, self.placa_orc, self.dia, self.descp1,
             self.descp2, self.descp3, self.descp4, self.totalizador, self.km, self.tecnico,
             self.tipoOrc, self.comp1, self.comp2, self.id_orc))
        self.conn.commit()

        self.desconecta_Glac()
        self.conecta_Glac()

        self.cursor.execute("""
    			UPDATE vistoria SET vist1 = ?, vist2 = ?, vist3 = ?, vist4 = ?, vist5 = ?,
    			vist6 = ? , vist7 = ?, vist8 = ?, vist9 = ? WHERE cod = ? """,
                (self.tanque, self.radio, self.odometro, self.calota, self.triangulo,
                 self.macaco, self.estepe, self.obs1, self.obs2, self.id_orc))
        self.conn.commit()

        self.desconecta_Glac()
        self.total_orc()
        msg = "Alterações realizadas com sucesso.\n "
        msg += ""
        messagebox.showinfo("GLAC - Orçamento", msg)

    def buscanomeorc(self):
        self.listaNomeO.insert(END, '%')
        self.listaServ.delete(*self.listaServ.get_children())

        nomeO = self.listaNomeO.get()
        self.conecta_Glac()
        self.cursor.execute("""SELECT id_orc1, nome ,dia , placa_orc, orcamento1.tipoOrc 
        FROM orcamento1, clientes WHERE  cod_cli = cliente_orc AND nome LIKE '%s' 
        ORDER BY id_orc1 DESC""" % nomeO)
        buscanomeO = self.cursor.fetchall()
        for row in buscanomeO:
            self.listaServ.insert("", END, values=row)
        self.listaNomeO.delete(0, END)
        self.desconecta_Glac()

    def buscaplacaorc(self):
        self.listaPlaca.insert(END, '%')
        self.listaServ.delete(*self.listaServ.get_children())
        placaO = self.listaPlaca.get()
        self.conecta_Glac()

        self.cursor.execute("""SELECT id_orc1, nome, dia , placa_orc, orcamento1.tipoOrc 
        FROM orcamento1, clientes WHERE cod_cli = cliente_orc 
        AND placa_orc LIKE '%s'""" % placaO)
        buscaplac = self.cursor.fetchall()
        for row in buscaplac:
            self.listaServ.insert("", END, values=row)

        self.listaPlaca.delete(0, END)
        self.desconecta_Glac()

    def carrega_orc(self, event):
        self.var_orc()
        self.limpa_cliente()
        self.entradaDataorc.delete('0', 'end')
        self.entradatotal.delete('0', 'end')
        self.listaNumOrc.delete('0', 'end')
        self.entradaTecnico.delete('0', 'end')
        self.listaServ.selection()

        self.conecta_Glac()
        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5 = self.listaServ.item(n, 'values')
            self.listaNumOrc.insert(0, col1)
        id_orc = self.listaNumOrc.get()

        self.entradaCod_aut.delete('0', 'end')
        self.entradaDataorc.delete('0', 'end')

        self.cursor.execute("""SELECT cliente_orc, placa_orc, descp1, descp2, descp3, descp4,
            dia, totalizador, km, comp1, comp2, tecnico, tipoOrc 
            FROM orcamento1 WHERE id_orc1 = '%s'""" % id_orc)
        consultanome = self.cursor.fetchall()
        for i in consultanome:
            self.entradaCod_cli.insert(0, i[0])
            self.placa.insert(0, i[1])
            self.area1.insert(0, i[2])
            self.area2.insert(0, i[3])
            self.area3.insert(0, i[4])
            self.area4.insert(0, i[5])
            self.entradaDataorc.insert(0, i[6])
            self.entradatotal.insert(0, i[7])
            self.entradaObs.insert(0, i[8])
            self.listInicio.insert(0, i[9])
            self.listFim.insert(0, i[10])
            self.entradaTecnico.insert(0, i[11])
            self.Tipvar.set(i[12])
        self.desconecta_Glac()
        self.carrega_cliente()
        self.conecta_Glac()
        #
        placa = self.placa.get()
        self.cursor.execute("""SELECT UPPER(veiculo), ano, montadora, UPPER(combust), 
        UPPER(cor) FROM frota WHERE placa = '%s'""" % placa)
        consultaautomovel = self.cursor.fetchall()
        for i in consultaautomovel:
            self.listAut.insert(0, i[0])
            self.listAno.insert(0, i[1])
            self.listMarca.insert(0, i[2])
            self.listCombustivel.insert(0, i[3])
            self.listCor.insert(0, i[4])

        self.listaServProd.delete(*self.listaServProd.get_children())
        self.cursor.execute("""
            SELECT ordem_item, desc_item, cod_item, valor, quant, total 
            FROM orcamento2 WHERE id_orc2 = '%s' """ % id_orc)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServProd.insert("", 0, values=row)

        self.cursor.execute("""SELECT vist1, vist2, vist3, vist4, vist5, vist6, vist7, 
        vist8, vist9 FROM vistoria WHERE cod = '%s' """ % id_orc)
        codVisto = self.cursor.fetchall()
        for i in codVisto:
            self.are1.insert(0, i[0])
            self.are3.insert(0, i[1])
            self.are2.insert(0, i[2])
            self.are4.insert(0, i[3])
            self.are5.insert(0, i[4])
            self.are6.insert(0, i[5])
            self.are7.insert(0, i[6])
            self.are8.insert(0, i[7])
            self.are9.insert(0, i[8])
        self.listaOrc.destroy()
        self.desconecta_Glac()
        self.total_orc()

    def OnDoubleClick(self, event):
        self.limpa_cliente()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5 = listaServ.item(n, 'values')
            self.entradan.insert(END, col1)

        self.carrega_orc()

    def backup(self):
        try:
            shutil.copyfile("c:\glacx\glac.db", "c:\glacbkp\copiaGlacX.db")
            msg = "Backup salvo em c:\glacbkp\ \n" \
                 "Copie e salve em local seguro. ;) "
            msg += ""
            messagebox.showinfo("GLACX", msg)
        except:
            msg = "Copia não realizada, crie a pasta c:\glacbkp \n" \
                  "antes de realizar o backup"
            messagebox.showinfo("GLACX", msg)

    def busca_serv(self):
        # self.listaServ1.delete(0, END)
        self.listaServ1.delete(*self.listaServ1.get_children())
        self.listaServicos1.insert(END, '%')

        self.conecta_Glac()

        servprod = self.listaServicos1.get()

        self.cursor.execute("""SELECT cod_sp, servprod, tiposerv, hor, descricao, id_marcaprod, sistemaserv, valor * hor
    	FROM servprod WHERE servprod LIKE '%s' """ % servprod)
        buscaservico12 = self.cursor.fetchall()
        for i in buscaservico12:
            self.listaServ1.insert("", END, values=i)
        self.listaServicos1.delete(0, END)
        self.desconecta_Glac()

    def OnVsb_S1F(self, *args):
        self.listaServ1F.yview(*args)

    def busca_servF(self):
        # self.listaServ1.delete(0, END)
        self.listaServ1F.delete(*self.listaServ1F.get_children())
        self.listaServicos1F.insert(END, '%')

        self.conecta_Glac()
        servprodF = self.listaServicos1F.get()
        self.cursor.execute("""SELECT cod_falha, falha, falha2 FROM codfalha 
        WHERE falha LIKE '%s' """ % self.servprodF)
        buscaservico12F = self.cursor.fetchall()
        for i in buscaservico12F:
            self.listaServ1F.insert("", END, values=i)

        self.listaServicos1F.delete(0, END)
        self.desconecta_Glac()

    def PaginaRf(self):
        webbrowser.open("https://www.facebook.com/rfzorzi/")

    def buscaCli(self):
        self.conecta_Glac()
        self.EntryCliente2.insert(END, '%')
        nome = self.EntryCliente2.get()
        nomecod = self.cursor
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
            SELECT cod_cli, nome FROM clientes WHERE nome LIKE '%s' 
            """ % nome)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)
        self.EntryCliente2.delete(0, END)
        self.desconecta_Glac()

    def carrega_cliente2C(self, event):
        self.limpa_clienteC()
        pos = int(self.listaServ2.curselection()[0])
        cod_cli = self.listaServ2.get(pos)
        self.cursor.execute("SELECT cod_cli FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacod = cursor.fetchall()
        for i in consultacod:
            self.entradaCod_clicC.insert(END, i)
        self.carrega_clienteC()

    def busca_serv_veic(self):
        # self.listaServ1.delete(0, END)
        self.listaServ1.delete(*self.listaServ1.get_children())
        self.listaServicos1.insert(END, '%')

        servprod = self.listaServicos1.get()

        self.conecta_Glac()

        self.cursor.execute("""SELECT cod_sp, servprod, tiposerv, hor, descricao, 
        id_marcaprod, sistemaserv, valor * hor	FROM servprod 
        WHERE id_marcaprod LIKE '%s' """ % servprod)
        buscaservico12 = self.cursor.fetchall()
        for i in buscaservico12:
            self.listaServ1.insert("", END, values=i)

        self.listaServicos1.delete(0, END)

        self.desconecta_Glac()

    def OnVsb(self, *args):
        self.listaServ.yview(*args)

    def OnVsb_S1(self, *args):
        self.listaServ1.yview(*args)

    def OnVsb_Orc(self, *args):
        self.listaServ.yview(*args)

    def totalbotao(self):
        self.var_orc()

        self.conecta_Glac()
        self.cursor.execute("""SELECT SUM(total) FROM orcamento2 
            WHERE id_orc2 = '%s' """ % self.id_orc)
        total1 = self.cursor.fetchall()
        total = float(total1[0])

        self.desconecta_Glac()

        self.entradatotal.delete(0, END)
        self.entradatotal.insert(END, f'{total:.2f}')

    def add_servico1bind(self, event):
        self.codServ1.delete(0, END)
        self.listaCol2a.delete(0, END)
        self.listaCol4a.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ1.insert(END, col1)

        self.add_servico1()
        self.listaServP1.destroy()

    def sel_lists_tps(self):
        self.conecta_Glac()
        self.cursor.execute("""SELECT ano_dscr FROM ano; """ )
        self.rows_ano_dscr = self.cursor.fetchall()
        self.desconecta_Glac()
        self.rows_ano_dscr = list(self.rows_ano_dscr)

        self.conecta_Glac()
        self.cursor.execute("""SELECT mes_dscr FROM meses; """)
        self.rows_meses_dscr = self.cursor.fetchall()
        self.desconecta_Glac()
        self.rows_meses_dscr = list(self.rows_meses_dscr)

        self.tipos_pag = {self.m_Debito, self.m_Credito, self.m_Dinheiro, self.m_Boleto,
            self.m_ChequePre, self.m_ChequeVista, self.m_Crediario, self.m_Promissoria,
            self.m_Desconto, self.m_Avista}
        self.tipos_pag = sorted(self.tipos_pag)

        self.sim_nao = {self.m_Sim, self.m_Nao}
        self.sim_nao = sorted(self.sim_nao)

    def format_cpf_cnpj(self, event):
        if self.open_win_cli == "cadcli":
            valid_cpf_mat = self.cnpj_mat_str.get()
            if valid_cpf_mat == "CNPJ":
                text = self.cnpj_mat_ent.get().replace(".", "").replace("/", "").replace("-", "")[:14]
                new_text = ""
                if event.keysym.lower() == "backspace": return

                for index in range(len(text)):
                    if not text[index] in "0123456789": continue
                    if index in [1, 4]:
                        new_text += text[index] + "."
                    elif index == 7:
                        new_text += text[index] + "/"
                    elif index == 11:
                        new_text += text[index] + "-"
                    else:
                        new_text += text[index]

                self.cnpj_mat_ent.delete(0, "end")
                self.cnpj_mat_ent.insert(0, new_text)
            elif valid_cpf_mat == "CPF":
                text = self.cnpj_mat_ent.get().replace(".", "").replace("-", "")[:11]
                new_text = ""
                if event.keysym.lower() == "backspace": return

                for index in range(len(text)):
                    if not text[index] in "0123456789": continue
                    if index in [2, 5]:
                        new_text += text[index] + "."
                    elif index == 8:
                        new_text += text[index] + "-"
                    else:
                        new_text += text[index]

                self.cnpj_mat_ent.delete(0, "end")
                self.cnpj_mat_ent.insert(0, new_text)
        elif self.open_win_cli == "cadfor":
            valid_cpf_mat = self.cnpj_mat_str.get()
            if valid_cpf_mat == "CNPJ":
                text = self.entr_cnpj.get().replace(".", "").replace("/", "").replace("-", "")[:14]
                new_text = ""
                if event.keysym.lower() == "backspace": return

                for index in range(len(text)):
                    if not text[index] in "0123456789": continue
                    if index in [1, 4]:
                        new_text += text[index] + "."
                    elif index == 7:
                        new_text += text[index] + "/"
                    elif index == 11:
                        new_text += text[index] + "-"
                    else:
                        new_text += text[index]

                self.entr_cnpj.delete(0, "end")
                self.entr_cnpj.insert(0, new_text)
            elif valid_cpf_mat == "CPF":
                text = self.entr_cnpj.get().replace(".", "").replace("-", "")[:11]
                new_text = ""
                if event.keysym.lower() == "backspace": return

                for index in range(len(text)):
                    if not text[index] in "0123456789": continue
                    if index in [2, 5]:
                        new_text += text[index] + "."
                    elif index == 8:
                        new_text += text[index] + "-"
                    else:
                        new_text += text[index]

                self.entr_cnpj.delete(0, "end")
                self.entr_cnpj.insert(0, new_text)

    def format_float(self, event):
        self.text = self.text[:11]
        new_text = ""
        if event.keysym.lower() == "backspace":
            return
        for index in range(len(self.text)):
            if not self.text[index] in "0123456789": continue
            if index in [-3]:
                new_text += self.text[index] + "."
            else:
                new_text += self.text[index]
        self.texto.delete(0, "end")
        self.texto.insert(0, new_text)
