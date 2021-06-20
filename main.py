import random


class Board:
    players = {1: 'X', 2: 'O'}
    bot = False
    board = [[' ' for _ in range(3)] for _ in range(3)]

    def board_print(self):
        for i in range(3):
            print(f"{self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]}")
            if i < 2:
                print('-' * 11)
        # print("\n")
        print("*"*11)

    def valid_pos(self, player, pos):
        if not pos.isnumeric():
            print("Position should be a number ")
        elif int(pos) not in range(1, 10):
            print("Position should be within range 1 to 9 ")
        else:
            i = (int(pos) - 1) // 3
            j = (int(pos) - 1) % 3
            if self.board[i][j] == ' ':
                self.board[i][j] = self.players[player]
                self.board_print()
                return True
            else:
                print("This position is already occupied.")

    def validate_victory(self, player_num):
        player = self.players[player_num]
        for i in range(3):
            row_v = "".join([self.board[i][j] for j in range(3)])
            col_v = "".join([self.board[j][i] for j in range(3)])
            if player * 3 in [row_v, col_v]:
                print(f"Player{player_num} won !!!")
                return True
        if player * 3 in ["".join(self.board[i][i] for i in range(3)), "".join(self.board[i][2 - i] for i in range(3))]:
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


class Player:
    def __init__(self, player_num, bot):
        self.bot_enabled = bot
        self.player = player_num
        self.me = 'X' if self.player == 1 else 'O'
        self.opponent = 'O' if self.player == 1 else 'X'

    def two_in_row(self, sign, board):
        row_r, col_r, row_c, col_c = None, None, None, None
        for i in range(3):
            count_r, count_c = 0, 0
            for j in range(3):
                if board[i][j] == sign:
                    count_r += 1
                if board[i][j] == ' ':
                    row_r, col_r = i, j
                if board[j][i] == sign:
                    count_c += 1
                if board[j][i] == ' ':
                    row_c, col_c = j, i
                if count_r == 2 and (row_r, col_r) != (None, None):
                    return True, row_r, col_r
                if count_c == 2 and (row_c, col_c) != (None, None):
                    return True, row_c, col_c

        count_d1, row_d1, col_d1 = 0, None, None
        count_d2, row_d2, col_d2 = 0, None, None
        for i in range(3):
            if board[i][i] == sign:
                count_d1 += 1
            if board[i][i] == ' ':
                row_d1, col_d1 = i, i
        if count_d1 == 2 and (row_d1, col_d1) != (None, None):
            return True, row_d1, col_d1
        for i in range(3):
            if board[2 - i][i] == sign:
                count_d2 += 1
            if board[2 - i][i] == ' ':
                row_d2, col_d2 = 2-i, i
        if count_d2 == 2 and (row_d2, col_d2) != (None, None):
            return True, row_d2, col_d2
        return [False]

    def random_choice(self, board):
        empty_places = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    empty_places.append((i, j))
        return random.choice(empty_places)

    def input_pos(self, board):
        if not self.bot_enabled:
            return input(f"Enter a  pos for Player{self.player} :\n")
        else:
            got_2 = self.two_in_row(self.me, board)
            if got_2[0]:
                return got_2[1] * 3 + (got_2[2] + 1)
            got_2 = self.two_in_row(self.opponent, board)
            if got_2[0]:
                return got_2[1] * 3 + (got_2[2] + 1)
            row, col = self.random_choice(board)
            return row * 3 + (col + 1)


if __name__ == "__main__":
    boardgame = Board()
    play_again = "y"
    bot_enabled = True if input("Do you want to play with a bot (y or n)?: \n").lower() == 'y' else False
    choice = input("Choose your symbol X or O :").upper()

    user1 = Player(1, False if choice == 'X' else bot_enabled)
    user2 = Player(2, bot_enabled if choice == 'X' else False)

    while play_again == 'y':
        boardgame.reset_board()
        vic1, vic2 = False, False
        while not (vic1 and vic2):
            val1, val2 = False, False
            while not val1:
                val1 = boardgame.valid_pos(user1.player, str(user1.input_pos(boardgame.board)))

            if boardgame.validate_victory(user1.player) or boardgame.board_full():
                break

            while not val2:
                val2 = boardgame.valid_pos(user2.player, str(user2.input_pos(boardgame.board)))

            if boardgame.validate_victory(user2.player) or boardgame.board_full():
                break
        play_again = input("Do you want to continue:(y or n) \n").lower()
