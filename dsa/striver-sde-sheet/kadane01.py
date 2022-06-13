# brute force 
# input: array of intergers
# output: contiguous subarray with max. sum, print both the sum and the sybarray element

def output(arr):
    maxSum = arr[0]
    lim=len(arr)
    lowerLimit = 0
    upperLimit = 0
    sum = 0
    for i in range(0, lim):
        # sum = arr[i]
        sum = 0
        for j in range(i, lim):
            sum = sum + arr[j]
            if sum > maxSum:
                maxSum = sum
                lowerLimit = i
                upperLimit = j
    return [lowerLimit, upperLimit, maxSum]
    
ip = list(input().split(' '))
arr = list(map(int, ip))

op = output(arr)
a1 = []
for i in range(op[0], op[1]+1):
    a1.append(arr[i])
print('Max Subarray Element(s): ', a1)
print('Max Subarray Sum: ', op[2])