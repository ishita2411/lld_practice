from pizza import VeggiePizza, NonVeggiePizza
from toppings import Veggies, Cheese

if __name__ == "__main__":
    pizza = Cheese(VeggiePizza())
    print(pizza.getCost())