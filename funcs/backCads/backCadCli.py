from Janelas.estiloWidgets.widgets_Glac import *
from pycep_correios import get_address_from_cep, WebService, exceptions
from tkinter import messagebox


class CadCli:
    def list_cadcli(self):
        self.conecta_Glac()
        self.lista1 = self.cursor.execute("""SELECT  cod_cli, nome, fone1ddd, fone1
                    FROM clientes  ORDER BY nome ASC; """)
        for i in self.lista1:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()

    def add_autobindC(self, event):
        # codServ1.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.entradaVeiculo2.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.entradaMontadora2.delete(0, END)
        self.listatec1.selection()
        for n in self.listatec1.selection():
            col1, col2, col3 = self.listatec1.item(n, 'values')
            self.nomeEquipEntry.insert(END, col2)
            self.marcaEquipEntry.insert(END, col3)
            self.entradaVeiculo2.insert(END, col1)

        cod = self.entradaVeiculo2.get()

        self.conecta_Glac()

        self.cursor.execute(
            """SELECT montad FROM automoveis WHERE cod_aut LIKE '%s'""" % cod)
        addservico1cod = self.cursor.fetchall()
        for i in addservico1cod:
            self.marcaEquipEntry.insert(END, i)

        self.desconecta_Glac()
        self.listatec.destroy()

    def add_clienteC(self):
        self.conecta_Glac()
        self.listaServ.delete(*self.listaServ.get_children())
        self.variaveisCliente()
        self.variaveisVeiculo()

        self.cursor.execute("""INSERT INTO clientes 
        (nome, nascdia, endereco, numcasa, complemento, bairro, 
        municipio, uf, fone1ddd, fone1, fone2ddd, fone2, cep, cpf, email, obs)
        VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (self.cadcli_nome, self.cadcli_nascdia,
         self.cadcli_endereco, self.cadcli_numcasa, self.cadcli_complemento,
         self.cadcli_bairro, self.cadcli_municipio, self.cadcli_uf, self.cadcli_fone1ddd,
         self.cadcli_fone1, self.cadcli_fone2ddd, self.cadcli_fone2, self.cadcli_cep,
         self.cadcli_cpf, self.cadcli_email, self.cadcli_obs))
        self.conn.commit()

        msg = self.m_msgClienteAdd
        msg += ""
        messagebox.showinfo("GLAC ", msg)
        self.limpa_clienteC()
        self.desconecta_Glac()

        self.list_cadcli()

    def add_veiculoC(self):
        self.variaveisCliente()
        self.variaveisVeiculo()

        cod_cli = self.codPeEntry.get()
        motor = '0'
        self.conecta_Glac()
        self.cursor.execute("""INSERT INTO frota ( idcliente, placa, veiculo, montadora, 
        ano, combust, cor) VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
        (self.cadcli_cod, self.cadcli_placa, self.cadcli_montadora, self.cadcli_veiculo,
         self.cadcli_ano, self.cadcli_combust, self.cadcli_cor))
        self.conn.commit()

        self.serialEquipEntry.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.entradaVeiculo2.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.entradaMontadora2.delete(0, END)
        self.fabrAnoEquipEntry.delete(0, END)
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
        FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)

        self.desconecta_Glac()
        msg = self.m_msgAutAdd
        messagebox.showinfo("GLAC ", msg)

    def busca_clienteC(self):
        self.conecta_Glac()
        self.listaServ.delete(*self.listaServ.get_children())

        self.nomePeEntry.insert(END, '%')
        nome = self.nomePeEntry.get()
        self.cursor.execute("""SELECT cod_cli, nome, fone1ddd, fone1 FROM clientes 
        WHERE nome LIKE '%s' ORDER BY nome ASC""" % nome)
        buscanomecli = self.cursor.fetchall()
        for i in buscanomecli:
            self.listaServ.insert("", END, values=i)

        self.limpa_clienteC()
        self.desconecta_Glac()

    def bind_autoC(self, event):
        # codServ1.delete(0, END)
        global col1, col3, col2
        self.limpa_entryautoC()
        self.listaPlaca.selection()

        for n in self.listaPlaca.selection():
            col1, col2, col3, col4, col5, col6 = self.listaPlaca.item(n, 'values')

        self.serialEquipEntry.insert(END, col1)
        self.nomeEquipEntry.insert(END, col3)
        self.marcaEquipEntry.insert(END, col2)
        self.entradaVeiculo2.insert(END, 0)
        self.codEquipEntry.insert(END, 0)
        self.corvar.set(col4)
        self.combvar.set(col5)
        self.fabrAnoEquipEntry.insert(END, col6)

    def carrega_clienteC(self):
        cod_cli = self.codPeEntry.get()
        self.limpa_clienteC2()
        self.conecta_Glac()

        self.cursor.execute("""SELECT UPPER(nome), nascdia, numcasa, UPPER(complemento),
            UPPER(email), UPPER(endereco), UPPER(bairro), UPPER(municipio), UPPER(uf),
            fone1ddd, fone1, fone2ddd, fone2, cep, cpf, rg, UPPER(obs)
            FROM clientes WHERE cod_cli = '%s'""" % cod_cli)
        consultacli = self.cursor.fetchall()
        for i in consultacli:
            self.nomePeEntry.insert(END, i[0])
            self.nascDiaPeEntry.insert(END, i[1])
            self.numPeEntry.insert(END, i[2])
            self.complemPeEntry.insert(END, i[3])
            self.emailPeEntry.insert(END, i[4])
            self.logradPeEntry.insert(END, i[5])
            self.bairroPeEntry.insert(END, i[6])
            self.cidadePeEntry.insert(END, i[7])
            self.ufPeEntry.insert(END, i[8])
            self.fone1PeEntry.insert(END, i[9])
            self.fone1PeEntry2.insert(END, i[10])
            self.fone2PeEntry.insert(END, i[11])
            self.fone2PeEntry2.insert(END, i[12])
            self.cepPeEntry.insert(END, i[13])
            self.cnpj_mat_ent.insert(END, i[14])
            self.obsPeEntry.insert(END, i[16])

        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
    	    FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)
        self.desconecta_Glac()

    def OnVsbC(self, *args):
        self.listaServ.yview(*args)

    def OnMouseWheelC(self, event):
        self.listaServ.yview("scroll", event.delta, "units")
        return "break"

    def OnDoubleClickC(self, *args):
        self.limpa_clienteC()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4 = self.listaServ.item(n, 'values')
            self.codPeEntry.insert(END, col1)

        self.carrega_clienteC()

    def mud_autoC(self):
        self.variaveisCliente()
        self.variaveisVeiculo()

        cod_cli = self.codPeEntry.get()
        self.conecta_Glac()

        self.cursor.execute(""" UPDATE frota SET veiculo = ?, ano = ?, placa = ?,
            idcliente = ?, combust = ?, montadora = ?, cor = ? WHERE placa = ? AND idcliente = ?""",
                            (self.cadcli_veiculo, self.cadcli_ano, self.cadcli_placa, cod_cli,
                             self.cadcli_combust, self.cadcli_montadora,
                             self.cadcli_cor, self.cadcli_placa, cod_cli))
        self.conn.commit()

        self.serialEquipEntry.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.entradaVeiculo2.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.entradaMontadora2.delete(0, END)
        self.fabrAnoEquipEntry.delete(0, END)
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
            	    FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)

        self.desconecta_Glac()
        msg = self.m_msgVeiculoAlt
        msg += ""
        messagebox.showinfo("GLAC ", msg)
        self.carrega_clienteC()

    def mud_clienteC(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.conecta_Glac()

        self.variaveisCliente()
        self.variaveisVeiculo()

        self.cursor.execute("""UPDATE clientes SET nome = ?, endereco = ?, bairro = ?, 
        municipio = ?, uf = ?, cep = ?, cpf = ?, obs = ?, email = ?, fone1ddd = ?,
        fone1 = ?, fone2ddd = ?, fone2 = ?, complemento = ?, numcasa = ?, nascdia = ?
        WHERE cod_cli = ?""",(self.cadcli_nome, self.cadcli_endereco, self.cadcli_bairro,
        self.cadcli_municipio, self.cadcli_uf, self.cadcli_cep, self.cadcli_cpf,
        self.cadcli_obs, self.cadcli_email, self.cadcli_fone1ddd,
        self.cadcli_fone1, self.cadcli_fone2ddd, self.cadcli_fone2, self.cadcli_complemento,
        self.cadcli_numcasa, self.cadcli_nascdia, self.cadcli_cod))

        self.conn.commit()
        self.desconecta_Glac()

        self.list_cadcli()
        msg = self.m_msgClienteAlt
        msg += ""
        messagebox.showinfo("GLAC - Clientes", msg)

    def limpa_entryautoC(self):
        self.serialEquipEntry.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.fabrAnoEquipEntry.delete(0, END)

    def limpa_clienteC(self):
        self.codPeEntry.delete(0, END)
        self.limpa_clienteC2()

    def limpa_clienteC2(self):
        self.nomePeEntry.delete(0, END)
        self.nascDiaPeEntry.delete(0, END)
        self.logradPeEntry.delete(0, END)
        self.numPeEntry.delete(0, END)
        self.complemPeEntry.delete(0, END)
        self.bairroPeEntry.delete(0, END)
        self.cidadePeEntry.delete(0, END)
        self.ufPeEntry.delete(0, END)
        self.fone1PeEntry.delete(0, END)
        self.fone1PeEntry2.delete(0, END)
        self.fone2PeEntry.delete(0, END)
        self.fone2PeEntry2.delete(0, END)
        self.cepPeEntry.delete(0, END)
        self.cnpj_mat_ent.delete(0, END)
        self.obsPeEntry.delete(0, END)
        self.emailPeEntry.delete(0, END)
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.limpa_entryautoC()

    def del_clienteC(self):
        cod_cli = self.codPeEntry.get()

        self.conecta_Glac()
        self.cursor.execute("""DELETE FROM frota WHERE idcliente=?""", (cod_cli,))
        self.conn.commit()

        self.cursor.execute("""DELETE FROM clientes WHERE cod_cli=?""", (cod_cli,))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.desconecta_Glac()
        self.list_cadcli()

        self.listaPlaca.delete(*self.listaPlaca.get_children())
        self.limpa_clienteC()

    def del_placaC(self):
        self.listaPlaca.delete(*self.listaPlaca.get_children())
        cod_cli = self.codPeEntry.get()
        placa = self.serialEquipEntry.get()
        self.conecta_Glac()
        self.cursor.execute("""DELETE FROM frota 
        WHERE placa =? AND idcliente = ?""", (placa, cod_cli))
        self.conn.commit()
        self.listaPlaca.delete(*self.listaPlaca.get_children())
        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
        FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)
        self.desconecta_Glac()
        self.limpa_entryautoC()
        self.listatec.destroy()

    def variaveisCliente(self):
        self.cadcli_cod = self.codPeEntry.get()
        self.cadcli_nome = self.nomePeEntry.get()
        self.cadcli_nascdia = self.nascDiaPeEntry.get()
        self.cadcli_endereco = self.logradPeEntry.get()
        self.cadcli_numcasa = self.numPeEntry.get()
        self.cadcli_complemento = self.complemPeEntry.get()
        self.cadcli_bairro = self.bairroPeEntry.get()
        self.cadcli_municipio = self.cidadePeEntry.get()
        self.cadcli_uf = self.ufPeEntry.get()
        self.cadcli_fone1ddd = self.fone1PeEntry.get()
        self.cadcli_fone1 = self.fone1PeEntry2.get()
        self.cadcli_fone2ddd = self.fone2PeEntry.get()
        self.cadcli_fone2 = self.fone2PeEntry2.get()
        self.cadcli_cep = self.cepPeEntry.get()
        self.cadcli_cpf = self.cnpj_mat_ent.get()
        self.cadcli_email = self.emailPeEntry.get()
        self.cadcli_obs = self.obsPeEntry.get()

    def variaveisVeiculo(self):
        self.cadcli_veiculoId = self.codEquipEntry.get()
        self.cadcli_MontadoraId = self.entradaMontadora2.get()
        self.cadcli_veiculo = self.nomeEquipEntry.get()
        self.cadcli_ano = self.fabrAnoEquipEntry.get()
        self.cadcli_placa = self.serialEquipEntry.get()
        self.cadcli_montadora = self.marcaEquipEntry.get()
        self.cadcli_combust = self.combvar.get()
        self.cadcli_cor = self.corvar.get()

    def cep(self, pycep_correios=None):
        self.logradPeEntry.delete(0, END)
        self.bairroPeEntry.delete(0, END)
        self.cidadePeEntry.delete(0, END)
        self.ufPeEntry.delete(0, END)
        try:
            self.cep = self.cepPeEntry.get()
            endcep = get_address_from_cep(self.cep, webservice=WebService.APICEP)

            self.logradPeEntry.insert(END, endcep['logradouro'])
            self.bairroPeEntry.insert(END, endcep['bairro'])
            self.cidadePeEntry.insert(END, endcep['cidade'])
            self.ufPeEntry.insert(END, endcep['uf'])
        except exceptions.InvalidCEP as eic:
            msg = 'InvalidCEP - Não encontrado'
            messagebox.showinfo("GLAC", msg)

        except exceptions.CEPNotFound as ecnf:
            msg = 'CEPNotFound - Não encontrado'
            messagebox.showinfo("GLAC", msg)

        except exceptions.ConnectionError as errc:
            msg = 'ConnectionError - Não encontrado'
            messagebox.showinfo("GLAC", msg)

        except exceptions.Timeout as errt:
            msg = 'Timeout - Não encontrado'
            messagebox.showinfo("GLAC", msg)

        except exceptions.HTTPError as errh:
            msg = 'HTTPError - Não encontrado'
            messagebox.showinfo("GLAC", msg)

        except exceptions.BaseException as e:
            msg = 'BaseException - Não encontrado'
            messagebox.showinfo("GLAC", msg)

    def busca_auto_c(self, *args):
        # Widgets - Listar tecnicos #
        self.nomeEquipEntry.insert(END, '%')

        veicAuto = self.nomeEquipEntry.get()

        self.listatec = Toplevel()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("405x235+100+150")
        self.listatec.resizable(FALSE, FALSE)
        self.listatec.transient(self.janelaCli)
        self.listatec.focus_force()
        self.listatec.grab_set()
        ##########
        self.listatec1 = ttk.Treeview(self.listatec, height=10,
            column=("col1", "col2", "col3"))
        self.listatec1.heading("#0", text="")
        self.listatec1.heading("#1", text='Cod')
        self.listatec1.heading("#2", text=self.m_Automovel)
        self.listatec1.heading("#3", text=self.m_Marca)

        self.listatec1.column("#0", width=0)
        self.listatec1.column("#1", width=40)
        self.listatec1.column("#2", width=180)
        self.listatec1.column("#3", width=150)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.listatec, orient='vertical',
                                   command=self.listatec1.yview)

        # Adiciona barra de rolagem
        self.listatec1.configure(yscroll=self.barra.set)
        self.barra.place(x=377, y=6, height=220)
        self.listatec1.place(x=5, y=5)
        self.conecta_Glac()
        self.cursor.execute("""SELECT cod_aut, automovel, marca 
        FROM automoveis, montadora WHERE montadora.cod = automoveis.montad
        AND automovel LIKE '%s' ORDER BY automovel ASC""" % veicAuto)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listatec1.insert("", END, values=row)
        self.listatec1.bind('<Double-1>', self.add_autobindC)
        self.desconecta_Glac()

    def deletar_window_c(self):
        res = messagebox.askquestion('Deletar cliente', 'Deseja realmente deletar este registro?')
        if res == 'no':
            res = ''
        else:
            self.del_clienteC()
            messagebox.showinfo('Mensagem', 'Registro deletado com sucesso!!')

    def deletar_window_placa_c(self):
        res = messagebox.askquestion('Deletar veiculo', 'Deseja realmente deletar este registro?')
        if res == 'no':
            res = ''
        else:
            self.del_placaC()
            messagebox.showinfo('Mensagem', 'Registro deletado com sucesso!!')
