from abc import ABC, abstractmethod
class Pizza(ABC):
    @abstractmethod
    def getDescription(self):
        pass

    @abstractmethod
    def getCost(self):
        pass

class VeggiePizza(Pizza):
    def getDescription(self):
        return "Veggie Pizza"

    def getCost(self):
        return 100

class NonVeggiePizza(Pizza):
    def getDescription(self):
        return "Non Veggie Pizza"

    def getCost(self):
        return 150