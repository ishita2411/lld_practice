'''
Question : Implement Amazon Notify Funtionality for Iphone stock availability
'''

from abc import ABC, abstractmethod

class StockObservable(ABC): # Inherit from ABC
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def notifySubscribers(self):
        pass

    @abstractmethod
    def getStockCount(self):
        pass
    
    def setStockCount(self, count):
        pass

class IphoneObservable(StockObservable):
    def __init__(self):
        self.observerList = []
        self.stockCount = 0

    def add(self, observer):
        self.observerList.append(observer)

    def remove(self, observer):
        self.observerList.remove(observer)

    def notifySubscribers(self):
        for observer in self.observerList:
            observer.update()

    def getStockCount(self):
        return self.stockCount
    
    def setStockCount(self, newStockAdded):
        if self.stockCount == 0:
            self.notifySubscribers()
        self.stockCount = self.stockCount + newStockAdded
