
import random 

board = [[''] * 8 for _ in range(8)]

board[3][3] = 'W'
board[4][4] = 'W'
board[3][4] = 'B'
board[4][3] = 'B'


dirs = [(0,1), (1,0), (-1,0),(1,1) , (-1,-1), (1,-1), (-1,1), (0,-1)]

def isValid(r, c, color):

    if board[r][c] != '':
        # print('Choose an empty cell for your move')
        return False

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        change = 0 
        while 0 <= nr < 8 and 0 <= nc < 8 and board[nr][nc] != '' :
            if board[nr][nc]  == color and change >0:
                return True
            change +=1
            nr, nc = nr+ dr, nc +dc
    
    # print('Not a valid move')
    return False


def makeMove(r,c, color):

    if not isValid(r,c,color):
        # print('Make a valid move')
        return False
    
    board[r][c] = color 
    
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        change = 0 
        while 0 <= nr < 8 and 0 <= nc <8 and board[nr][nc] != '':
            if board[nr][nc] == color and change > 0:
                for i in range(change):
                    nr, nc = nr - dr, nc - dc
                    board[nr][nc] = color
                
                break
            change +=1 
            nr, nc = nr +dr, nc + dc

    # print('Changes have been made')
    return True

def hasLegalMove(color):
    for r in range(8):
        for c in range(8):
            if isValid(r,c,color):
                return True
    
    return False

def printBoard():
    print('   ' + ' '.join(str(c) for c in range(8)))
    for r in range(8):
        row_str = ' '.join(cell if cell != '' else '.' for cell in board[r])
        print(f'{r}  {row_str}')
    print()


isWhite = True

mode = input('Choose option1: Player vs Player \n Option2 : Player vs Computer\n Input 1 or 2: ')
mode = int(mode)


while mode == 1:

    whiteHasMove = hasLegalMove('W')
    blackHasMove = hasLegalMove('B')

    if not whiteHasMove and not blackHasMove:

        flat = [cell for row in board for cell in row]
        white_count = flat.count('W')
        black_count = flat.count('B')
        if white_count > black_count :
            print(f'White wins with {white_count}')
            print(f'Black count is {black_count}')

        
        elif black_count > white_count :
            print(f'Black wins with {black_count}')
            print(f'White count is {white_count}')

        
        else:
            print('DRAW')

        break



    if isWhite:

        if not whiteHasMove:
            print('White has no valid moves passing turn')
            isWhite = False
            printBoard()
        else:
            raw  = input('White to move:\n input row, col :')
            input_r, input_c = raw.split(',')
            input_r, input_c = int(input_r), int(input_c)
            if makeMove(input_r, input_c, 'W'):
                isWhite = False
                printBoard()
            else:
                print('Input a valid Move')

    else:

        if not  blackHasMove:
            print('Black has no valid moves passing turn')
            isWhite = True
            printBoard()
            
        else:
            raw  = input('Black to move:\n input row, col :')
            input_r, input_c = raw.split(',')
            input_r, input_c = int(input_r), int(input_c)
            if makeMove(input_r, input_c, 'B'):
                isWhite = True
                printBoard()
            else:
                print('Input a valid move')



if mode == 2:
    player_color = input('Player can choose color W or B\n input W or B:  ')
    isPlayer = True
    comp_color = 'W' if player_color == 'B' else 'B'

while mode == 2:

    playerHasMove = hasLegalMove(player_color)
    compHasMove = hasLegalMove(comp_color)

    if not playerHasMove and not compHasMove:
        flat = [cell for row in board for cell in row]
        player_count = flat.count(player_color)
        comp_count = flat.count(comp_color)
        if player_count > comp_count :
            print(f'Player wins with {player_count}')
            print(f'Computer count is {comp_count}')
            
        
        elif comp_count > player_count :
            print(f'Computer wins with {comp_count}')
            print(f'Player count is {player_count}')
         
        
        else:
            print('DRAW')
        
        break




    if isPlayer:

        if not playerHasMove:
            print('White has no valid moves passing turn')
            isPlayer = False
        else:
            raw  = input(f'{player_color} to move:\n input row, col :  ')
            input_r, input_c = raw.split(',')
            input_r, input_c = int(input_r), int(input_c)
            if makeMove(input_r, input_c, player_color):
                isPlayer = False
                printBoard()
            else:
                print('Input a valid Move')

    else:

        if not compHasMove:
            print('White has no valid moves passing turn')
            isPlayer = True
        else:
            input_r, input_c = random.randint(0,7), random.randint(0,7)

            if makeMove(input_r, input_c,comp_color):
                isPlayer = True
                printBoard()
    

    












