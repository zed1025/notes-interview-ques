# https://leetcode.com/problems/reshape-the-matrix/
# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.


def matrixReshape(mat, r, c):
    l = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            l.append(mat[i][j])
    # print(l)
    if r*c != len(l):
        return mat
        
    op = []
    t = 0
    for i in range(r):
        temp = []
        for j in range(c):
            temp.append(l[t])
            t = t+1
        op.append(temp)

    if len(l) == t+1:
        # print(mat)
        return mat
    else:
        # print(op)
        return op


mat = [[1,2],[3,4]]
r = 1
c = 4
print(matrixReshape(mat, r, c))