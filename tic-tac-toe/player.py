import math
import time
import random

class PlayerUno:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter


    def get_move(self, game):
        pass

class RandomCPU(PlayerUno):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):
        square = random.choice(game.avalible_move())
        return square

class HumanPlayer(PlayerUno):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square =False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.avalible_move():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid Square. Plz tac another toe")
        return val