# https://leetcode.com/problems/pascals-triangle/submissions/
# Given an integer numRows, return the first numRows of Pascal's triangle.


def generate(numRows):
    op = []
    if numRows == 1:
        op.append([1])
        return op
    if numRows == 2:
        op.append([1])
        op.append([1, 1])
        return op
    op.append([1])
    op.append([1, 1])
    # print(op)
    for i in range(2, numRows):
        temp = []
        prev = op[i-1]
        for j in range(i+1):
            if j == 0:
                temp.append(1)
                continue
            if j == i:
                temp.append(1)
                continue
            temp.append(prev[j-1]+prev[j])
        op.append(temp)
    return op
            

numRows = 5
print(generate(numRows))