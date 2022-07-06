# https://leetcode.com/problems/valid-sudoku/
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    # Each row must contain the digits 1-9 without repetition.
    # Each column must contain the digits 1-9 without repetition.
    # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.


# def isValidSudoku(board):
#     # checking for all empty board, because its valid
#     all_empty = True
#     for i in range(9):
#         if not all_empty:
#             break
#         for j in range(9):
#             if board[i][j] != '.':
#                 all_empty = False
#                 break
#     if all_empty:
#         print('from all empty')
#         return True

#     # checking rows
#     for i in range(9):
#         hmap = {}
#         for j in board[i]:
#             if j == '.':
#                 continue
#             if j not in hmap:
#                 hmap[j] = 1
#             else:
#                 hmap[j] += 1
#     for key in hmap:
#         if hmap[key] > 1:
#             # print('False from row checking {}'.format(key))
#             return False
#     # checking cols
#     for i in range(9):
#         hmap = {}
#         for j in range(9):
#             if board[j][i] == '.':
#                 continue
#             if board[j][i] not in hmap:
#                 hmap[board[j][i]] = 1
#             else:
#                 hmap[board[j][i]] += 1
#     for key in hmap:
#         if hmap[key] > 1:
#             # print('False from column checking')
#             return False
#     # checking submatrices
#     for i in (0, 3, 6):
#         for j in (0, 3, 6):
#             # print(i, j)
#             x = checkMiniBoard(i, j, board)
#             if x == False:
#                 print(i, j)
#                 # print('False from sum-matrix checking')
#                 return False
#     return True

# def checkMiniBoard(i, j, board):
#     hmap = {}
#     for x in range(i, i+3):
#         for y in range(j, j+3):
#             if board[x][y] == '.':
#                 continue
#             if board[x][y] not in hmap:
#                 hmap[board[x][y]] = 1
#             else:
#                 hmap[board[x][y]] += 1
#     for key in hmap:
#         if hmap[key] > 1:
#             return False
#     return True

def isValidSudoku(board):
    return (is_row_valid(board) and
            is_col_valid(board) and
            is_square_valid(board))

def is_row_valid(board):
    for row in board:
        if not is_unit_valid(row):
            return False
    return True

def is_col_valid(board):
    for col in zip(*board):
        if not is_unit_valid(col):
            return False
    return True
    
def is_square_valid(board):
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_unit_valid(square):
                return False
    return True
    
def is_unit_valid(unit):
    unit = [i for i in unit if i != '.']
    return len(set(unit)) == len(unit)
    


board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
board2 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
board3 = [[".",".","4",".",".",".","6","3","."],
[".",".",".",".",".",".",".",".","."],
["5",".",".",".",".",".",".","9","."],
[".",".",".","5","6",".",".",".","."],
["4",".","3",".",".",".",".",".","1"],
[".",".",".","7",".",".",".",".","."],
[".",".",".","5",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."]]
board4 = [[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."]]
board5 = [["8","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board4))