from tkinter import *
from abc import ABC, abstractmethod


class QuoteAbstract(ABC):
    @abstractmethod
    def printQuote(self):
        pass


class StockQuoteMonitor(QuoteAbstract):
    # Initialising the class below.
    def __init__(self, frame, root, server, type, checkbox, quote):
        self.type = type
        self.root = root
        self.frame = frame
        self.client = server
        self.checkbox = checkbox
        self.quote = quote
        self.T = Text(self.frame, width=50, height=50)
        self.T.pack(side=LEFT)

    # Function to print the Quote data for the quote entered by the user.
    def printQuote(self):
        quit = False

        self.T.delete("1.0", END)
        while not quit:
            # If user wants to use the normal SOAP Service.
            if self.type == 1:
                # Get the quote data.
                result = self.client.service.getQuote(self.quote)
                fieldnames = self.client.service.getFieldNames()
            # If user wants to use the TimeLapse SOAP Service.
            else:
                # Get the quote data.
                result = self.client.service.getStockQuote(self.quote)
                fieldnames = self.client.service.getFieldNames()

            # Displaying the Quote Data on the text box widget.
            self.T.insert(END, "Stock quote data:\nSymbol: " + str(result[0]))
            self.T.insert(END, "\nPrice: " + str(result[1]))
            self.T.insert(END, "\nDate: " + str(result[2]))
            self.T.insert(END, "\nTime: " + str(result[3]))

            # Displaying the Quote Data on the Python Interpreter.
            print("Stock quote data: ")
            print("Symbol: " + result[0])
            print("Price: " + result[1])
            print("Date: " + result[2])
            print("Time: " + result[3])
            print("############################")

            # If the user doesn't want to update Quote data, then we simply end after displaying the values once.
            if self.checkbox == 0:
                quit = True
                break
            # Otherwise, it means that the user wants to continue updating the StockQuote Data.
            else:
                # The line waits 10 minutes and then contacts tht SOAP Service again to update the Quote Data.
                self.root.after(1000 * 600, self.printQuote)
                break
