class Board:
    """
    class Board which helps in creation  of snake ladder game board containing snakes and ladders
    """
    def __init__(self):
        """  initialize the board with size n
            enter the number of snakes and one by one enter the snake value from and to
            enter the number of ladder and one by one enter the ladder value from and to
        """
        print("----------------------")
        print("Create your board")
        print("----------------------")
        n = int(input("enter the size of the board"))
        self.__size = n
        self.__board = list(([-1] * n) for i in range(n))
        self.__snakes = self.add_snakes()
        self.__ladders = self.add_ladders()

    def calculate_position(self, value):
        """
        find out the coordinates x and y from the number on the board

        some examples are (board size 10 * 10 ):
                9 - > (9,8)
                66 -> (3,5)

        :param value: the number on the board

        :return: x and y coordinates of the board after conversion
        """
        n = self.__size
        x = int((value - 1) / n)
        y = int((value - 1) % n)
        if x % 2 != 0:
            y = n - 1 - y
        x = n - 1 - x
        return x, y

    def add_snakes(self):
        """
        add snakes in the board

        :return: list of snakes in the board
        """
        sn = int(input("Enter the number of snakes in your board:"))
        snake_list = []
        for i in range(sn):
            print("enter the snake" + str(i + 1) + " :")
            from_ = int(input("from"))
            to_ = int(input("to"))
            x, y = self.calculate_position(from_)
            self.__board[x][y] = to_
            snake_list.append([from_, to_])
        return snake_list

    def add_ladders(self):
        """
        add ladders in the board

        :return: list of ladders in the board
        """
        ld = int(input("Enter the number of ladders in your board:"))
        ladder_list = []
        for i in range(ld):
            print("enter the ladder" + str(i + 1) + " :")
            from_ = int(input("from"))
            to_ = int(input("to"))
            x, y = self.calculate_position(from_)
            self.__board[x][y] = to_
            ladder_list.append([from_, to_])
        return ladder_list

    @property
    def snakes(self):
        """ return the list of snakes """
        return self.__snakes

    @property
    def ladders(self):
        """ return the list of ladders """
        return self.__ladders

    @property
    def board(self):
        """
        :return:  the board with snakes and ladders
        """
        return self.__board

    def display(self):
        """
        display the board
        :return: none
        """
        for row in self.__board:
            for col in row:
                print(col, end=" ")
            print()


# b = Board()
# b.display()
# snake=b.snakes
# ladder=b.ladders
# print("snakes :")
# for ele in snake:
#     print(str(ele[0])+" : "+str(ele[1]))
# print("ladders :")
# for ele in ladder:
#         print(str(ele[0]) + " : " + str(ele[1]))
