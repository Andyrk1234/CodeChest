from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.dates as mdates
import time
from matplotlib.backends.backend_tkagg import Figure
from abc import ABC, abstractmethod

f = Figure(figsize=(6, 6), dpi=100)
ax = f.add_subplot(111)


class GraphAbstract(ABC):
    @abstractmethod
    def __init__(self):
        server = Server(url).getServer()
        self.type = type
        self.frame = Toplevel(root)
        self.client = server
        self.checkbox = 0
        self.quote = "NAB"
        # a.plot(Value, Time)
        self.canvas = FigureCanvasTkAgg(f, master=self.frame)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvas.get_tk_widget().update_idletasks()
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.frame)
        self.toolbar.update()
        ax.set_xlabel("Dates")
        ax.set_ylabel("Stock Values")

    def createGraph(self):
        quote = "NAB"
        server = Server(url).getServer()
        result = server.service.getQuote(quote)
        print(result)
        present = time.strftime("%d/%m/%Y")
        dated = str(result[2])
        value = str(dated) + " " + str(result[3])
        Date = matplotlib.dates.datestr2num(value)

        # a.set_xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016])  # Tickmark + label at every plotted point
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y %H:%M'))
        # ax.plot_date(x=Date, y=result[1], ls="-", marker='o', fmt="r-", c='red')
        # plt.scatter(Date, result[1])
        ax.plot(Date, result[1], '-o')
        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
        self.canvas.show()
        print("heyy")


class StockGraphMonitor:
    # Setting up the initial values of the class.
    # It creates widgets available in the tkinter pakcage and integrates them with the matplotlib library.
    def __init__(self, ax, f, frame, server, type, checkbox, quote):
        self.type = type
        self.ax = ax
        self.f = f
        self.frame = frame
        self.client = server
        self.checkbox = checkbox
        self.quote = quote
        # a.plot(Value, Time)
        self.canvas = FigureCanvasTkAgg(self.f, master=self.frame)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvas.get_tk_widget().update_idletasks()
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.frame)
        self.toolbar.update()
        ax.set_xlabel("Dates")
        ax.set_ylabel("Stock Values")

    # Creates a graph by plotting Stock Value vs. Date time.
    def createGraph(self):

        if self.type == 1:
            result = self.client.service.getQuote(self.quote)
            fieldnames = self.client.service.getFieldNames()
        else:
            result = self.client.service.getStockQuote(self.quote)
            fieldnames = self.client.service.getFieldNames()
        print(result)
        present = time.strftime("%d/%m/%Y")
        dated = str(result[2])
        value = str(dated) + " " + str(result[3])
        Date = matplotlib.dates.datestr2num(value)

        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y %H:%M'))
        # ax.plot_date(x=Date, y=result[1], ls="-", marker='o', fmt="r-", c='red')
        self.ax.plot(Date, result[1], '-o')

        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
        self.canvas.show()
        print("heyy")
