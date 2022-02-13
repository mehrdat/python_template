# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pprint import pprint

class Board:
    """class for players"""

    def __init__(self, name,size,ships_number,player_type):
        self.name = name
        self.ships_number=ships_number
        self.size = size
        self.type=type
        self.board=[['.' for x in range(size)] for y in range(size)]
        self.ships=[]
        self.gusses=[]
        self.type = player_type

    def print(self):
        """ prit the rsults"""
        pprint(self.board)

    def guess():
        pass
    def add_ship():
        pass

    
def random_print(size):
    pass

def valid_coordination():
    pass

def populate_board():
    pass
def make_guess():
    pass

def play_game():
    pass

def new_game():
    """game starts here""" 

    board_size = 5
    ships_number = 4


    print('-----------------------------------------')
    print('Welcome to Battleship game')
    print(f"Board size is {board_size} number of ships are {ships_number}")
    print('Top left corner is row: 0  and col: 0')
    print('-----------------------------------------')

#creating the class
    name=input('Please enter your name : ')
    player_board=Board(name, board_size, ships_number,'player')
    #computer_board=Board('Computer', ships_number)

   # print(f"{player_board.name}'s board : ")
    
    player_board.print()




new_game()