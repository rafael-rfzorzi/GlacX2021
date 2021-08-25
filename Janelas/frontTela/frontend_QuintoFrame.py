from Janelas.estiloWidgets.widgets_Glac import LabelGlac
from tkinter import messagebox
import awesometkinter as atk

class QuintoFrame:
    def quinto_frame(self):
        #  Label Licença
        licenciamento = LabelGlac(self.top5, self.Licenca)
        licenciamento.configure(bg='gray20')
        licenciamento.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.4)

        def funcpag():
            if self.listaNumOrc.get() == "":
                msg = "É necessário que um Orçamento ou Ordem de Serviço esteja " \
                      "devidamente carregada na tela!!!"
                messagebox.showinfo("GLAC", msg)
            elif self.listaNumOrc.get() == "Numero":
                msg = "É necessário que um Orçamento ou Ordem de Serviço esteja " \
                      "devidamente carregada na tela!!!"
                messagebox.showinfo("GLAC", msg)
            else:
                self.pagaOrdem()

        # Botao Forma de Pagamento
        formapag = atk.Button3d(self.top5, text=self.m_Forma + '  $$$', command=funcpag)
        formapag.place(relx=0.8, rely=0.1, relwidth=0.18, relheight=0.8)

