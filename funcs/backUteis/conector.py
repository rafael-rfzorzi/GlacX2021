import sqlite3


class Conector:
    def conecta_Glac(self):
        self.conn = sqlite3.connect("glac.db")
        self.cursor = self.conn.cursor()

    def desconecta_Glac(self):
        self.conn.close()
