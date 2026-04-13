class Pizza:
    def __init__(self, size, base_price, tax_rate):
        self.size = size
        self.base_price = base_price
        self.tax_rate = tax_rate



class Topping:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Mushroom(Topping):
    def __init__(self, quantity):
        super().__init__("Mushroom", 40, quantity)
    def get_price(self):
        return self.price * self.quantity

class Corn(Topping):
    def __init__(self, quantity, pizza):
        super().__init__("Corn", 0, quantity)  # price is dynamic, so we’ll compute it in get_price
        self.pizza = pizza

    def get_price(self):
        if self.pizza.size == "Medium":
            return 50 + (self.quantity - 1) * 40
        elif self.pizza.size == "Large":
            return self.quantity * 20


class Cheeseburst(Topping):
    def __init__(self, quantity):
        super().__init__("Cheeseburst", 100, quantity)
    def get_price(self):
        return self.price + (self.price * (self.quantity -1))
    
class Onion(Topping):
    def __init__(self, quantity):
        super().__init__("Onion", 30, quantity)
    def get_price(self):
        return self.price * self.quantity

class PizzaOrder:
    def __init__(self, pizza):
        self.pizza = pizza
        print(pizza.base_price)
        self.toppings = []
        self.checkIfMushroomOrCheezeburst = False
    
    def add_topping(self, topping):
        if isinstance(topping, Topping):
            self.toppings.append(topping)
        
    def calculate_total_price(self):
        total_price = self.pizza.base_price
        for topping in self.toppings:
            if (type(topping) == Mushroom or type(topping) == Cheeseburst) and self.checkIfMushroomOrCheezeburst:
                continue
            if (type(topping) == Mushroom or type(topping) == Cheeseburst) and not self.checkIfMushroomOrCheezeburst:
                self.checkIfMushroomOrCheezeburst = True
            
            if type(topping) == Cheeseburst:
                self.pizza.tax_rate = 1.3 * self.pizza.tax_rate
            total_price += topping.get_price()
        print(total_price)

        total_price += (total_price * self.pizza.tax_rate/100)
        return total_price

    
    
pizza = Pizza("Medium", 350, 8)
order = PizzaOrder(pizza)
order.add_topping(Mushroom(2))
order.add_topping(Cheeseburst(1))
order.add_topping(Corn(2, pizza))
# order.add_topping(Onion(2))

print(order.calculate_total_price())

