from tkcalendar import DateEntry
from Janelas.estiloWidgets.widgets_Glac import *


class Aba1:
    def aba1(self):
        self.frameProb = GradientFrame(self.frame_aba1)
        self.frameProb.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.DescrProb = LabelGlac(self.frame_aba1, "   " + self.m_Atend1)
        self.DescrProb.place(relx=0.04, rely=0.04, relwidth=0.91, relheight=0.12)

        self.area1 = Entry(self.frame_aba1)
        self.area1.place(relx=0.05, rely=0.18, relwidth=0.9, relheight=0.1)

        self.area2 = Entry(self.frame_aba1)
        self.area2.place(relx=0.05, rely=0.285, relwidth=0.9, relheight=0.1)

        self.DescrProb2 = LabelGlac(self.frame_aba1, "   " + self.m_Atend2)
        self.DescrProb2.place(relx=0.04, rely=0.49, relwidth=0.91, relheight=0.12)

        self.area3 = Entry(self.frame_aba1)
        self.area3.place(relx=0.05, rely=0.63, relwidth=0.9, relheight=0.1)

        self.area4 = Entry(self.frame_aba1)
        self.area4.place(relx=0.05, rely=0.735, relwidth=0.9, relheight=0.1)

        descrInicio = LabelGlac(self.frame_aba1, 'Data inicial')
        descrInicio.place(relx=0.05, rely=0.045, relwidth=0.09, relheight=0.1)

        self.listInicio = DateEntry(self.frame_aba1, locale="pt_BR")
        self.listInicio.place(relx=0.14, rely=0.045, relwidth=0.1, relheight=0.1)

        descrFim = LabelGlac(self.frame_aba1, 'Data final')
        descrFim.place(relx=0.05, rely=0.495, relwidth=0.09, relheight=0.1)

        self.listFim = DateEntry(self.frame_aba1, locale="pt_BR")
        self.listFim.place(relx=0.14, rely=0.495, relwidth=0.1, relheight=0.1)