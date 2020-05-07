import random
board = [" "," "," "," "," "," "," "," "," "]
turn = random.randint(1,2)
if turn == 1:
    print("User's turn first")
else:
    print("PC's turn first")
char = input("Select your character: ")
if char == "X":
    human_char = "X"
    pc_char = "O"
elif char == "O":
    human_char = "O"
    pc_char = "X"
else:
    print("worng input try again")
      
def board_game():
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

def user_turn():
    human_move = int(input("where would you like to place your character: "))
    if board[human_move] == " ":
        board.pop(human_move)
        board.insert(human_move,human_char)
        print("\n")
        board_game()
        print("\n")
    else:
        print("slot has been taken try agian")
        user_turn()   
def pc_turn():
    pc_move = int
    pc_move = random.randint(0,8)
    if board[pc_move] == " ":
        board.pop(pc_move)
        board.insert(pc_move,pc_char)
        print("After PC's turn")
        print("\n")
        board_game()
        print("\n")
    else:
        print("slot has been taken try again")
        pc_turn()   
def game():
    if turn == 1:    
        user_turn()
        counter = 0
        for i in range(0,5):
            counter = counter + 1
            winner_check = winner()
            if counter == 4 and winner_check == 0:
                print("its a draw")
                break
            if winner_check == 1:
                break
            else:    
                pc_turn()
                if winner_check == 1:
                    break
                else:
                    user_turn()  
    if turn == 2:
        pc_turn()
        counter = 0
        for i in range(0,5):
            counter = counter + 1
            winner_check = winner()
            if counter == 4 and winner_check == 0:
                print("its a draw")
                break
            if winner_check == 1:
                break
            else:    
                user_turn()
                if winner_check == 1:
                    break
                else:
                    pc_turn()    
def winner():
    winner_looser = 0
    if(
       board[0] == "X" and board[1] == "X" and board[2] == "X"
       or
       board[3] == "X" and board[4] == "X" and board[5] == "X"
       or
       board[6] == "X" and board[7] == "X" and board[8] == "X"
       or
       board[0] == "X" and board[3] == "X" and board[6] == "X"
       or
       board[1] == "X" and board[4] == "X" and board[7] == "X"
       or
       board[2] == "X" and board[5] == "X" and board[8] == "X"
       or
       board[0] == "X" and board[4] == "X" and board[8] == "X"
       or
       board[2] == "X" and board[4] == "X" and board[6] == "X"
       ):
        winner_looser = winner_looser + 1
        print("character X won")
        return winner_looser
        
    elif(
       board[0] == "O" and board[1] == "O" and board[2] == "O"
       or
       board[3] == "O" and board[4] == "O" and board[5] == "O"
       or
       board[6] == "O" and board[7] == "O" and board[8] == "O"
       or
       board[0] == "O" and board[3] == "O" and board[6] == "O"
       or
       board[1] == "O" and board[4] == "O" and board[7] == "O"
       or
       board[2] == "O" and board[5] == "O" and board[8] == "O"
       or
       board[0] == "O" and board[4] == "O" and board[8] == "O"
       or
       board[2] == "O" and board[4] == "O" and board[6] == "O"
       ):
        winner_looser = winner_looser + 1
        print("character O won")
        return winner_looser
        
game()