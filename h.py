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
            print(" ".join(row))
         
         
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
            ships.append((x,y))
            if self.player_type=='player':
                self.board[x][y]="@"
     
def random_point(size): 
      
    return random.randint(0, size-1) 


def valid_coordination(row,col,borad): 
    try:
        if (row in range(0,5)) and (col in range(0,5)) :
            raise ValueError(
                f"the position you entered is out of range!"
            )
        elif  board.guess()=='Miss':
            raise ValueError(
                f"You entered this location before"
            )
    except:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True
 


def populate_board(board):
    while True:
            c_row=random_point(5)
            c_col=random_point(5)
            if valid_coordination(c_row, c_col, borad):
                board.add_ship(c_row,c_col)
                return board  # i have to make sure that whhich one i have to put here the class or coordination. 
                break



def make_guess(board):
       
    if board.type=='player':
        while True:
            h_row=input('please enter the row\n')
            h_col=input ('please enter the column\n')
            if valid_coordination(h_row,h_col,board):
                return board # i have to make sure that whhich one i have to put here the class or coordination. 
                break
    else :
        while True:
            c_row=random_point(5)
            c_col=random_point(5)
            if valid_coordination(c_row, c_col, borad):
                board.add_ship(c_row,c_col)
                return board  # i have to make sure that whhich one i have to put here the class or coordination. 
                break
 
 
def play_game(c_board,h_board): 
    print('welcom to the battleship game')
    print('*'*15)
    print(board.name + "'s board : ")
    c_board.print()
    print('*'*15)
    print(board.name + "'s board : ")
    h_board.print()

    

 
def new_game():
    size=5 
    ships_num=4 
    human_player='human_player' 
    computer_player='computer' 
     
    name=input ('please enter your name : \n') 
    player_one_board=Board(name, size , ships_num, human_player) 
    player_computer_board =Board('computer', size, ships_num, computer_player) 
     
    
    for _ in range(ships_num):
        populate_board(player_one_board)
        populate_board(player_computer_board)
    
    play_game(player_computer_board, player_one_board)




new_game()