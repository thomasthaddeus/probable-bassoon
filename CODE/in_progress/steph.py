'''
Tic-Tac-Toe
'''
#####################################
##          TIC TAC TOE            ##
##  by Stephanie Ort, Thad Thomas  ##
##            IS 201               ##
##    Fundamentals of Computing    ##
#####################################

import random
import logging
logging.basicConfig(filename='gamelog.txt',
                    filemode='a',level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Start of Program')
BOARD_KEYS = list('123456789')
X, O, BLANK = 'X', 'O', " "

tttBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}
def main():
    '''main file'''
    #Welcome and begin
    print("Welcome to Tic Tac Toe!")
    print("Enter 'q' to quit at anytime!\n")

    # 1. choose who is going for the first turn
    # 2. choose X or O
    # 3. begin

    #Places X's or O's on the board
    order = get_piece() # order should have [O, X] or [X, O]
    print("order = ", order)
    computer = O
    player = X
    for spot in range(9):
        # tttBoard[i] = get_piece() #[O,X] [X,O]
        get_board(tttBoard)
        spot = input('Choose a spot 1-9:')
        print("your spot = ", spot)

    # true loop of game
    while True:
        print(get_board(tttBoard))
        while not empty_space(tttBoard, spot):
            print(f"{player} Its your turn to play. Choose a move")
            turn = input()
            marker(tttBoard, turn, spot)
            # i += 1
            input(tttBoard)

            if check_win(tttBoard, player):
                print(get_board(tttBoard))
                break
            elif check_tie(tttBoard):
                print(get_board(tttBoard))
                break
            player, computer = computer, player
logging.info('End of Program')

# def get_board(board):
#     '''Displays visual representation  of board'''
#     print(board['1'] + '|' + board['2'] + '|' + board['3'])
#     print('-+-+-')
#     print(board['4'] + '|' + board['5'] + '|' + board['6'])
#     print('-+-+-')
#     print(board['7'] + '|' + board['8'] + '|' + board['9'])


def get_piece():
    """Defines which piece the user is and whether they go first or second"""
    while True:
        piece = input("To Play Please Select Either X's or O's:  ").upper()
        if piece == 'X':
            print('You go first!')
            return 'X', 'O'
        elif piece == 'O':
            print('Computer goes first!')
            return 'O','X'
        else:
            print('x or o?')

def player_one():
    '''Who goes first'''
    logging.info("randomly assigns player one")
    if random.randint(0,1)==0:
        return "O"
    else:
        return "X"

def marker(board, free_space, move):
    """draw on the board"""
    logging.debug("drawing on the board")
    board[free_space] = move

def get_board(board):
    '''Displays visual representation  of board'''
    logging.info("get the board")
    topl,topm,topr = board['1'],board['2'],board['3']
    midl,mid,midr  = board['4'],board['5'],board['6']
    botl,botm,botr = board['7'],board['8'],board['9']
    board = f"""
___________________
|     |     |     |
|  {topl}  |  {topm}  |  {topr}  | 1 2 3
|_____|_____|_____|
|     |     |     |
|  {midl}  |  {mid}  |  {midr}  | 4 5 6
|_____|_____|_____|
|     |     |     |
|  {botl}  |  {botm}  |  {botr}  | 7 8 9
|_____|_____|_____|
"""
    return board

def check_win(board, winner):
    '''Checks for winner using the board'''
    logging.info('Checking for winner on the board')
    i, mark = board, winner
    return ((i["1"] == i["2"] == i["3"] == mark) or  # 1. top_horizon
            (i["4"] == i["5"] == i["6"] == mark) or  # 2. mid_horizon
            (i["7"] == i["8"] == i["9"] == mark) or  # 3. bottom_horizon
            (i["1"] == i["4"] == i["7"] == mark) or  # 4. left_vertical
            (i["2"] == i["5"] == i["8"] == mark) or  # 5. middle_vertical
            (i["3"] == i["6"] == i["9"] == mark) or  # 6. right_vertical
            (i["1"] == i["5"] == i["9"] == mark) or  # 7. tl_br
            (i["3"] == i["5"] == i["7"] == mark))    # 8. tr_bl

def empty_space(board, free_space):
    '''Check if space is free on the board'''
    return free_space in BOARD_KEYS and board[free_space] == BLANK

def check_tie(board):
    '''Checks board for a Tie'''
    #logging.info("Checking for a tie")
    for free_space in BOARD_KEYS:
        if board[free_space] == BLANK:
            return False
        else:
            print("Game is a Tie")



# def replay():
#     playAgain = input("Do you want to play again (Y)es / (N)o ?")
#     """Asks if you want to replay TicTacToe"""
#     try:
#         if playAgain.upper() == 'Y':
#             return True
#         elif playAgain.upper() == 'N':
#             return False
#     except ValueError:
#         raise logging.exception
#         print("Value Error: ")
#     else:
#         return main()

# get_board(tttBoard)

if __name__ == '__main__':
    main()
