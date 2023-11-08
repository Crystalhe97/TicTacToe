from logic import check_winner

def get_empty_board():
    return[
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def print_board(board):
    for row in board:
        print(row)   #print will print the variable in a new line

def get_player_input():
    """
    input:
    row, col
    return:
        row: int -> the index of row
        col: int -> the index of column
    """
    #prompt = f"player {current_player}, Please input your move, e.g. row,col/n"
    prompt = f"player {current_player} > "
    player_input = input(prompt) #this is a string
    # "1,1" .split(',') -> ["1","1"]
    row_col_list = player_input.split(',')   #["1","1"]
    row, col = [int(x) for x in row_col_list] #[1,1]
    return row,col

def switch_player(current_player):
    if current_player == 'X':
        return 'O'
    return 'X'

if __name__ == '__main__':
    current_player = 'X'
    board = get_empty_board() # get an empty board
    winner = None

    while winner is None:
        print_board(board)# print the board
        try:
            row, col = get_player_input() #ask user input
        except ValueError:
            print("Invalid imput, try again")
            continue
        
        #mark the board
        board[row][col] = current_player
        winner = check_winner(board) #"O", "X" -> break out the loop


        current_player = switch_player(current_player)
        #current_player = "X" if current_player == "O" else "O"
    
    # check for winner
    # check if game is draw
    # print the winner
