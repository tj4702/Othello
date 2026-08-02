
board = [[''] * 8 for _ in range(8)]

board[3][3] = 'W'
board[4][4] = 'W'
board[3][4] = 'B'
board[4][3] = 'B'


dirs = [(0,1), (1,0), (-1,0),(1,1) , (-1,-1), (1,-1), (-1,1), (0,-1)]

def isValid(r, c, color):

    if board[r][c] != '':
        print('Choose an empty cell for your move')
        return False

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        change = 0 
        while 0 <= nr < 8 and 0 <= nc < 8 and board[nr][nc] != '' :
            if board[nr][nc]  == color and change >0:
                return True
            change +=1
            nr, nc = nr+ dr, nc +dc
    
    print('Not a valid move')
    return False


def makeMove(r,c, color):

    if not isValid(r,c,color):
        print('Make a valid move')
        return 
    
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


    print('Changes have been made')
    

makeMove(2, 3, 'B')
print(board)







