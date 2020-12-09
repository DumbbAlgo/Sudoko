#generating random valid sudoko puzzles
import random
board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]                             
for i in range(3):
    for j in range(3):
        x = random.choice(l)
        board[i][j] = x
        l.remove(x)
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(3, 6):
    for j in range(3, 6):
        x = random.choice(l)
        board[i][j] = x
        l.remove(x)
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(6, 9):
    for j in range(6, 9):
        x = random.choice(l)
        board[i][j] = x
        l.remove(x)
k1 = 3
k2 = 3
def sudo(board, k1=3, k2=3):
    #here we will print the sudoko
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
sudo(board)
print()
def zero_search(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]==0:
                return (row, col)
    return ("no", "no")
def is_valid(board, val, pos):
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
solve_it(board)
for i in range(50):

    i = random.randint(0, 8)
    j = random.randint(0, 8)
    while board[i][j]==0:
        i = random.randint(0, 8)
        j = random.randint(0, 8)
    board[i][j] = 0
sudo(board)
