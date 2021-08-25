from tkinter import *
from tkinter import ttk

class TerceiroFrame:
    def terceiro_frame(self):
        self.abas = ttk.Notebook(self.top3)
        self.frame_aba1 = Frame(self.abas)
        self.frame_aba2 = Frame(self.abas)
        self.frame_aba3 = Frame(self.abas)
        self.frame_aba4 = Frame(self.abas)

        self.frame_aba1.configure(background="gray20")
        self.frame_aba2.configure(background="gray20")
        self.frame_aba4.configure(background="gray20")

        self.label1 = Label(self.frame_aba1)
        self.label1.pack(padx=850, pady=225)
        self.label3 = Label(self.frame_aba3)
        self.label3.pack(padx=850, pady=225)
        self.label4 = Label(self.frame_aba4)
        self.label4.pack(padx=850, pady=225)
        self.abas.add(self.frame_aba2, text=self.m_Aba1)
        self.abas.add(self.frame_aba1, text=self.m_Aba3)
        self.abas.add(self.frame_aba4, text=self.m_Aba4)
        self.abas.pack(side="bottom")

        # Caixa de Seleção de Orçamento ou Ordem de Serviço
        self.Tipvar = StringVar()
        self.TipV = (self.m_Ordem, self.m_Orcamento)
        popupMenu = ttk.OptionMenu(self.top3, self.Tipvar, self.TipV[1], *self.TipV)
        popupMenu.place(relx=0.44, rely=-0.01, relwidth=0.15, height=25)



