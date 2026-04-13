class Symbol:
    def __init__(self, symbol):
        self.symbol = symbol

class X(Symbol):
    def __init__(self):
        super().__init__("X")
class O(Symbol):
    def __init__(self):
        super().__init__("O")