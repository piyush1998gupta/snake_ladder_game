from snake_ladder import SnakeLadderGame
from player import Player
from board import Board

players = []  # initialize the player

print('------------------------------------------------------------')
print('                 SNAKE - LADDER GAME                        ')
print('------------------------------------------------------------')

n = int(input('Enter the number of Player\'s:'))

for i in range(n):
    name = input('Enter the player' + str(i + 1) + ' name : ')
    players.append(Player(i, name))



# default board
board_game = [
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

# create the board with snakes and ladders
# board_game = Board()
# game = SnakeLadderGame(players, board_game.board)

# initialize the game with players and board
game = SnakeLadderGame(players)

# start the game
rounds = game.start()
print()
print("-------------------WINNER--------------------------")
print(game.winner.name + "  is  a winner")
print("game finish in "+str(rounds)+" rounds")
print("---------------------------------------------------")

# game.pos_board_display()




