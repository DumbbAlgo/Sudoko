board = [[0 ,0 ,0 , 2 ,0 ,5 ,8 ,0 ,0],
         [0 ,0 ,0 ,3, 8 ,0  ,0 ,4 ,0],
         [0 ,0 ,5  ,0, 0 ,9  ,0 ,1 ,0],
         [5 ,4 ,6   ,0 ,2 ,0  ,0 ,7 ,0],
         [0 ,0 ,0   ,0 ,0 ,0  ,0 ,8 ,5],
         [0 ,0 ,3   ,0 ,5 ,4  ,6 ,0 ,0],
         [0 ,1 ,4   ,0 ,0 ,2  ,3 ,0 ,8],
        [9 ,3 ,8   ,5 ,0 ,0 , 0 ,0 ,0],
        [6, 0 ,0  ,0 ,0 ,0  ,7 ,0 ,0]]
k1 = 3
k2 = 3
def sudo(board, k1, k2):
    #print the sudoko
    for i in range(len(board)):
        if i%k2==0 and i!=0:
            print("----------------------------")
        for j in range(len(board[0])):
            if j%k1==0 and j!=0:
                print(" | ", end = "")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
def zero_search(board):
    #searching for empety places, 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]==0:
                return (row, col)
    return ("no", "no")
def is_valid(board, val, pos):
    #checking if puting val at position pos is valid
    for i in range((pos[0] // 3)*3, ((pos[0] // 3)+1)*3):
        for j in range((pos[1] // 3)*3, ((pos[1] // 3)+1)*3):
            if board[i][j] == val and (i,j) != pos:
                return False
    for i in range(len(board)):
        if board[i][pos[1]] == val and pos[0] != i:
            return False
    for i in range(len(board[0])):
        if board[pos[0]][i] == val and pos[1] != i:
            return False
    return True
def solve_it(board):
    #implementing backtracking
    zero = zero_search(board)
    if zero==("no", "no"):
        return True
    else:
        row, col = zero
    for i in range(1,10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            if solve_it(board):
                return True
            board[row][col] = 0
    return False
def is_board_valid(board):
    #checking is your puzzle valid
    for row in range(len(board)):
        for col in range(len(board[0])):
            pos = (row, col)
            val = board[row][col]
            if val==0:
                continue
            # checking if puting val at position pos is valid
            #print(val, pos)
            for i in range((pos[0] // 3) * 3, ((pos[0] // 3) + 1) * 3):
                for j in range((pos[1] // 3) * 3, ((pos[1] // 3) + 1) * 3):
                    if board[i][j] == val and (i, j) != pos:
                        return False
            for i in range(len(board)):
                if board[i][pos[1]] == val and pos[0] != i:
                    return False
            for i in range(len(board[0])):
                if board[pos[0]][i] == val and pos[1] != i:
                    return False
    return True
if is_board_valid(board)==False:
    print("Invalid board!")
else:
    sudo(board, k1, k2)
    print("Solving...")
    solve_it(board)
    print("Board solved!!!")
    sudo(board, k1, k2)