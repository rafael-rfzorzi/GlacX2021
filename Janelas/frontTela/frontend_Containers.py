import awesometkinter as atk


class Containers:
    def containers(self):
        # Primeiro Container da janela
        self.top = atk.Frame3d(self.janela)
        self.top.place(relx=0, rely=0, relwidth=1, relheight=0.11)

        # Segundo Container da Janela
        self.top2 = atk.Frame3d(self.janela)
        self.top2.place(relx=0, rely=0.111, relwidth=1, relheight=0.225)

        # Terceiro Container da janela
        self.top3 = atk.Frame3d(self.janela)
        self.top3.place(relx=0, rely=0.34, relwidth=1, relheight=0.465)

        # Quarto Container da Janela
        self.top4 = atk.Frame3d(self.janela)
        self.top4.place(relx=0, rely=0.805, relwidth=1, relheight=0.1)

        # Quinto Container da janela
        self.top5 = atk.Frame3d(self.janela)
        self.top5.place(relx=0, rely=0.905, relwidth=1, relheight=0.1)


