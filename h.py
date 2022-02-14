#https://p3-battleships.herokuapp.com

from pprint import pprint 
import random 
 
 
class Board: 
     
 
    def __init__(self,name,size,num_ships,player_type): 
         
        self.name=name 
        self.player_type=player_type 
        self.num_ships=num_ships 
        self.size=size 
        self.board=[["." for x in range(size)] for y in range(size)] 
        self.gusses=[] 
        self.ships=[] 
         
         
    def print(self): 
        for row in self.board:
            print("  ".join(row))
         
         
    def guess(self,x,y):
        self.gusses.append((x,y))
        self.board[x][y]='X'
        if (x,y) in self.ships:
            board[x][y]='*'
            return 'Hit'
        else:
            return 'Miss'
    
 
    def add_ship(self , x , y , type="computer"): 
        if len(self.ships)>= self.num_ships:
            print('Error! You cannot add any more ships')

        else:
            self.ships.append((x,y))
            if self.player_type == 'player':
                self.board[x][y] = "@"
     
def random_point(size): 
      
    return random.randint(0, size-1) 


def valid_coordination(row,col,board): 
    try:
        if not( (row in range(5) ) or (col in range(5) ) ) :
            raise ValueError(
                f"the position you entered is out of range!"
            )
        elif (row,col) in board.ships:
            raise ValueError(
                f"You entered this location before"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True
 


def populate_board(board):
    while True:
            c_row=random_point(5)
            c_col=random_point(5)
            if (c_row,c_col ) not in board.ships:
                if board.player_type=='player':
                    board.board[c_row][c_col]='@'
                    board.add_ship(c_row,c_col,'player')
                return board  # i have to make sure that whhich one i have to put here the class or coordination. 
                break



def make_guess(board):
       
    if board.player_type=='player':
        h_row=input('please enter the row\n')
        h_col=input ('please enter the column\n')
        if valid_coordination(h_row,h_col,board):
            return board # i have to make sure that whhich one i have to put here the class or coordination. 
                
    else :
        c_row=random_point(5)
        c_col=random_point(5)
        if valid_coordination(c_row, c_col, board):
            board.guesses=[c_row,c_col]
            return board  # i have to make sure that whhich one i have to put here the class or coordination. 
        
 
 
def play_game(c_board,h_board): 
    
    print('*'*15)
    print(c_board.name + "'s board : ")
    c_board.print()
    print('*'*15)
    print(h_board.name + "'s board : ")
    h_board.print()

    while True:
        make_guess(c_board)



    

 
def new_game():
    size=5 
    ships_num=4 
    human_player='player' 
    computer_player='computer' 

    print("*"*30)
    print('welcom to the battleship game')
    print("*"*30)
    name=input ('please enter your name : \n')
    print(' '*40)
    player_one_board=Board(name, size , ships_num, human_player) 
    player_computer_board =Board('computer', size, ships_num, computer_player) 
     
    
    for _ in range(ships_num):
        populate_board(player_one_board)
        populate_board(player_computer_board)
    
    play_game(player_computer_board, player_one_board)




new_game()