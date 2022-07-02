
# brute force
def maxSubarray1(nums):
    maxSum = nums[0]
    l_limit = 0
    u_limit = 0
    
    x = len(nums)
    for i in range(x):
        sum = 0
        for j in range(i, x):
            sum = sum + nums[j]
            if sum > maxSum:
                maxSum = sum
                l_limit = i
                u_limit = j
    return [maxSum, l_limit, u_limit]

# max subarray, kadane
def kadane(nums):
    max = nums[0] # max so far
    sum = 0 # max end here
    start, end = 0, 0
    s = 0 # to get the indices
    x = len(nums)
    for i in range(0, x):
        sum = sum + nums[i]
        if sum > max:
            max = sum
            start = s
            end = i
        if sum < 0:
            sum = 0
            s = i+1

    return [max, start, end]

# ip = list(input().split(' '))
# ip = list(map(int, ip))
# print(ip)
num = [-2,1,-3,4,-1,2,1,-5,4]
# op = maxSubarray1(num)
op = kadane(num)
print(op[0])
l = []
for i in range(op[1], op[2]+1):
    l.append(num[i])
print(l)
            
