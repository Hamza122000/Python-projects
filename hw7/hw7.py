
#==========================================
# Purpose: (checks if there is a common variable between 3 different lists?)
# Input Parameter(s): (grades which represented the students that got goo grades,sleep which represents the students that got good sleep, life which represents the students that have a good social life)
# Return Value(s): (it returns the students who managed to be able to have all 3. good grades, a good social life and good hours of sleep)
#==========================================
def wizards(grades,life,sleep):
    ls=[]
    for i in grades:
        for x in life:
            for f in sleep:
                if i==x and i==f:
                    ls.append(i)
    return ls


#==========================================
# Purpose: (checks if there are any empty slots and returns the index number of those slots?)
# Input Parameter(s): board which represents the board of the tic tac toe game as a list
# Return Value(s): returns the index number of any empty slots in the board
#==========================================

def open_slots(board):
    ls=[]
    for x in range(0,9):
            if board[x] == '-':
                ls.append(x)
    return ls



#==========================================
# Purpose: see the combination of the tic tac toe game and checks if there is any winner or loser or if it is a tie
# Input Parameter(s): board which represents the board of the tic tac toe game as a list
# Return Value(s): returns x is the winner of the game is x, o if the winner of the game is o, D if it is a draw
#==========================================

def winner(board):
    for i in board:
        D ='D'
        slot = '-'
        if board[0]== board[1] and board[0]==board[2] and board[0] != '-':
            return board[0]
        elif board[3]== board[4] and board[3]== board[5] and board[3] != '-':
            return board[3]
        elif board[6]== board[7] and board[6]==board[8] and board[6] != '-':
            return board[6]
        elif board[0]== board[3] and board[0]==board[6] and board[0] != '-':
            return board[0]
        elif board[1]== board[4] and board[1]==board[7] and board[1] != '-':
            return board[1]
        elif board[2]== board[5] and board[2]==board[8]and board[2] != '-':
            return board[2]
        elif board[0]== board[4] and board[0]==board[8] and board[0] != '-':
            return board[0]
        elif board[2]== board[4] and board[2]==board[6] and board[2] != '-':
            return board[2]
        elif i=='-':
            return slot 
    return D

#==========================================
# Purpose: it makes the computer generate a game ot tic tac toe
# Input Parameter(s): none
# Return Value(s): returns x is the winner of the game is x, o if the winner of the game is o, D if it is a draw
#==========================================
import random
       
def tic_tac_toe():
    ls=9*['-']
    turn=0
    for i in range(0,9):
        slots=open_slots(ls)
        if turn%2==0:
            which_spot=random.choice(slots)
            ls[which_spot]='X'
            turn+=1
            if winner(ls)!='-':
                return winner(ls)

        else:
            board_state=1
            min_index=slots[0]
            for i in slots:
                ls2=ls[:]
                ls2[i]='O'
                result_state=force_win(ls2)
                if result_state<board_state:
                    board_state=result_state
                    min_index=i
            ls[min_index]='O'
            turn+=1
            if winner(ls)!='-':
                return winner(ls)

#==========================================
# Purpose: run a computer genrerate tic toc toe game at a given amount of times
# Input Parameter(s): the number of time the game is suppose to run
# Return Value(s): returns the number of times x won, the number of times o won, and the number of times they tied
#==========================================
def play_games(n):
    x_num_win=0
    o_num_win=0
    d_num_win=0
    for i in range(0,n+1):
        result=tic_tac_toe()
        if result=='X':
            x_num_win+=1
        elif result=='O':
            o_num_win+=1
        else:
            d_num_win+=1
    print('x wins:',x_num_win)
    print('O wins:',o_num_win)
    print('Draws:',d_num_win)

#==========================================
# Purpose:  this program takes in a number and uses the collatz theory on it to determine whether the theory applies to the number or not
# Input Parameter(s): a positive intenger 
# Return Value(s): returns a list of all the numbers derived from that number when the collatz theory is applied
#==========================================

def collatz(n):
    n=int(n)
    if n/2==1:
        return [1]
    elif n %2==0:
        return [n]+collatz(n/2)
    elif n%2!=0:
        return [n]+collatz(3*n+1)

#==========================================
# Purpose: takes a list of numbers and returns the minimum value
# Input Parameter(s): a list of intengers 
# Return Value(s): returns the minimum number
#==========================================

def find_min(ls):
    return help_func(ls,0,ls[0])
def help_func(ls,i,min_number):
    if not i<len(ls):
        return min_number
    else:
        if ls[i]<min_number:
            min_number=ls[i]
        i=i+1
        return help_func(ls,i,min_number)
    
#==========================================
# Purpose: runs a game of tic tac toe using recursion to ensure each player fills a spot that will give them the best result. in this game the spot chosen is not at random
# Input Parameter(s): a board of tic tac toe game
# Return Value(s): the highest state that eiter X or O can use

#==========================================


      
def force_win(board):
    if winner(board)!='-':
        y = winner(board)
        if y=='X':
            state = 1
            return state
        elif y=='O':
            state = -1
            return state
        else:
            state = 0
            return state
    
    else:
        x=len(open_slots(board))
        if x %2!=0:
            turn='X'
        else:
            turn='O'
        if turn=='X':
            board_state=-1
            slots=open_slots(board)
            for i in slots:
                board2=board[:]
                board2[i]='X'
                result_state=force_win(board2)
                if result_state>board_state:
                    board_state=result_state
            return board_state
        if turn=='O':
            slots=open_slots(board)
            board_state=1
            for i in slots:
                board2=board[:]
                board2[i]='O'
                result_state=force_win(board2)
                if result_state<board_state:
                    board_state=result_state
            return board_state



      
