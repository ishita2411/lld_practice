class Pieces:
    def __init__(self):
        self.moves = []

class King(Pieces):
    def __init__(self):
        super().__init__()
        self.moves = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]