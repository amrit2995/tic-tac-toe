class Board:
    player1 = None
    player2 = None
    board = [[' ' for _ in range(3)] for _ in range(3)]

    def board_print(self):
        for i in range(3):
            print(f"{self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]}")
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
        self.valid_pos(player_inp)
        self.board_print()
        return

    def valid_pos(self, player):
        valid = False
        while not valid:
            pos = input(f"Enter a  pos for {player} :\n")
            if not pos.isnumeric():
                print("Position should be a number ")
            elif int(pos) not in range(1, 10):
                print("Position should be within range 1 to 9 ")
            else:
                i = (int(pos)-1)//3
                j = (int(pos)-1) % 3
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.player1 if player == 1 else self.player2
                    return
                else:
                    print("This position is already occupied.")

    def validate_victory(self, player_num):
        player = self.player1 if player_num == 1 else self.player2
        for i in range(3):
            row_v = "".join([self.board[i][j] for j in range(3)])
            col_v = "".join([self.board[j][i] for j in range(3)])
            if player*3 in [row_v, col_v]:
                print(f"Player{player_num} won !!!")
                return True
        if player*3 in ["".join(self.board[i][i] for i in range(3)), "".join(self.board[i][2-i] for i in range(3))]:
            print(f"Player{player_num} won !!!")
            return True

    def board_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return False
        print("Draw !!!")
        return True

    def reset_board(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]


if __name__ == "__main__":
    boardgame = Board()
    play_again = "y"
    # bot = input("Do you want to play with a bot ?: \n")
    #
    while play_again == 'y':
        boardgame.reset_board()
        vic1, vic2 = False, False
        boardgame.symbol_choice()
        while not (vic1 and vic2):
            # boardgame.board_print()
            boardgame.user_input(1)
            if boardgame.validate_victory(1) or boardgame.board_full() :
                break
            boardgame.user_input(2)
            if boardgame.validate_victory(2) or boardgame.board_full():
                break
        play_again = input("Do you want to continue:(y or n) \n").lower()