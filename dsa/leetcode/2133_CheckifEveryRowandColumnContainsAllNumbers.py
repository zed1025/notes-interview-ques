# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/submissions/
# https://leetcode.com/discuss/general-discussion/199808/can-i-define-another-function-in-python3-in-solution
# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.


def all_unique(l):
    return len(l) == len(set(l))

# brute force
def checkValid(matrix):
    # print(matrix)
    for i in range(len(matrix)):
        if not all_unique(matrix[i]):
            return False
    # transpose the matrix and check again
    new_mat = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[i])):
            temp.append(matrix[j][i])
        new_mat.append(temp)
    # print(new_mat)
    for i in range(len(new_mat)):
        if not all_unique(new_mat[i]):
            return False
    return True


matrix = [[1,2,3],[3,1,2],[2,3,1]]
print(checkValid(matrix))
