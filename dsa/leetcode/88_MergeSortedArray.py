# https://leetcode.com/problems/merge-sorted-array/
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1


def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if m==0:
        nums1.clear()
        nums1.extend(nums2)
    if n==0:
        print(nums1)
        return
    l = []
    i = j = 0
    flag = 0 # i finished last
    print('Hello')
    while i < m and j < n:
        print('Hello')
        if nums1[i] < nums2[j]:
            l.append(nums1[i])
            i = i+1
            flag = 0 # nums1 inserted last, nums2 remaining
        else:
            l.append(nums2[j])
            j = j+1
            flag = 1 # nums2 inserted last, nums1 remaining
    if flag == 0:
        p = n-j
        while p:
            l.append(nums2[j])
            j = j+1
            p = p-1
    else:
        p = m-i
        while p>0:
            l.append(nums1[i])
            p = p-1
            i = i+1
    nums1.clear()
    nums1.extend(l)
    print(nums1)

nums1 = [1,2,3,0,0,0] 
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)

