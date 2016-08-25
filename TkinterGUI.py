from StockQuote import StockQuoteMonitor
from StockGraph import StockGraphMonitor
from tkinter import *
from SOAPServer import Server, url, url2
from Main import root, ax, f


class GUI:
    # Initialises the entire GUI by creating and placing widgets, performing different functions as can be observed
    # below.
    def __init__(self, frame):
        self.frame = frame
        self.var = IntVar()

        self.label_2 = Label(self.frame, text="StockQuote Data", bd=3, relief=FLAT)

        self.label_2.pack(side=LEFT)
        self.label_2.place(relx=0.2, rely=0.4)

        self.user_text = StringVar()
        self.entry = Entry(self.frame, text="Stock Quote Name", textvariable=self.user_text)
        self.entry.pack(side=LEFT, anchor=W)
        self.entry.place(relx=0.4, rely=0.4)

        self.c = Checkbutton(self.frame, text="Keep updating the stock", variable=self.var)
        self.c.pack(side=BOTTOM, anchor=E)
        self.c.place(relx=0.2, rely=0.5)
        self.button_1 = Button(self.frame, text="Show Stock Data", command=self.StockQuote)
        self.button_2 = Button(self.frame, text="Show Stock Graph", command=self.StockGraph)
        self.button_1.pack(side=RIGHT and BOTTOM, anchor=CENTER)
        self.button_2.pack(side=TOP, anchor=CENTER)
        self.button_2.place(relx=0.62, rely=0.4)
        self.button_1.place(relx=0.62, rely=0.5)

        self.button_3 = Button(self.frame, text="Quit", command=self.frame.quit)
        self.button_3.pack(side=LEFT and BOTTOM, anchor=CENTER)
        self.button_3.place(relx=0.5, rely=0.7)

        self.v = IntVar()
        self.radio1 = Radiobutton(self.frame, text="Normal Web Server", variable=self.v, value=1)
        self.radio1.pack(anchor=W)
        self.radio2 = Radiobutton(self.frame, text="Time Lapse Web Server", variable=self.v, value=2)
        self.radio2.pack(anchor=W)
        # self.radio1.place(relx=0.2, rely=0.4)
        # self.radio2.place(relx=0.2, rely=0.5)

    # En-route to printing the StockQuote Information.
    def StockQuote(self):
        server = Server(url).getServer()
        if self.v.get() == 1:
            server = Server(url).getServer()
        elif self.v.get() == 2:
            server = Server(url2).getServer()
        checkbox = self.var.get()
        quote = self.user_text.get()
        server_type = self.v.get()
        print(server)
        Quote(server, server_type, checkbox, quote)

    # En-route to displaying the live monitoring of how the StockQuote value changes with time, i.e. displaying a live
    # updating graph.

    def StockGraph(self):

        server_choice = self.v.get()
        if server_choice == 1:
            server = Server(url).getServer()
        else:
            server = Server(url2).getServer()
        quote = self.user_text.get()
        checkbox = self.var.get()
        print(server)
        # Time.clear()
        # Value.clear()
        # print(server.service.__getattr__())
        Graph(server, server_choice, checkbox, quote)
        # Create Graph Monitor of a stock.
        # Use both the SOAP Services.

    def getEntry(self):
        return self.user_text.get()

    def getFrame(self):
        return self.frame


def Quote(server, server_type, checkbox, quote):
    window = Toplevel(root)
    window.geometry('400x400')
    monitor = StockQuoteMonitor(window, server, server_type, checkbox, quote)
    monitor.printQuote()


def Graph(server, server_choice, checkbox, quote):
    ax.clear()
    window = Toplevel(root)
    monitor = StockGraphMonitor(window, server, server_choice, checkbox, quote)
    print("hey")
    flag = False
    while not flag:
        monitor.createGraph()
        # Waits 3 minutes before updating the graph.
        f.canvas.start_event_loop(180)
