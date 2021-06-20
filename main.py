# create 3*3 matrix
# UI class
# user entry
# computer entry
import random
board = []
symbols = {'O': 0, 'X': 1}
# board = [[' ' for _ in range(3)] for _ in range(3)]


class Board:
    player1 = None
    player2 = None
    board = [[' ' for _ in range(3)] for _ in range(3)]

    def board_print(self):
        for i in range(3):
            print(f"{board[i][0]} | {board[i][1]} | {board[i][2]}")
            if i < 2:
                print('-' * 11)

    def symbol_choice(self):
        choice = None
        count = 0
        while choice not in ["X", "O"]:
            choice = input('Choose the Symbol for Player1 : \n').upper()
            if choice == 'X':
                self.player1, self.player2 = ['X', 'O']
                return
            elif choice == 'O':
                self.player1, self.player2 = ['O', 'X']
                return

    def user_input(self, player_inp):
        player = self.player1 if player_inp == 1 else self.player2
        pos = 0
        while pos not in range(1, 10):
            pos = input(f"Input position for Player{player_inp}:\n")
            if pos.isalnum():
                pos = int(pos)
            if pos in range(1, 10):
                pos = int(pos)
                board[(pos - 1)//3][(pos - 1) % 3] = player
                self.board_print()
                return

    def validate_victory(self, player):
        player = self.player1 if player == 1 else self.player2
        for i in range(3):
            row_v = "".join([board[i][j] for j in range(3)])
            col_v = "".join([board[j][i] for j in range(3)])
            if player*3 in [row_v, col_v]:
                return True
        if player*3 in ["".join(board[i][i] for i in range(3)), "".join(board[i][2-i] for i in range(3))]:
            return True

    def board_full(self):
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    return True
        return False


if __name__ == "__main__":
    boardgame = Board()
    play_again = "y"
    while play_again == 'y':
        reset_board()
        vic1, vic2 = False, False
        boardgame.symbol_choice()
        while not (vic1 and vic2):
            # boardgame.board_print()
            boardgame.user_input(1)
            if boardgame.validate_victory(1) :
                print('Player1 Wins')
                break
            boardgame.user_input(2)
            if boardgame.validate_victory(2):
                print('Player2 Wins')
                break
            if not boardgame.board_full():
                print("Game Draw!")
                break
        play_again = input("Do you want to continue:(y or n) \n").lower()