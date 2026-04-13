from symbol import X, O
from user import User
from board import Board

def main():
    n = 3
    board = Board(3)
    player1 = User("Player 1", X())
    player2 = User("Player 2", O())

    list_of_players = [player1, player2]
    i = 0

    while i < n*n:
        board.print_board()

        current_player = list_of_players[0]
        print(f"{current_player.get_name()}'s turn. Symbol: {current_player.get_symbol()}")
        input_n, input_m = input("Enter the position to place your symbol (row col): ").split()
        input_n, input_m = int(input_n), int(input_m)
        if board.set_piece_onBoard(input_n, input_m, current_player.get_symbol()):
            if board.is_winning_move(input_n, input_m, current_player.get_symbol()):
                print(f"{current_player.get_name()} wins!")
                return
            list_of_players.append(list_of_players.pop(0))  # Switch player
            i += 1
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
    