# https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums) -> bool:
    dict = {}
    for i in nums:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
    flag = False
    for key in dict:
        if dict[key] > 1:
            flag = True
    if flag == True:
        print('true')
    else:
        print('false')

nums = [1,1,1,3,3,4,3,2,4,2]
containsDuplicate(nums)
        