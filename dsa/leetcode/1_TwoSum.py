# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# https://leetcode.com/discuss/general-discussion/199808/can-i-define-another-function-in-python3-in-solution

# optimised, using hashmap
def solution2(nums, target):
    nummap = {} # hashmap with key as numbers in nums and value as their index
    x = len(nums)
    for i in range(x):
        num = target-nums[i]
        if num in nummap:
            return [nummap[num], i]
        nummap[nums[i]] = i


# brute force
def solution1(nums, target):
    x = len(nums)
    for i in range(0, x-1):
        for j in range(i+1, x):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [0, 0]


num = [2,7,11,15]
target = 9
print(num, target)

# print(solution1(num, target=target))
print(solution2(num, target=target))