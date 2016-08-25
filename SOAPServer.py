from suds.client import Client
from abc import ABC, abstractmethod

url = "http://viper.infotech.monash.edu.au:8180/axis2/services/StockQuoteServiceStageOne?wsdl"
url2 = "http://viper.infotech.monash.edu.au:8180/axis2/services/StockQuoteTimeLapseService?wsdl"


class ServerAbstract(ABC):
    @abstractmethod
    def getServer(self):
        pass


class Server(ServerAbstract):
    def __init__(self, url):
        self.client = Client(url)

    def getServer(self):
        return self.client
