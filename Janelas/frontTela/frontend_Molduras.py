import awesometkinter as atk


class Molduras:
    def molduras(self):
        # Moldura dos dados do cliente
        self.FrameCliente = atk.Frame3d(self.top2)
        self.FrameCliente.place(relx=0, rely=0, relwidth=0.6, relheight=1)

        # Lista das placas de veiculos do cliente
        self.FrameAut2 = atk.Frame3d(self.top2)
        self.FrameAut2.place(relx=0.6, rely=0.002, relwidth=0.1, relheight=1)

        # Moldura dos dados veiculo
        self.FrameAut = atk.Frame3d(self.top2)
        self.FrameAut.place(relx=0.7, rely=0.002, relwidth=0.3, relheight=1)

