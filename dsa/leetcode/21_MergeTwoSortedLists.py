# https://leetcode.com/problems/merge-two-sorted-lists/
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.



def makeLL(l):
    t = len(l)
    if len(l) == 0:
        return ListNode(None, None)
    x = ListNode(l[0], None)
    y = x
    for i in range(1, t):
        temp = ListNode(l[i], None)
        x.next = temp
        x = temp
    # print(y)
    # while True:
    #     print(y.val)
    #     y = y.next
    #     if y == None:
    #         break
    return y
      
      
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        x = ListNode(None, None)
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val < list2.val:
            x.val = list1.val
            list1 = list1.next
        else:
            x.val = list2.val
            list2 = list2.next
        op = x
        while True:
            if list1 == None or list2 == None:
                break
            if list1.val < list2.val:
                temp = ListNode(list1.val, None)
                x.next = temp
                x = temp
                list1 = list1.next
            else:
                temp = ListNode(list2.val, None)
                x.next = temp
                x = temp
                list2 = list2.next
        if list1 == None:
            while True:
                temp = ListNode(list2.val, None)
                x.next = temp
                x = temp
                list2 = list2.next
                if list2 == None:
                    break
        else:
            while True:
                temp = ListNode(list1.val, None)
                x.next = temp
                x = temp
                list1 = list1.next
                if list1 == None:
                    break
        return op


  

list1 = [1,2,4]
list2 = [1,3,4]
list1 = makeLL(list1)
list2 = makeLL(list2)
obj = Solution()
op = obj.mergeTwoLists(list1, list2)
while True:
    print(op.val)
    op = op.next
    if op == None:
        break