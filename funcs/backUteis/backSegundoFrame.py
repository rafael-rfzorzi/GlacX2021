from tkinter import *


class SegundoFrame:
    def limpa_cliente(self):
        self.entradaCod_cli.delete('0', 'end')
        self.listNome.delete('0', 'end')
        self.listEndereco.delete('0', 'end')
        self.listMunicipio.delete('0', 'end')
        self.listCpf.delete('0', 'end')
        self.listFone.delete('0', 'end')
        self.listUf.delete('0', 'end')
        self.listObs.delete('0', 'end')
        self.entradaCod_aut.delete('0', 'end')
        self.listAut.delete('0', 'end')
        self.listAno.delete('0', 'end')
        self.listMarca.delete('0', 'end')
        self.listCombustivel.delete('0', 'end')
        self.listCor.delete('0', 'end')
        self.placa.delete('0', 'end')
        self.entradaObs.delete('0', 'end')
        self.area1.delete('0', 'end')
        self.area2.delete('0', 'end')
        self.area3.delete('0', 'end')
        self.area4.delete('0', 'end')
        self.entradatotal.delete('0', 'end')
        self.listInicio.delete('0', 'end')
        self.listFim.delete('0', 'end')
        self.codServ1.delete('0', 'end')
        self.listaCol2a.delete('0', 'end')
        self.listaCol3a.delete('0', 'end')
        self.listaCol3a.insert(0, '1')
        self.listaCol4a.delete('0', 'end')
        self.listaCol4a.insert(0, 'R$ 0,00')
        self.listaCol5a.delete('0', 'end')
        self.listaCol5a.insert(0, 'R$ 0,00')
        self.listaNumOrc.delete('0', 'end')
        self.are1.delete('0', 'end')
        self.are2.delete('0', 'end')
        self.are3.delete('0', 'end')
        self.are4.delete('0', 'end')
        self.are5.delete('0', 'end')
        self.are6.delete('0', 'end')
        self.are7.delete('0', 'end')
        self.are8.delete('0', 'end')
        self.are9.delete('0', 'end')
        self.listaServProd.delete(*self.listaServProd.get_children())

    def carrega_automovel(self, event):
        self.listAut.delete('0', 'end')
        self.listAno.delete('0', 'end')
        self.listMarca.delete('0', 'end')
        self.listCombustivel.delete('0', 'end')
        self.listCor.delete('0', 'end')
        self.listObs.delete('0', 'end')
        self.placa.delete('0', 'end')
        self.conecta_Glac()
        pos = int(self.entradaCod_aut.curselection()[0])
        placa = self.entradaCod_aut.get(pos)

        nomeplac = self.cursor
        nomeplac.execute("""SELECT placa, UPPER(veiculo), ano, UPPER(montadora), UPPER(combust),
                        UPPER(cor)
                        FROM frota WHERE placa = '%s'""" % placa)
        consultaplac = self.cursor.fetchall()
        for i in consultaplac:
            self.placa.insert(0, i[0])
            self.listAut.insert(0, i[1])
            self.listAno.insert(0, i[2])
            self.listMarca.insert(0, i[3])
            self.listCombustivel.insert(0, i[4])
            self.listCor.insert(0, i[5])
        self.desconecta_Glac()
        def carrega_automovel_a(event):
            carrega_automovel()

    def carrega_cliente(self):
        self.conecta_Glac()
        cod_cli = self.entradaCod_cli.get()
        nomecur = self.cursor
        nomecur.execute("""SELECT UPPER(nome) , UPPER(endereco), "Nº", numcasa, UPPER(municipio),
            cpf, fone1ddd, fone1, UPPER(uf), obs FROM clientes WHERE cod_cli = '%s'""" % cod_cli)
        consultanome = self.cursor.fetchall()
        for i in consultanome:
            self.listNome.insert(END, i[0])
            self.listEndereco.insert(END, i[1:4])
            self.listMunicipio.insert(END, i[4])
            self.listCpf.insert(END, i[5])
            self.listFone.insert(END, i[6:8])
            self.listUf.insert(END, i[8])
            self.listObs.insert(END, i[9])

        pla = self.cursor
        pla.execute("SELECT placa FROM frota, clientes "
                    "WHERE idcliente = cod_cli and cod_cli = '%s'" % cod_cli)
        consultapla = self.cursor.fetchall()
        for i in consultapla:
            self.entradaCod_aut.insert(END, i)
        self.desconecta_Glac()
        def carrega_cliente_a(event):
            self.carrega_cliente()

    def carrega_cliente2(self, event):
        self.limpa_cliente() # Variaveis da função
        self.listaServ.selection()
        for n in self.listaServ.selection():
            col1, col2 = self.listaServ.item(n, 'values')
            self.entradaCod_cli.insert(0, col1)
        self.carrega_cliente()
        self.listacliente.destroy()
        def carrega_cliente2_a(event):
            self.carrega_cliente2()