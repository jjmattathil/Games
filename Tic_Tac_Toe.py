""" This is a script for Tic Tac Toe Game"""

import random

def display_board(board):
    print("\n"*10)
    print('____________\n')
    print(f'|{board[0]}| |{board[1]}| |{board[2]}|')
    print('____________\n')
    print(f'|{board[3]}| |{board[4]}| |{board[5]}|')
    print('____________\n')
    print(f'|{board[6]}| |{board[7]}| |{board[8]}|')
    print('____________')

def player_input():
    marker=''
    while marker not in ['X','O']:
        marker=input("Please enter player 1 marker as 'X' or 'O': ")
        if marker not in ['X','O']:
            print("Please enter a valid marker")
        return marker

def place_marker(board, marker, position):
    board[position]=marker
    return board

def win_check(board, mark):
    if((board[0]==board[1]==board[2]==mark) or (board[3]==board[4]==board[5]==mark) or (board[6] == board[7] == board[8] == mark) or (board[0]==board[3]==board[6]==mark) or (board[1] == board[4] == board[7] == mark) or (board[2]==board[5]==board[8]==mark) or (board[0] == board[4] == board[8] == mark) or (board[2]==board[4]==board[6]==mark)):
        print("Congratulations marker {} won the game".format(mark))
        return True
    else:
        return False

def choose_first():
    out=random.randint(1,2)
    return str(out)

def space_check(board, position):

    if board[position]=='X' or board[position]=='O':
        return False
    else:
        return True

def full_board_check(board):
    for i in range(len(board)):
        if board[i]==' ':
            print(i)
            return False
    return True

def player_choice(board):
    position=''
    while(position not in range(0,9)):
        position=(input("Please enter next postion as a number 0-8: "))
        position=int(position)
        if (position not in range(0,9)):
            print("Enter a number between 0 and 8")
        else:
            if space_check(board, position)==True:
                return position
            else:
                print("This space is already occupied")

def replay():
    play=input("Do you want to play again? type 'Y' or 'N': ")
    if (play=='Y'):
        return True
    else:
        return False

print('Welcome to Tic Tac Toe!')
while True:
    board = [' ']*9
    display_board(board)
    marker1=player_input()
    if(marker1=='X'):
        marker2='O'
    elif(marker1=='O'):
        marker2='X'
    else:
        continue
    first=choose_first()
    if (first=="1"):
        second="2"
    else:
        second="1"
    my_dict={'1':marker1,'2':marker2}
    print(f'player {first} will play first')
    while True:
        ####Player 1

        position=None
        while (position ==None):
            position=player_choice(board)
        board=place_marker(board,my_dict[first], position)
        display_board(board)
        if win_check(board,my_dict[first]):
            break
        if full_board_check(board):
            break
        ###Player 2
        position = None
        while (position == None):
            position = player_choice(board)
        board =place_marker(board,my_dict[second], position)
        display_board(board)
        if win_check(board, my_dict[second]):
            break
        if full_board_check(board):
            break
    if not replay():
        break


