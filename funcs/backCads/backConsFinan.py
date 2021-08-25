from tkinter import *


class ConsFinan:
    def OnDoubleClickFinan(self, event):
        self.limpa_produto()
        self.listaServ.selection()
        for n in self.listaServ.selection():
            col1, col2, col3, col4 = self.listaServ.item(n, 'values')
            self.entradaCodprod.insert(END, col1)
            self.carrega_produto()

    def carrega_receita(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        self.listaServ2.delete(*self.listaServ2.get_children())

        ano = self.entry5.get()
        mes = self.entry6.get()
        ano = str(ano.replace("(", "").replace(")", "").replace(",", ""))
        mes = str(mes.replace("(", "").replace(")", "").replace(",", ""))
        mes2 = ''
        if mes == "'Janeiro'" : mes2 = '01'
        elif mes == "'Fevereiro'" : mes2 = '02'
        elif mes == "'Março'" : mes2 = '03'
        elif mes == "'Abril'" : mes2 = '04'
        elif mes == "'Maio'" : mes2 = '05'
        elif mes == "'Junho'" : mes2 = '06'
        elif mes == "'Julho'" : mes2 = '07'
        elif mes == "'Agosto'" : mes2 = '08'
        elif mes == "'Setembro'" : mes2 = '09'
        elif mes == "'Outubro'" : mes2 = '10'
        elif mes == "'Novembro'" : mes2 = '11'
        elif mes == "'Dezembro'": mes2 = '12'

        lista = self.cursor.execute("""select id_orc1, placa_orc, dia, 
            (select (sum(total)) from orcamento2 where id_orc2 = id_orc1) from orcamento1 
            where substr(dia, 7,10) = '%s' and substr(dia, 4,2) = '%s' 
            and tipoOrc != 'Orçamento' order by dia asc; """ % (ano, mes2))
        for i in lista:
            self.listaServ.insert("", END, values=i)

        lista2 = self.cursor.execute("""select substr(dia, 7,10), substr(dia, 4,2), 
            sum(trim(replace(totalizador, ',', '.'),'R$'))
            from orcamento1 where substr(dia, 7,10) = '%s' and substr(dia, 4,2) = '%s'
            and tipoOrc != 'Orçamento'; """ % (ano, mes2))
        for i in lista2:
            self.listaServ2.insert("", END, values=i)
        self.desconecta_Glac()

    def limpa_receita(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.listaServ2.delete(*self.listaServ2.get_children())
