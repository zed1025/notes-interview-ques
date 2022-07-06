# https://leetcode.com/problems/search-a-2d-matrix/
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

    # Integers in each row are sorted from left to right.
    # The first integer of each row is greater than the last integer of the previous row.



def searchMatrix(matrix, target):
    if target < matrix[0][0]:
        return False
    for i in range(len(matrix)):
        if target < matrix[i][0]:
            return False
        for j in range(len(matrix[i])):
            if target == matrix[i][j]:
                return True
    # return 'false'






matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
x = searchMatrix(matrix, target)
print(x)