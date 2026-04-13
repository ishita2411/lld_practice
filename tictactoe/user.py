class User:
    def __init__(self, name, symbol):
        self.name = name
        self.symbolClass = symbol
    
    def get_symbol(self):
        return self.symbolClass.symbol
    
    def get_name(self):
        return self.name