import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import Dados_finanças as dfi

class Aplicacao(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Dados Financeiros")

        # Criação dos widgets e páginas
        self.frames = {}
        for Pagina in (Pagina1, Pagina2, Pagina3):
            frame = Pagina(self)
            self.frames[Pagina] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_pagina(Pagina1)

    def mostrar_pagina(self, cont, *args, **kwargs):
        frame = self.frames[cont]
        frame.atualizar()
        frame.tkraise()


#Bitcoin
class Pagina1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.config(bg="lightgray")

        # Configuração do gráfico na página 1
        self.figura1 = Figure(figsize=(16, 9), dpi=100)
        self.plot1 = self.figura1.add_subplot(111)
        self.plot1.plot(dfi.btc_Dates(), dfi.btc_Close())
        self.plot1.set_title("Preço do Bitcoin Em Dollar")
        self.plot1.set_xlabel("Data")
        self.plot1.set_ylabel("Preço do bitcoin(USD)")
        self.plot1.fill_between(dfi.btc_Dates() ,dfi.btc_High(), dfi.btc_Low(), alpha=0.2, color='red')


        self.canvas1 = FigureCanvasTkAgg(self.figura1, self)
        self.canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Adiciona um botão na página 1 para USD_BRL
        self.botao = tk.Button(self, text="Dollar", command=lambda: master.mostrar_pagina(Pagina2))
        self.botao.pack(side=tk.BOTTOM)

        # Adiciona um botão na página 1 para EUR_BRL
        self.botao = tk.Button(self, text="Euro", command=lambda: master.mostrar_pagina(Pagina3))
        self.botao.pack(side=tk.BOTTOM)

    def atualizar(self):
        pass

#USD_BRL
class Pagina2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.config(bg="lightgray")

        # Configuração do gráfico na página 2
        self.figura2 = Figure(figsize=(16, 9), dpi=100)
        self.plot2 = self.figura2.add_subplot(111)
        self.plot2.plot(dfi.USD_BRL_DATES(), dfi.USD_BRL_Close())
        self.plot2.set_title("Preço do dollar em Real")
        self.plot2.set_xlabel("Data")
        self.plot2.set_ylabel("BRL")
        self.plot2.fill_between(dfi.USD_BRL_DATES(), dfi.USD_BRL_High(), dfi.USD_BRL_Low(), alpha=0.2, color='red')

        self.canvas2 = FigureCanvasTkAgg(self.figura2, self)
        self.canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Adiciona um botão na página 2 para BTC
        self.botao = tk.Button(self, text="Bitcoin", command=lambda: master.mostrar_pagina(Pagina1))
        self.botao.pack(side=tk.BOTTOM)

        # Adiciona um botão na página 2 para EUR_BRL
        self.botao = tk.Button(self, text="Euro", command=lambda: master.mostrar_pagina(Pagina3))
        self.botao.pack(side=tk.BOTTOM)

    def atualizar(self):
        pass


#EUR_BRL
class Pagina3(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.config(bg="lightgray")

        # Configuração do gráfico na página 3
        self.figura3 = Figure(figsize=(16, 9), dpi=100)
        self.plot3 = self.figura3.add_subplot(111)
        self.plot3.plot(dfi.EUR_BRL_DATES(), dfi.EUR_BRL_Close())
        self.plot3.set_title("Preço do Euro em Reais")
        self.plot3.set_xlabel("Data")
        self.plot3.set_ylabel("BRL")
        self.plot3.fill_between(dfi.EUR_BRL_DATES(), dfi.EUR_BRL_High(), dfi.EUR_BRL_Low(), alpha=0.2, color='red')

        self.canvas3 = FigureCanvasTkAgg(self.figura3, self)
        self.canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Adiciona um botão na página 3 para BTC
        self.botao = tk.Button(self, text="Bitcoin", command=lambda: master.mostrar_pagina(Pagina1))
        self.botao.pack(side=tk.BOTTOM)

        # Adiciona um botão na página 3 para USD_BRL
        self.botao = tk.Button(self, text="Dolar", command=lambda: master.mostrar_pagina(Pagina2))
        self.botao.pack(side=tk.BOTTOM)

    def atualizar(self):
        pass

app = Aplicacao()
app.geometry("1600x940")
app.mainloop()
