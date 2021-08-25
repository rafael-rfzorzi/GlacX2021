from tkinter import *

class EditItens:
    def altera_itens_orc_quant(self):
        valor = self.valorItem.get()
        quant = self.quantItem.get()
        total = self.totalItem.get()
        valor = float(valor)
        quant = float(quant)
        self.totalItem.delete('0', 'end')
        soma = valor * quant
        soma = float(f'{soma:>8.2f}')
        self.totalItem.insert(END, soma)
    def altera_itens_orc_alterabt(self):
        valor = self.valorItem.get();
        quant = self.quantItem.get();
        total = self.totalItem.get()
        ordem = self.ordemItem.get();
        descr = self.descrItem.get();
        codigo = self.codigoItem.get()
        numorc = self.listaNumOrc.get();
        ordem2 = self.ordemItem.get()

        self.conecta_Glac()
        updateValor = self.cursor
        updateValor.execute("""UPDATE orcamento2 SET ordem_item = ?, desc_item = ?, 
            cod_item = ?, valor = ?, quant = ?, total = ? 
            WHERE id_orc2 = ? AND ordem_item = ?""",
                    (ordem, descr, codigo, valor, quant, total, numorc, ordem2))
        self.conn.commit()

        self.altOrcW.destroy()
        self.desconecta_Glac()
        self.atualiza_listaServProd()
        self.total_orc()
    def altera_itens_orc_deletabt(self):
        ordem = self.ordemItem.get();
        numorc = self.listaNumOrc.get();

        self.conecta_Glac()
        self.cursor.execute("""DELETE FROM orcamento2 WHERE ordem_item = ? AND id_orc2 = ?""", (ordem, numorc,))

        self.conn.commit()

        self.altOrcW.destroy()
        self.desconecta_Glac()
        self.atualiza_listaServProd()
        self.total_orc()