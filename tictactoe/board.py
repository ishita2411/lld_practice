class Board:
    def __init__(self, n):
        self.board = [['_' for _ in range(n)] for _ in range(n)]
        self.n = n
    
    def set_piece_onBoard(self, x, y, symbol):
        if self.board[x][y] == '_':
            self.board[x][y] = symbol
            return True
        return False
    def is_winning_move(self, x, y, symbol):
        # Check row
        if all(self.board[x][col] == symbol for col in range(self.n)):
            return True
        
        # Check column
        if all(self.board[row][y] == symbol for row in range(self.n)):
            return True
        
        # Check main diagonal
        if x == y and all(self.board[i][i] == symbol for i in range(self.n)):
            return True
        
        # Check anti-diagonal
        if x + y == self.n - 1 and all(self.board[i][self.n - 1 - i] == symbol for i in range(self.n)):
            return True
        
        return False
    def print_board(self):
        for row in self.board:
            print(' '.join(row))