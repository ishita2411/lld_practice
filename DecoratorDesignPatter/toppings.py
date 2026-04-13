from abc import ABC, abstractmethod

class Topping():
    def __init__(self, pizza):
        self.pizza = pizza
        self.cost = self.pizza.getCost()


class Veggies(Topping):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = self.cost + 10

    def getCost(self):
        return self.cost

class Cheese(Topping):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = self.cost + 30  
    def getCost(self):
        return self.cost