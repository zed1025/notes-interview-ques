# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/282372/Java-solution-with-all-3-follow-up-questions

# brute force
def intersect(nums1, nums2):
    x = len(nums1)
    y = len(nums2)
    op = []
    i = 0
    if x <= y:
        while i < len(nums1):
            if nums1[i] in nums2:
                op.append(nums1[i])
                nums2.remove(nums1[i])
                nums1.pop(i)
                i = 0
            else:
                i = i+1
        return op
    else:
        while i < len(nums2):
            if nums2[i] in nums1:
                op.append(nums2[i])
                nums1.remove(nums2[i])
                nums2.pop(i)
                i = 0
            else:
                i = i+1
        return op


# optimal, similar to merge sort merge method
def intersect2(nums1, nums2):
    x = len(nums1)
    y = len(nums2)
    i = j = 0
    op = []
    nums1.sort()
    nums2.sort()
    while i < x and j < y:
        if nums1[i] == nums2[j]:
            op.append(nums1[i])
            i = i+1
            j = j+1
        elif nums1[i] > nums2[j]:
            j = j+1
        else:
            i = i+1
    return op


# optimal using hashmaps
def intersect3(nums1, nums2):
    mymap = {}
    op = []
    if len(nums1) > len(nums2):
        for i in nums1:
            if i in mymap:
                mymap[i] += 1
            else:
                mymap[i] = 1
        for j in nums2:
            if j in mymap:
                if mymap[j] == 0:
                    continue
                op.append(j)
                mymap[j] -= 1
        return op
    else:
        for i in nums2:
            if i in mymap:
                mymap[i] += 1
            else:
                mymap[i] = 1
        for j in nums1:
            if j in mymap:
                if mymap[j] == 0:
                    continue
                op.append(j)
                mymap[j] -= 1
        return op


nums1 = [3, 1, 2]
nums2 = [1,1]
# op = intersect(nums1=nums1, nums2=nums2)
# op = intersect2(nums1=nums1, nums2=nums2)
op = intersect3(nums1=nums1, nums2=nums2)
print(op)
