from Janelas.estiloWidgets.widgets_Glac import *


class CadPagamento:
    def add_pag(self):
        ordem = self.listaNumOrc.get()
        tipopag = self.listtipopag.get()
        valortotal = self.entryValorTotal.get()
        valordeduzir = self.entryValor.get()

        dia = self.data_forma_pag.get()
        pago = "Não"

        self.conecta_Glac()
        self.cursor.execute("""	INSERT INTO formapag 
        ( ordem, tipopag, valorpagar, valordeduzir, dia, pago)
       	VALUES ( ?, ?, ?, ?, ?, ?)""", (ordem, tipopag, valortotal,
        valordeduzir, dia, "Sim"))
        self.conn.commit()
        self.desconecta_Glac()

        self.sel_pag_ordem()

        msg = "Pagamento incluido com sucesso"
        messagebox.showinfo("GLAC - Pagamentos", msg)
        self.sel_pag_ordem()

    def mud_pag(self):
        self.conecta_Glac()
        tipopag = self.entry2.get()
        valor = self.entry3.get()
        diaA = self.entry4.get()
        pago = self.entry7.get()
        idA = self.entry9.get()

        self.cursor.execute("""UPDATE formapag SET tipopag = ?, valordeduzir = ?, dia = ?,
            pago = ? WHERE id = ? """, (tipopag, valor, diaA, pago, idA))
        self.conn.commit()

        self.desconecta_Glac()
        self.janPag2.destroy()
        self.sel_pag_ordem()

    def carregaConsulta(self):
        self.conecta_Glac()

        tipopag = self.listtipopag.get()
        valor = self.entryValorDevido.get()

        mes = self.mesvar.get()
        ano = self.anovar.get()
        pago = self.entry7.get()

        ano = str(ano.replace("(", "").replace(")", "").replace(",", ""))
        mes = str(mes.replace("(", "").replace(")", "").replace(",", ""))
        mes2 = ''
        if mes == "'Janeiro'":
            mes2 = '01'
        elif mes == "'Fevereiro'":
            mes2 = '02'
        elif mes == "'Março'":
            mes2 = '03'
        elif mes == "'Abril'":
            mes2 = '04'
        elif mes == "'Maio'":
            mes2 = '05'
        elif mes == "'Junho'":
            mes2 = '06'
        elif mes == "'Julho'":
            mes2 = '07'
        elif mes == "'Agosto'":
            mes2 = '08'
        elif mes == "'Setembro'":
            mes2 = '09'
        elif mes == "'Outubro'":
            mes2 = '10'
        elif mes == "'Novembro'":
            mes2 = '11'
        elif mes == "'Dezembro'":
            mes2 = '12'

        self.listaPag.delete(*self.listaPag.get_children())
        lista = self.cursor.execute("""
            SELECT  ordem, tipopag, valordeduzir, dia, pago
            FROM formapag WHERE tipopag = ? AND  substr(dia, 4,2) = ? AND substr(dia, 7,10) = ?
            AND pago = ? ORDER BY id ASC; """, (tipopag, mes2, ano, pago))
        for i in lista:
            print(i)
            self.listaPag.insert("", END, values=i)
        self.entryValorDevido.delete(0, END)

        lista2 = self.cursor.execute("""SELECT  SUM(valordeduzir)
            FROM formapag WHERE tipopag = ? AND  substr(dia, 4,2) = ? AND substr(dia, 7,10) = ?
            AND pago = ? ORDER BY id ASC; """, (tipopag, mes2, ano, pago))
        for i in lista2:
            print(i)
            if i == '':
                self.entryValorDevido.insert(END, "0.00")
            else:
                self.entryValorDevido.insert(END, i)
        self.desconecta_Glac()

    def carregaConsulta2(self):
        mes = self.mesvar2.get()
        ano = self.anovar2.get()
        pago = self.entry72.get()

        ano = str(ano.replace("(", "").replace(")", "").replace(",", ""))
        mes = str(mes.replace("(", "").replace(")", "").replace(",", ""))
        mes2 = ''
        if mes == "'Janeiro'":
            mes2 = '01'
        elif mes == "'Fevereiro'":
            mes2 = '02'
        elif mes == "'Março'":
            mes2 = '03'
        elif mes == "'Abril'":
            mes2 = '04'
        elif mes == "'Maio'":
            mes2 = '05'
        elif mes == "'Junho'":
            mes2 = '06'
        elif mes == "'Julho'":
            mes2 = '07'
        elif mes == "'Agosto'":
            mes2 = '08'
        elif mes == "'Setembro'":
            mes2 = '09'
        elif mes == "'Outubro'":
            mes2 = '10'
        elif mes == "'Novembro'":
            mes2 = '11'
        elif mes == "'Dezembro'":
            mes2 = '12'

        self.conecta_Glac()
        self.listaPag.delete(*self.listaPag.get_children())

        lista = self.cursor.execute("""
            SELECT  ordem, tipopag, valordeduzir, dia, pago
            FROM formapag WHERE  substr(dia, 4,2) = ? AND substr(dia, 7, 4) = ?
            AND pago = ? ORDER BY id ASC; """, (mes2, ano, pago))
        for i in lista:
            self.listaPag.insert("", END, values=i)

        self.entryValorDevido.delete(0, END)

        lista2 = self.cursor.execute("""
            SELECT  SUM(valordeduzir)
            FROM formapag WHERE substr(dia, 4,2) = ? AND substr(dia, 7, 4) = ?
            AND pago = ? ORDER BY id ASC; """, (mes2, ano, pago))
        for i in lista2:
            print(i)
            self.entryValorDevido.insert(END, i)
        self.desconecta_Glac()

    def sel_pag_ordem(self):
        valortotal1 = self.entryValorTotal.get()

        numAt = self.listaNumOrc.get()
        self.entryNumAtend.insert(END, numAt)
        self.listaPag.delete(*self.listaPag.get_children())
        self.conecta_Glac()
        lista = self.cursor.execute("""SELECT  ordem, tipopag, valorpagar, valordeduzir, 
            dia, pago, id FROM formapag WHERE ordem = '%s'   ORDER BY id ASC; """ % numAt)
        for i in lista:
            self.listaPag.insert("", END, values=i)

        informe = self.cursor.execute("""SELECT SUM(valordeduzir) FROM formapag 
            WHERE ordem = '%s' AND pago = 'Sim' ORDER BY id ASC; """ % numAt)
        for i in informe:
            soma = float(i[0])
            soma = f'{i[0]:.2f}'
            self.entryValorInform.delete(0, END)
            self.entryValorInform.insert(END, soma)
            valor_devido = float(valortotal1) - float(soma)
            valor_devido = float(valor_devido)
            self.entryValorDevido.delete(0, END)
            self.entryValorDevido.insert(END, f'{valor_devido:.2f}')

        self.desconecta_Glac()