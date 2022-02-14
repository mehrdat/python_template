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
        if not( (int(row) in range(5) ) and (int(col) in range(5) ) ) :
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
        h_row=int(input('please enter the row\n'))
        h_col=int(input ('please enter the column\n'))
        if valid_coordination(h_row,h_col,board):
            board.guesses=[h_row,h_col]
            #return board.guess(h_row,h_col) # i have to make sure that whhich one i have to put here the class or coordination. 
            return h_row,h_col
            
    else :
        c_row=random_point(5)
        c_col=random_point(5)
        if valid_coordination(c_row , c_col , board):
            board.guesses=[c_row,c_col]
            #return board.guess(c_row,c_col)  # i have to make sure that whhich one i have to put here the class or coordination. 
            return c_row,c_col
        
 
 
def play_game(c_board,h_board): 
    
    h_hit=0
    c_hit=0
    print('*'*15)
    print(c_board.name + "'s board : ")
    c_board.print()
    print('*'*15)
    print(h_board.name + "'s board : ")
    h_board.print()

    h_row,h_col=make_guess(h_board)
    c_row,c_col=make_guess(c_board)
    print(' '*35)
    print('*'*35)
    print(f'player guessed {(h_row,h_col)}')
    

    if h_board.guess(h_row, h_col)=='Hit':
        print(f'you have got a Hit !')
        h_hit += 1
    else:
        print('You missed this time !')
        print('*'*35)
    print(f'computer guessed {(c_row,c_col)}')
    if c_board.guess(c_row, c_col)=='Hit':
        print(f'computer has got a Hit !')
        c_hit += 1
    else:
        print('computer missed this time !')
    print(' '*35)
    print('after this round the scores are :')
    print(f'{h_board.name} : {h_hit} --- computer: {c_hit} ' )
    print(' '*35)
    print('*'*35)

    
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