from tkinter import *
from tkinter import ttk
import awesometkinter as atk
import sqlite3
from time import sleep
from PIL import Image, ImageTk


class StyleGlac(ttk.Style):
    def __init__(self, estilo="Treeview.Heading", fonte=('Arial', 10, 'bold'), backg="gray40",
                 foreg='gray80', field="gray30", **kwargs):
        ttk.Style.__init__(self, **kwargs)
        self.configure(style=estilo, font=fonte, background=backg, foreground=foreg, fieldbackground=field)

class LabelGlac(Label):
    def __init__(self, parent, texto="texto", backg="gray50", foreg='gray85', **kwargs):
        Label.__init__(self, parent, **kwargs)
        self.configure(text=texto, background=backg, foreground=foreg, font=('Arial', '8', 'bold'))

class GradientFrame(Canvas):
    def __init__(self, parent, color1="gray20", color2="gray40", **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.configure(bd=0, highlightthickness=0, relief='ridge')
        self.bind("<Configure>", self._draw_gradient)
    def _draw_gradient(self, event=None):
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1, g1, b1) = self.winfo_rgb(self._color1)
        (r2, g2, b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i, 0, i, height, tags=("gradient"), fill=color)
        self.lower("gradient")

class EntPlaceHold(Entry):
    def __init__(self, master=None, placeholder="Texto padrão", color='gray30'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()
    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color
    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

class Entry(ttk.Entry):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(style="EntryStyle.TEntry", font=('Calibri', 8))

class ButtonGlac(atk.Button3d):
    def __init__(self, parent, texto="texto", comando="comando", fundo='#456E96', **kwargs):
        atk.Button3d.__init__(self, parent, bg=fundo, **kwargs)
        self.configure(text=texto)
        self.configure(command=comando)

class AutocompleteEntrySP(Entry):
    def __init__(self, *args, **kwargs):
        #### Creating query for autocomplete
        conn = sqlite3.connect("glac.db")
        cursor = conn.cursor()

        self.lista2 = cursor
        self.lista2.execute("""SELECT cod_sp, '*****', LOWER(servprod), ' - ', tiposerv,
            ' - ' , LOWER(id_marcaprod) FROM servprod """)
        self.lista3 = cursor.fetchall()
        self.zlist = []
        for tup in self.lista3:
            t = str(tup).replace("('", "").replace("',)", "").replace(")", "")\
                .replace("'", "").replace(",", "").replace("(", "")
            self.zlist.append(t)
        cursor.close()

        Entry.__init__(self, *args, **kwargs)
        self.lista = self.zlist
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()
        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        self.configure(background='gray25', foreground='gray70')

        self.lb_up = False

    def changed(self, name, index, mode):
        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:
                if not self.lb_up:
                    self.lb = Listbox(bd=1, bg='gray25', fg='gray70')
                    self.lb.place(relx=0.075, rely=0.102, relheight=0.32, relwidth=0.43)
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb_up = True
                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END, w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False

    def selection(self, event):
        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)

    def up(self, event):
        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':
                self.lb.selection_clear(first=index)
                index = str(int(index) - 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)

    def down(self, event):
        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:
                self.lb.selection_clear(first=index)
                index = str(int(index) + 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)

    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*')
        return [w for w in self.lista if re.match(pattern, w)]

class ButtonGlac2(Button):
    def __init__(self, parent, texto="texto", comando="comando", **kwargs):
        Button.__init__(self, parent, **kwargs)
        photo = PhotoImage(file='circulo.png')
        self.configure(image=photo)
        self.configure(text=texto)
        self.configure(command=comando)
