from reportlab.pdfgen import canvas
import platform
from funcs.backUteis import license
import webbrowser
from reportlab.lib.colors import lightslategray, lightgrey

plataforma = platform.system()


class PrintRel(license.Data_company):
    def VarRel(self):
        self.dados()
        self.dia_R = self.entradaDataorc.get()
        self.cliente_R = self.listNome.get()
        self.endereco_R = self.listEndereco.get()
        self.municipio_R = self.listMunicipio.get()
        self.cpf_R = self.listCpf.get()
        self.fone_R = self.listFone.get()
        self.uf_R = self.listUf.get()
        self.obs_R = self.listObs.get()
        self.aut_R = self.listAut.get()
        self.anoAut_R = self.listAno.get()
        self.marca_R = self.listMarca.get()
        self.combustivel_R = self.listCombustivel.get()
        self.cor_R = self.listCor.get()
        self.placa_R = self.placa.get()
        self.numorc_R = self.listaNumOrc.get()
        self.area1_R = self.area1.get()
        self.area2_R = self.area2.get()
        self.area3_R = self.area3.get()
        self.area4_R = self.area4.get()
        self.km_R = self.entradaObs.get()
        self.comp1 = self.listInicio.get()
        self.comp2 = self.listFim.get()

        self.lista1_R = self.listaCol2a.get()
        self.colquant1_R = self.listaCol3a.get()
        self.colunit1_R = self.listaCol4a.get()
        self.coltotal1_R = self.listaCol5a.get()

        self.entradatotal2_R = self.entradatotal.get()
        self.tecnico_R = self.entradaTecnico.get()
        self.tiporc_R = self.Tipvar.get()
    def PrintOrc(self):
        if plataforma == "Linux":
            webbrowser.open("Orcamento.pdf")
            print(platform.system())
        else:
            webbrowser.open("file:///c:/glacx/Orcamento.pdf")
    def imprime_orc(self):
        self.VarRel()
        # Gerar Relatorio de orçamento
        if plataforma == "Linux":
            self.c = canvas.Canvas("Orcamento.pdf")
            self.c.setFont("Helvetica-Bold", 24)
        else:
            self.c = canvas.Canvas("c:\glacx\Orcamento.pdf")
            self.c.setFont("Helvetica-Bold", 24)
        try:
            self.c.drawInlineImage("logoempresa.jpg", 150, 770, 300, 70)
        except:
            self.c.drawString(220, 790, self.m_SeuLogo)
        self.c.setFont("Helvetica-Bold", 14)

        self.c.drawString(15, 480, self.m_ProdutosEServicos)
        self.c.drawString(450, 130, self.m_Total + ":")
        self.c.drawString(500, 130, "R$" + self.entradatotal2_R)
        self.c.setFont("Helvetica", 12)

        self.linha = self.c
        self.linha.setFillColor(lightgrey)
        #self.linha.rect(250, 753, 100, 12, fill=True, stroke=False)

        # moldura
        self.linha.rect(15, 713, 150, 17, fill=True, stroke=False)
        self.linha.rect(15, 698, 570, 12, fill=True, stroke=False)
        self.linha.rect(15, 683, 570, 12, fill=True, stroke=False)
        self.linha.rect(15, 669, 570, 12, fill=True, stroke=False)
        self.linha.rect(15, 633, 150, 17, fill=True, stroke=False)
        self.linha.rect(15, 618, 570, 12, fill=True, stroke=False)
        self.linha.rect(15, 603, 570, 12, fill=True, stroke=False)
        self.linha.rect(15, 580, 570, 17, fill=True, stroke=False)
        self.linha.rect(15, 530, 570, 17, fill=True, stroke=False)
        self.linha.rect(15, 550, 570, 30, fill=True, stroke=False)
        self.linha.rect(15, 500, 570, 30, fill=True, stroke=False)

        self.c.setFillColor(lightslategray)

        self.c.drawString(230, 755, self.tiporc_R + " Nº  " + self.numorc_R)
        self.c.drawString(15, 755, 'Entrada: ' + self.comp1)
        self.c.drawString(480, 755, 'Saida: ' + self.comp2)

        self.c.drawString(15, 720, self.m_DadosDoCliente)
        self.c.drawString(15, 700, "Nome:")
        self.c.drawString(285, 700, "Fone:")
        self.c.drawString(415, 700, "Cpf / Cnpj:")
        self.c.drawString(15, 685, "Endereco:")
        self.c.drawString(15, 671, "Cidade:")
        self.c.drawString(500, 671, "Uf:")

        self.c.drawString(15, 640, self.m_DadosDoVeiculo)
        self.c.drawString(15, 620, "Placa:")
        self.c.drawString(120, 620, "Veiculo:")
        self.c.drawString(420, 620, "Cor:")
        self.c.drawString(15, 605, "Combustivel:")
        self.c.drawString(420, 605, "Km:")

        linhaItem = 480
        contador = 0
        while (contador < 31):
            contador = contador + 1
            linhaItem -= 10
            self.linha.rect(13, linhaItem, 570, 0.5, fill=True, stroke=False)

        # MOLDURAS DO RELATORIO
        self.c.rect(13, 155, 1, 314, fill=True, stroke=False)
        self.c.rect(40, 155, 1, 314, fill=True, stroke=False)
        self.c.rect(420, 155, 1, 314, fill=True, stroke=False)
        self.c.rect(475, 155, 1, 314, fill=True, stroke=False)
        self.c.rect(515, 155, 1, 314, fill=True, stroke=False)
        self.c.rect(583, 155, 1, 314, fill=True, stroke=False)
        self.c.rect(13, 155, 571, 1, fill=True, stroke=False)

        self.c.setFont("Helvetica", 10)

        ####  TEXTO DE DESCRICAO DOS PROBLEMAS
        self.c.drawString(50, 570, self.area1_R)
        self.c.drawString(50, 555, self.area2_R)
        self.c.drawString(50, 520, self.area3_R)
        self.c.drawString(50, 505, self.area4_R)

        self.c.setFont("Helvetica-Bold", 10)
        self.c.drawString(15, 585, self.m_Atend1print)
        self.c.drawString(15, 535, self.m_Atend2print)

        #### DADOS DO CLIENTE
        self.c.rect(15, 745, 570, 2, fill=True, stroke=False)
        self.c.drawString(65, 700,  self.cliente_R)
        self.c.drawString(325, 700,  self.fone_R)
        self.c.drawString(485, 700,  self.cpf_R)
        self.c.drawString(80, 685,  self.endereco_R)

        self.c.drawString(85, 671,  self.municipio_R)
        self.c.drawString(530, 671, self.uf_R)

        # DADOS DO AUTOMOVEL
        self.c.drawString(60, 620,  self.placa_R)
        self.c.drawString(165, 620,  self.aut_R)
        self.c.drawString(280, 620, self.marca_R)
        self.c.drawString(470, 620, self.cor_R)
        self.c.drawString(150, 605, self.combustivel_R)
        self.c.drawString(450, 605, self.km_R)

        self.c.setFont("Helvetica-Bold", 9)
        self.c.drawString(17, 462, self.m_Item)
        self.c.drawString(200, 462, self.m_Descricao)
        self.c.drawString(482, 462, self.m_Quant)
        self.c.drawString(425, 462, self.m_ValorUnit)
        self.c.drawString(540, 462, self.m_Total)

        self.c.setFont("Helvetica", 8)

        # DESCRIÇÃO DOS ITENS DO ORÇAMENTO
        self.conecta_Glac()

        self.cursor.execute("""SELECT desc_item
        FROM orcamento2 WHERE id_orc2 = '%s'  """ % self.numorc_R)
        rows = self.cursor.fetchall()
        x = 462
        for row in rows:
            row = str(row)
            row = row.replace('(', '').replace(',)', '').replace("'", "")
            x -= 10
            self.c.drawString(45, x, row)

        self.cursor.execute("""SELECT ordem_item 
                FROM orcamento2 WHERE id_orc2 = '%s'  """ % self.numorc_R)
        rows = self.cursor.fetchall()
        x = 462
        for row in rows:
            row = str(row)
            row = row.replace('(', '').replace(',)', '').replace("'", "")
            x -= 10
            self.c.drawString(25, x, row[0])

        self.cursor.execute("""SELECT valor FROM orcamento2 
        WHERE id_orc2 = '%s'  """ % self.numorc_R)
        rows = self.cursor.fetchall()
        x = 462
        for row in rows:
            row = str(row)
            row = row.replace('(', '').replace(',)', '').replace("'", "")
            x -= 10
            self.c.drawString(430, x, row)

        self.cursor.execute("""SELECT quant FROM orcamento2 
                    WHERE id_orc2 = '%s'  """ % self.numorc_R)
        rows = self.cursor.fetchall()
        x = 462
        for row in rows:
            row = str(row)
            row = row.replace('(', '').replace(',)', '').replace("'", "")
            x -= 10
            self.c.drawString(480, x, row)
        #
        self.cursor.execute("""SELECT total FROM orcamento2 WHERE id_orc2 = '%s'  """ % self.numorc_R)
        rows = self.cursor.fetchall()
        x = 462
        for row in rows:
            row = str(row)
            row = row.replace('(', '').replace(',)', '').replace("'", "")
            x -= 10
            self.c.drawString(520, x, row)
        self.desconecta_Glac()

        self.c.setFont("Helvetica", 12)
        # VARIAVEIS DO RODAPE DO RELATORIO - DADOS DA EMPRESA
        self.c.rect(15, 100, 570, 5, fill=True, stroke=False)
        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawString(270, 80, self.NomeEmpresa)
        self.c.setFont("Helvetica", 11)
        self.c.drawString(30, 60, self.NomeRuaEmp)
        self.c.drawString(300, 60, self.NomeBairroEmp)
        self.c.drawString(430, 60, self.MunicipioEmp)
        self.c.drawString(30, 40, self.TelefoneEmp)
        self.c.drawString(30, 20, self.m_Tecnico + ":" + self.tecnico_R)
        self.c.setFont("Helvetica", 8)
        self.c.drawString(30, 5, "GlacX - Oficinas - RfZorzi Sistemas - https://www.facebook.com/rfzorzi/")
        self.c.showPage()
        self.c.save()
        self.PrintOrc()

    def PrintVist(self):
        if plataforma == "Linux":
            webbrowser.open("Vistoria.pdf")
            print(platform.system())
        else:
            webbrowser.open("file:///c:/glacx/Vistoria.pdf")

    def imprime_vist(self):
        self.VarRel()
        self.tecnico_R = self.entradaTecnico.get()
        self.tiporc_R = self.Tipvar.get()

        if plataforma == "Linux":
            self.c = canvas.Canvas("Vistoria.pdf")
            self.c.setFont("Helvetica-Bold", 24)
        else:
            self.c = canvas.Canvas("c:\glacx\Vistoria.pdf")
            self.c.setFont("Helvetica-Bold", 24)
            #### MOLDURA E TITULOS DO RELATORIO

        try:
            self.c.drawInlineImage("logoempresa.jpg", 150, 770, 300, 70)
        except:
            self.c.drawString(220, 790, 'Seu Logo')
        self.c.setFont("Helvetica-Bold", 16)
        self.c.drawString(200, 755, self.m_VistoriadoVeiculo + "Nº  " + self.numorc_R)

        self.linha = self.c
        self.linha.setFillColor(lightgrey)

        # moldura
        self.linha.rect(15, 713, 150, 17, fill=True, stroke=False)
        self.linha.rect(15, 698, 570, 12, fill=True, stroke=False)
        self.linha.rect(15, 683, 570, 12, fill=True, stroke=False)
        self.linha.rect(15, 669, 570, 12, fill=True, stroke=False)
        self.linha.rect(15, 633, 150, 17, fill=True, stroke=False)
        self.linha.rect(15, 618, 570, 12, fill=True, stroke=False)
        self.linha.rect(15, 603, 570, 12, fill=True, stroke=False)
        self.linha.rect(15, 565, 150, 17, fill=True, stroke=False)
        self.linha.rect(35, 538, 530, 20, fill=True, stroke=False)
        self.linha.rect(35, 498, 530, 20, fill=True, stroke=False)
        self.linha.rect(35, 458, 530, 20, fill=True, stroke=False)
        self.linha.rect(35, 418, 530, 20, fill=True, stroke=False)
        self.linha.rect(35, 378, 530, 20, fill=True, stroke=False)
        self.linha.rect(35, 338, 530, 20, fill=True, stroke=False)
        self.linha.rect(35, 298, 530, 20, fill=True, stroke=False)
        self.linha.rect(35, 258, 530, 20, fill=True, stroke=False)
        self.linha.rect(35, 218, 530, 20, fill=True, stroke=False)

        self.c.setFillColor(lightslategray)
        self.c.setFont("Helvetica", 12)

        self.c.drawString(15, 755, 'Entrada: ' + self.comp1)
        self.c.drawString(480, 755, 'Saida: ' + self.comp2)

        self.c.drawString(15, 720, self.m_DadosDoCliente)
        self.c.drawString(15, 700, "Nome:")
        self.c.drawString(285, 700, "Fone:")
        self.c.drawString(415, 700, "Cpf / Cnpj:")
        self.c.drawString(15, 685, "Endereco:")
        self.c.drawString(15, 671, "Cidade:")
        self.c.drawString(500, 671, "Uf:")

        self.c.drawString(15, 640, self.m_DadosDoVeiculo)
        self.c.drawString(15, 620, "Placa:")
        self.c.drawString(120, 620, "Veiculo:")
        self.c.drawString(420, 620, "Cor:")
        self.c.drawString(15, 605, "Combustivel:")
        self.c.drawString(420, 605, "Km:")

        self.c.setFont("Helvetica", 16)
        self.c.drawString(17, 568, self.m_ItensVistoriados)

        # Vistoria variaveis
        self.codVist_R = self.listaNumOrc.get()
        self.tanque_R = self.are1.get()
        self.odometro_R = self.are2.get()
        self.radio_R = self.are3.get()
        self.calota_R = self.are4.get()
        self.triangulo_R = self.are5.get()
        self.macaco_R = self.are6.get()
        self.estepe_R = self.are7.get()
        self.obs1_R = self.are8.get()
        self.obs2_R = self.are9.get()

        self.c.setFont("Helvetica-Bold", 14)
        #
        self.c.drawString(35, 540, self.m_Tanque)
        self.c.drawString(35, 500, self.m_Odometro)
        self.c.drawString(35, 460, 'Obs 1:')
        self.c.drawString(35, 420, 'Obs 2:')
        self.c.drawString(35, 380, 'Obs 3:')
        self.c.drawString(35, 340, 'Obs 4:')
        self.c.drawString(35, 300, 'Obs 5:')
        self.c.drawString(35, 260, 'Obs 6:')
        self.c.drawString(35, 220, 'Obs 7:')

        self.c.drawString(250, 540, self.tanque_R)
        self.c.drawString(200, 500, self.odometro_R)
        self.c.drawString(100, 460, self.radio_R)
        self.c.drawString(100, 420, self.calota_R)
        self.c.drawString(100, 380, self.triangulo_R)
        self.c.drawString(100, 340, self.macaco_R)
        self.c.drawString(100, 300, self.estepe_R)
        self.c.drawString(100, 260, self.obs1_R)
        self.c.drawString(100, 220, self.obs2_R)

        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawString(35, 200, "Confirmo que deixei o veiculo nas condições descritas:")
        self.c.drawString(35, 170, "Assinatura:")

        # MOLDURAS DO RELATORIO
        self.c.rect(13, 155, 2, 427, fill=True, stroke=False)
        self.c.rect(14, 155, 572, 2, fill=True, stroke=False)
        self.c.rect(585, 155, 2, 427, fill=True, stroke=False)
        self.c.rect(13, 582, 572, 2, fill=True, stroke=False)

        self.c.setFont("Helvetica-Bold", 10)
        self.c.drawString(65, 700, self.cliente_R)
        self.c.drawString(325, 700, self.fone_R)
        self.c.drawString(485, 700, self.cpf_R)
        self.c.drawString(80, 685, self.endereco_R)

        self.c.drawString(85, 671, self.municipio_R)
        self.c.drawString(530, 671, self.uf_R)

        # DADOS DO AUTOMOVEL
        self.c.drawString(60, 620, self.placa_R)
        self.c.drawString(165, 620, self.aut_R)
        self.c.drawString(280, 620, self.marca_R)
        self.c.drawString(470, 620, self.cor_R)
        self.c.drawString(150, 605, self.combustivel_R)
        self.c.drawString(450, 605, self.km_R)

        # VARIAVEIS DO RODAPE DO RELATORIO - DADOS DA EMPRESA
        self.c.rect(15, 100, 570, 5, fill=True, stroke=False)
        self.c.drawString(30, 80, self.NomeEmpresa)
        self.c.drawString(30, 60, self.NomeRuaEmp)
        self.c.drawString(300, 60, self.NomeBairroEmp)
        self.c.drawString(430, 60, self.MunicipioEmp)
        self.c.drawString(30, 40, self.TelefoneEmp)

        self.c.drawString(30, 20, self.m_Tecnico + self.tecnico_R)
        self.c.setFont("Helvetica", 8)
        self.c.drawString(280, 5, "GlacX - Oficinas - RfZorzi Sistemas - https://www.facebook.com/rfzorzi/")
        self.c.showPage()
        self.c.save()

        self.PrintVist()