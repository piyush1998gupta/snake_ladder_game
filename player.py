class Player:
    def __init__(self, unique_id, name):
        """
        constructor for Player

        :param unique_id: starts from 0 that is
        player 1 -> 0
        player 2 -> 1


        :param name: name of that player
        """
        self.unique_id = unique_id
        self.name = name
        self.pos = None
        self.win = False

    @property
    def name(self):
        """ getter for name"""
        return self.__name

    @name.setter
    def name(self, name):
        """ setter for the name """
        self.__name = name

    @property
    def unique_id(self):
        """ getter for unique_id """
        return self.__unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """ setter for unique id """
        self.__unique_id = unique_id

    @property
    def win(self):
        """ getting the value whether the player os winner or not """
        return self.__win

    @win.setter
    def win(self, value):
        """ setting the value whether the player is winner or not """
        self.__win = value

    @property
    def pos(self):
        """
        getter for position
        :return: list containing x and y coordinates of that player in the board
        """
        return self.__pos

    @pos.setter
    def pos(self, pos):
        """
        setter for the position of that player
        :param pos: list containing x and y  coordinates
        :return: None
        """
        self.__pos = pos
