import random


class SnakeLadderGame:
    # default board_game
    board_game_default = [
        [-1, 78, -1, -1, -1, 75, -1, 73, -1, -1],
        [-1, -1, -1, -1, -1, -1, 24, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, 91],
        [-1, 19, 81, 60, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, 34, -1, -1, 67],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [59, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, 84, -1, -1],
        [38, -1, -1, 7, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 14, -1, -1, -1, -1, 31, -1],
    ]

    def __init__(self, players, board=None):
        """
        constructor of Game
        :param players:  list of players playing the game
        :param board: snake ladder board  - by default there is given one board
            board in the form of -1 and values
            -1 denotes no snake and ladder
            value denotes the jump to or push down to that value

        values:
         winner = winner of this game
         size = length of the board
         pos_board = display the board in which each player position is given by its id
        """
        if board is None:
            board = SnakeLadderGame.board_game_default
        self.players = players
        self.winner = None
        self.board_game = board
        self.size = len(self.board_game)
        self.pos_board = list(([-1] * self.size) for i in range(self.size))

    def pos_board_display(self):
        """ display the board in which each player position is given by its id """
        for row in self.pos_board:
            for col in row:
                print(col, end=" ")
            print()

    @property
    def board_game(self):
        """ board game getter """
        return self.__board_game

    @board_game.setter
    def board_game(self, board):
        """ board game setter """
        self.__board_game = board

    @property
    def size(self):
        """ size getter"""
        return self.__size

    @size.setter
    def size(self, size):
        """size setter"""
        self.__size = size

    @property
    def roll_dice(self):
        """
        :return: random integer between 1 and 6 (both inclusive)
        """
        return random.randint(1, 6)

    @property
    def players(self):
        """
        getter
        :return:list of players
        """
        return self.__players

    @players.setter
    def players(self, players):
        """ setter
        :param players: list of players
        :return: None
        """
        self.__players = players

    @property
    def winner(self):
        """ returns the winner of that game """
        return self.__winner

    @winner.setter
    def winner(self, player):
        """ setter of the winner of that board"""
        self.__winner = player

    def placed(self, x, y, player):
        """
        place the player into new position

        :param x: x coordinates
        :param y: y coordinates
        :param player: current player turn
        :return:  whether curr player cuts the giti or not
        """
        player.pos = [x, y]
        flag = False
        # some player is already in that position and that player is not current player ( snakes bites and move to
        # current position )
        if self.pos_board[x][y] != -1 and self.pos_board[x][y] != player.unique_id:
            pl_id = self.pos_board[x][y]
            print("It cuts the giti of " + self.players[pl_id].name + " and get another chance of rolling a dice .")
            self.players[pl_id].pos = None
            flag = True
        self.pos_board[x][y] = player.unique_id
        return flag

    def calculate_target_value(self, x, y):
        """
            find out the number on the board from the coordinates

            some examples are (board size 10 * 10 ):
                    (9,8) -> 9
                    (3,5) -> 66

            :param x: x coordinate
            :param y: y coordinate

            :return: value on the board after conversion
        """
        n = self.size - 1
        # print("(" + str(x) + "," + str(y) + ")-->", end=" ")
        x = n - x
        if x % 2 != 0:
            y = n - y
        value = (x * (n + 1)) + y + 1
        # print(str(value))
        return value

    def calculate_position(self, value):
        """
            find out the coordinates x and y from the number on the board

            some examples are (board size 10 * 10 ):
                    9 - > (9,8)
                    66 -> (3,5)

            :param value: the number on the board

            :return: x and y coordinates of the board after conversion
        """
        n = self.size
        x = int((value - 1) / n)
        y = int((value - 1) % n)
        if x % 2 != 0:
            y = n - 1 - y
        x = n - 1 - x
        # print(str(value)+"---->"+"(" + str(x) + "," + str(y) + ")")
        return x, y

    def move(self, player):
        """
        this is the main function in which
        player first roll the dice then move to the new position and checks accordingly
        if it gets 6 on dice it gets another chance
        and also on a new position if there is another player it cuts the giti of the that player
        """
        dice = self.roll_dice  # random value on the dice from 1 and 6
        print(" rolls a dice and get number " + str(dice), end=", ")
        new_turn = False  # new turn whenever player cuts the giti of another player
        if player.pos is None:  # player is at home
            if dice == 1 or dice == 6:  # when player open its giti only on 6 and 1
                print("and opens its giti ", end=", ")
                player.pos = [self.size - 1, -1]  # set the position to bottommost leftmost corner
            else:  # didn't open its giti
                print("but is at home ", end=", ")

        else:
            x, y = player.pos  # current position of that player
            n = self.size   # size of the board
            curr_val = self.calculate_target_value(x, y)  # value of the board on that coordinates x and y
            tar_val = curr_val + dice  # new value in which player to move
            if tar_val <= n * n:  # when the move is possible on the board
                new_x, new_y = self.calculate_position(tar_val)
                if self.board_game[new_x][new_y] == -1:  # no snake or ladder on that position
                    print("and move from " + str(curr_val) + " to " + str(tar_val), end=", ")
                    new_turn = self.placed(new_x, new_y, player)  # place the player to that position and return
                    # whether it cuts the giti of another player
                else:  # exist snake or ladder in that position
                    print("and move from " + str(curr_val) + " to " + str(tar_val), end=", ")
                    value = tar_val  # position at which snake or ladder exist
                    tar_val = self.board_game[new_x][new_y]  # the new position after snake bites or ladder jump
                    if value < tar_val:  # ladder:- new value greater than old
                        print("and ladder @ " + str(value) + ": jump to " + str(tar_val), end=", ")
                    else:  # snake :- new value is smaller than current value
                        print("and Snake bites @ " + str(value) + ": push down to  " + str(tar_val), end=", ")
                    new_x, new_y = self.calculate_position(tar_val)  # calculate the x and y from the value
                    new_turn = self.placed(new_x, new_y, player)  # place the player to that position and return
                    # whether it cuts the giti of another player
                # when the player is not at home and change its previous position to -1 that is reset in the pos board
                if y != -1:
                    self.pos_board[x][y] = -1
                # this player reach the destination and declared as winner
                if tar_val == (n * n):
                    self.winner = player  # set the winner of this game
                    player.win = True  # change the status of the player to winner
                    return

            else:  # when move is not possible
                print("new position is " + str(tar_val) + " which is not possible on the board ", end=" ")
                return
        if new_turn:  # when again turn when players cuts the giti of another player
            self.move(player)
        elif dice == 6:  # again turn when there is 6 on dice
            print("and gets another chance as 6 on the last dice roll")
            self.move(player)

    def start(self):
        """ start the game with player 1 and so on """
        idx = 0  # starting from index 0
        curr_player = self.players[idx]  # curr _palyer starts from player 1
        rounds = 0  # number of rounds in a game
        while not curr_player.win:
            if idx == 0:
                rounds += 1
            curr_player = self.players[idx]
            print(curr_player.name + " turns : ")
            self.move(curr_player)
            idx += 1  # next player turn
            idx = idx % len(self.players)  # after last player then player 1 gets turn
            print()
        return rounds
